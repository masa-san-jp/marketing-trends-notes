#!/usr/bin/env python3
"""frontmatter を検証し、グラフと被覆集計を生成する。

    python3 tools/build_graph.py            # 検証 + data/graph.json + data/coverage.json + 被覆マップ更新
    python3 tools/build_graph.py --check    # 検証のみ（CI 用・書き込みなし）

検証で落ちるもの: 必須項目の欠落／id・uri とパスの不一致／id 重複／存在しない参照／語彙外の型・関係・
役割・確度／EDTF 違反／解釈系の関係で certainty・source の欠落／verified なのに項目ごとの根拠がない・
根拠が vendor / anecdotal だけ／trend の market・geo・stage・kind・naming・freshness の欠落／
freshness.recheck_by が stage と食い違う／trend 本文に反証の見出しが無い／predictions の形式違反／
本文の相対リンク切れ／俯瞰の依存先が更新されたのに as_of が古い（STALE）。
"""

import json
import re
import sys

import yaml

from kb import (CERTAINTIES, CHANNEL_ROLES, DIR_FOR_TYPE, ENTITIES,
                EVIDENCE_FIELDS_FOR_VERIFIED, INTERPRETIVE_RELATIONS, PREDICTION_OUTCOMES,
                RELATION_TARGET_TYPES, RELATIONS, RETRIEVEDS, ROOT, SATURATIONS, SEARCHED_FIELDS,
                STAGES, STATUSES,
                TREND_KINDS, TYPES, URI_PREFIX, VERIFIABLE_CERTAINTIES, alias_map, build_edges,
                data_as_of, edtf_ok, edtf_year_range, load_config, load_entities,
                read_frontmatter, read_queries, read_searched, recheck_deadline, resolve,
                search_entities)

OVERVIEWS = ROOT / "overviews"
MARK_START = "<!-- generated:coverage:start -->"
MARK_END = "<!-- generated:coverage:end -->"

# 反証の見出し。書けないならそれはトレンドではなく感想（docs/schema.md「本文の型」）
REFUTATION_HEADING = "## 反証"


def find_todos(value, path=""):
    """frontmatter を再帰に歩いて、TODO が残る場所をパス付きで返す。

    top-level の文字列だけ見ると、naming.self_identified: TODO のような入れ子の雛形残りを見逃し、
    「TODO が1つでも残っていると落ちる」という雛形の約束が嘘になる。
    """
    if isinstance(value, str):
        return [path] if "TODO" in value else []
    if isinstance(value, dict):
        return [p for k, v in value.items()
                for p in find_todos(v, f"{path}.{k}" if path else str(k))]
    if isinstance(value, list):
        return [p for i, v in enumerate(value) for p in find_todos(v, f"{path}[{i}]")]
    return []


def validate(entities, records, cfg, errors):
    seen = {}
    alias_owner = {}
    aliases = alias_map(entities)
    for path, meta, body in records:
        rel = meta["path"]

        def err(msg):
            errors.append(f"{rel}: {msg}")

        for key in ("id", "uri", "type", "label_ja", "sources", "status", "updated"):
            if not meta.get(key):
                err(f"必須項目 {key} が空")
        if any("TODO" in str(s) for s in meta.get("sources") or []):
            err("sources に TODO が残っている（出典URLを入れる）")

        etype = meta.get("type")
        if etype not in TYPES:
            err(f"未知の type: {etype}")
        else:
            expected = f"{etype}/{path.stem}"
            if meta.get("id") != expected:
                err(f"id とパスが不一致（id={meta.get('id')} / 期待={expected}）")
            if meta.get("uri") != URI_PREFIX + expected:
                err(f"uri は {URI_PREFIX}{expected} にする（今: {meta.get('uri')}）")
            if path.parent.name != DIR_FOR_TYPE[etype]:
                err(f"type={etype} は entities/{DIR_FOR_TYPE[etype]}/ に置く")

        if meta.get("id") in seen:
            err(f"id が重複: {meta.get('id')}（既出: {seen[meta['id']]}）")
        seen[meta.get("id")] = rel

        # sources は上で専用メッセージ、path は自分で注入した値なので除いて、残り全体を再帰で見る
        for p in find_todos({k: v for k, v in meta.items() if k not in ("path", "sources")}):
            err(f"{p} に TODO が残っている（雛形のまま）")

        if meta.get("status") not in STATUSES:
            err(f"status は {sorted(STATUSES)} のどれか（今: {meta.get('status')}）")

        if etype == "trend":
            validate_trend(meta, body, cfg, err)
        if etype == "practice" and meta.get("saturation") is not None \
                and meta["saturation"] not in SATURATIONS:
            err(f"saturation は {sorted(SATURATIONS)} のどれか（今: {meta['saturation']}）")

        t = meta.get("time") or {}
        for field in ("start", "end"):
            if not edtf_ok(t.get(field)):
                err(f"time.{field} が EDTF Level 1 サブセットに合わない: {t.get(field)!r}")

        auth = meta.get("authority") or {}
        if not auth.get("wikidata") and not auth.get("none_reason"):
            err("典拠が無いときは authority.none_reason に「何を検索して無かったか」を書く")

        for a in meta.get("aliases") or []:
            if a in entities:
                err(f"alias {a} が既存の id と衝突している")
            if a in alias_owner and alias_owner[a] != meta.get("id"):
                err(f"alias {a} が {alias_owner[a]} と重複している（同じ旧IDを2つのエンティティが名乗れない）")
            alias_owner[a] = meta.get("id")

        for r in meta.get("relations") or []:
            rtype = r.get("type")
            if rtype not in RELATIONS:
                err(f"未知の関係 type: {rtype}")
                continue
            allowed = RELATION_TARGET_TYPES.get(rtype)
            # alias（旧ID）を指していても型検証が素通りしないよう、実IDに解決してから見る
            target = entities.get(resolve(r.get("target"), entities, aliases))
            if allowed and target and target.get("type") not in allowed:
                err(f"{rtype} が指せるのは {sorted(allowed)}。今: {r.get('target')}"
                    f"（{target.get('type')}）")
            if rtype in INTERPRETIVE_RELATIONS:
                if r.get("certainty") not in CERTAINTIES:
                    err(f"{rtype} は certainty が必須（{sorted(CERTAINTIES)}／今: {r.get('certainty')}）")
                if not r.get("source"):
                    err(f"{rtype} は source が必須（解釈を含む関係）")
        for c in meta.get("channels") or []:
            role = c.get("role")
            if role not in CHANNEL_ROLES:
                err(f"未知の channels role: {role}")
                continue
            target = entities.get(resolve(c.get("target"), entities, aliases))
            if target and target.get("type") != "channel":
                err(f"{role} が指せるのは channel。今: {c.get('target')}（{target.get('type')}）")

        validate_evidence(meta, err)

    # build_edges が alias を実IDに解決済みなので、entities に無い先はすべて宙に浮いた参照
    for edge in build_edges(entities):
        if edge.get("derived"):
            continue
        if edge["to"] not in entities:
            errors.append(f"{edge['from']}: 存在しない参照先 {edge['to']}（{edge['type']}）")

    # 本文の相対リンクが実在するか（slug を変えたときに黙って切れるのを防ぐ）
    link_re = re.compile(r"\]\((\.[^)\s]+\.md)\)")
    for path, _meta, body in records:
        for rel_link in link_re.findall(body):
            if not (path.parent / rel_link).resolve().exists():
                errors.append(f"{path.relative_to(ROOT)}: 本文のリンク先が無い {rel_link}")


def validate_trend(meta, body, cfg, err):
    """trend 固有の必須項目。kind（成因）と stage（ライフサイクル）は独立に動く。"""
    if meta.get("kind") not in TREND_KINDS:
        err(f"trend は kind が必須（{sorted(TREND_KINDS)}／今: {meta.get('kind')}）")
    if meta.get("stage") not in STAGES:
        err(f"trend は stage が必須（{sorted(STAGES)}／今: {meta.get('stage')}）")
    if meta.get("market") not in cfg["categories"]:
        err(f"trend は market が必須（config/markets.yaml の categories／今: {meta.get('market')}）")
    if meta.get("geo") not in cfg["geographies"]:
        err(f"trend は geo が必須（config/markets.yaml の geographies／今: {meta.get('geo')}）")

    naming = meta.get("naming")
    if not isinstance(naming, dict) or "self_identified" not in naming:
        err("trend は naming.self_identified が必須（名付けた側と当事者の認識の区別）")
    elif not isinstance(naming.get("self_identified"), bool):
        err(f"naming.self_identified は true / false のどちらか（今: {naming.get('self_identified')!r}）")
    elif naming.get("self_identified") is False and not naming.get("named_by") \
            and not (naming.get("note") or "").strip():
        err("naming.self_identified=false なら named_by か note で命名の経緯を書く")
    if naming and "rejected_by" in naming:
        rb = naming.get("rejected_by")
        if not isinstance(rb, list) or not rb:
            err("naming.rejected_by は「誰が拒んだか」の配列にする（空なら項目を消す）")

    # 鮮度。dead は再検証しない（確定した過去）。それ以外は valid_as_of と、stage に整合する期限が要る
    fresh = meta.get("freshness") or {}
    if meta.get("stage") in STAGES and meta["stage"] != "dead":
        if not fresh.get("valid_as_of"):
            err("trend は freshness.valid_as_of が必須（最後に実データで確認した日）")
        else:
            derived = recheck_deadline(meta["stage"], fresh["valid_as_of"])
            got = str(fresh.get("recheck_by") or "")
            if not got:
                err(f"freshness.recheck_by が空（stage={meta['stage']} なら {derived}）")
            elif derived and got > derived:
                err(f"freshness.recheck_by が stage={meta['stage']} の期限より遅い"
                    f"（{got} > {derived}。早める分にはよい）")

    for pr in meta.get("predictions") or []:
        if not (pr.get("claim") or "").strip():
            err("predictions の各項目に claim が要る")
        if not edtf_ok(pr.get("by")) or not pr.get("by"):
            err(f"predictions の by が EDTF に合わない: {pr.get('by')!r}")
        if pr.get("outcome") is not None and pr["outcome"] not in PREDICTION_OUTCOMES:
            err(f"predictions の outcome は {sorted(PREDICTION_OUTCOMES)} か null（今: {pr['outcome']}）")
        if pr.get("outcome") is not None and not pr.get("resolved"):
            err("predictions に outcome を書くなら resolved（判定した日）も要る")

    # 反証の見出し。stub（枠だけ）には要求しない
    if meta.get("status") in ("draft", "verified") and REFUTATION_HEADING not in body:
        err(f"trend の本文に「{REFUTATION_HEADING}（これが偽なら何が観測されるか）」の見出しが無い"
            "（書けないなら、それはトレンドではなく感想）")


def validate_evidence(meta, err):
    """evidence（主張ごとの根拠）と、verified の2つの関門。

    verified を名乗るには2つを同時に満たす必要がある。
    1. measured / independent / attested の根拠が最低1本——vendor（その主張で儲かる側の数字）と
       anecdotal だけを重ねても verified にはならない（誰が出したか）
    2. retrieved: primary の根拠が最低1本——権威あるURLは読まずにも貼れる。原典を1本も開いて
       いない主張は verified にしない（自分が読んだか）
    """
    for c in meta.get("evidence") or []:
        if not c.get("source"):
            err(f"evidence の {c.get('field')} に source が無い")
        if c.get("certainty") not in CERTAINTIES:
            err(f"evidence の {c.get('field')} の certainty が語彙外: {c.get('certainty')}")
        if c.get("retrieved") not in RETRIEVEDS:
            err(f"evidence の {c.get('field')} の retrieved が語彙外: {c.get('retrieved')}"
                f"（{sorted(RETRIEVEDS)}／原典を開いていないなら summary）")
        if not c.get("as_of"):
            err(f"evidence の {c.get('field')} に as_of（いつ時点の数字か）が無い")

    if meta.get("status") == "verified":
        need = EVIDENCE_FIELDS_FOR_VERIFIED.get(meta.get("type"), set())
        rows = meta.get("evidence") or []
        have = {c.get("field") for c in rows}
        for field in sorted(need - have):
            err(f"verified を名乗るには evidence に {field} の根拠が要る")
        if rows and not any(c.get("certainty") in VERIFIABLE_CERTAINTIES for c in rows):
            err(f"verified を名乗るには {sorted(VERIFIABLE_CERTAINTIES)} の根拠が最低1本要る"
                "（vendor / anecdotal だけでは verified にならない）")
        if rows and not any(c.get("retrieved") == "primary" for c in rows):
            err("verified を名乗るには retrieved: primary の根拠が最低1本要る"
                "（原典を1本も開いていない主張は verified にしない）")


def check_searched(cfg, errors):
    """「調査したが該当なし」の記録を検証する。

    この記録は空欄を「調査済み」に変える——つまり**次の調査をしなくてよい理由になる**。
    だから語彙外のカテゴリや、何を探したか書いていない行は落とす。安く空欄を消せてはいけない。
    """
    for i, r in enumerate(read_searched(), 1):
        where = f"data/searched.jsonl:{i}"
        for field in SEARCHED_FIELDS:
            if not r.get(field):
                errors.append(f"{where}: {field} が空（何を調べたか分からない記録は残さない）")
        if r.get("market") and r["market"] not in cfg["categories"]:
            errors.append(f"{where}: market が語彙外: {r['market']}")
        if r.get("geo") and r["geo"] not in cfg["geographies"]:
            errors.append(f"{where}: geo が語彙外: {r['geo']}")


def check_overview_freshness(entities, errors):
    """俯瞰の depends_on が as_of より後に更新されていたら STALE として落とす。"""
    for path in sorted(OVERVIEWS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        meta = yaml.safe_load(text.split("---\n", 2)[1]) or {}
        as_of = str(meta.get("as_of") or "")
        for dep in meta.get("depends_on") or []:
            target = entities.get(dep)
            if target is None:
                errors.append(f"overviews/{path.name}: depends_on に存在しない {dep}")
            elif as_of and str(target.get("updated")) > as_of:
                errors.append(
                    f"overviews/{path.name}: STALE — {dep} が {target['updated']} に更新（as_of={as_of}）")


def coverage(entities, cfg):
    """trend × カテゴリ × 開始年の被覆と、受け入れ条件の達成度。

    **stub は実績に数えない。** 枠だけのファイルで件数を満たせてしまうと、受け入れ条件が意味を失う。
    鮮度は時計ではなくデータの最新日（as_of）に対して測る——生成物を決定的に保つため
    （生きた時計での鮮度は audit.py --now で見る）。
    """
    as_of = data_as_of(entities)
    trends = {i: m for i, m in entities.items() if m.get("type") == "trend"}
    counted = {i: m for i, m in trends.items() if m.get("status") in ("draft", "verified")}
    cats = cfg["categories"]
    th = cfg["thresholds"]
    grid, per_cat = {}, {c: 0 for c in cats}
    stale, vendor_only, isolated = [], [], []
    unread, hearsay = [], []
    searched_by_cat = {}
    for r in read_searched():
        searched_by_cat.setdefault(r.get("market"), []).append(r)
    all_edges = build_edges(entities)
    edge_ends = {e["from"] for e in all_edges} | {e["to"] for e in all_edges}

    for tid, meta in counted.items():
        cat = meta.get("market") if meta.get("market") in cats else "market-unknown"
        lo, _hi = edtf_year_range((meta.get("time") or {}).get("start"))
        year = str(lo) if lo else "unknown"
        if cat in per_cat:
            per_cat[cat] += 1
        grid.setdefault(cat, {}).setdefault(year, 0)
        grid[cat][year] += 1
        recheck = str((meta.get("freshness") or {}).get("recheck_by") or "")
        if meta.get("stage") != "dead" and recheck and recheck < as_of:
            stale.append(tid)
        rows = meta.get("evidence") or []
        if rows and all(c.get("certainty") == "vendor" for c in rows):
            vendor_only.append(tid)
        # 分母は counted（stub を除く trend）。一覧と比率が食い違わないよう同じループで拾う
        if not any(c.get("retrieved") == "primary" for c in rows):
            unread.append(tid)
        if not any(c.get("certainty") in VERIFIABLE_CERTAINTIES for c in rows):
            hearsay.append(tid)
        if tid not in edge_ends:
            isolated.append(tid)

    measured_ids = sorted(
        i for i, m in entities.items()
        if any(c.get("certainty") == "measured" for c in m.get("evidence") or []))
    resolved_predictions = sum(
        1 for m in entities.values() for p in m.get("predictions") or [] if p.get("resolved"))
    practices = {i: m for i, m in entities.items()
                 if m.get("type") == "practice" and m.get("status") in ("draft", "verified")}
    linked_practices = sum(
        1 for i, m in practices.items()
        if any(r.get("type") == "responds_to" for r in m.get("relations") or []))

    total = len(counted)
    return {
        "as_of": as_of,
        "trend_total": total,
        "trend_stub_excluded": len(trends) - total,
        "by_status": {s: sum(1 for m in trends.values() if m.get("status") == s)
                      for s in sorted(STATUSES)},
        "grid": grid,
        "per_category": per_cat,
        "stale": sorted(stale),
        "vendor_only": sorted(vendor_only),
        "searched": searched_by_cat,
        "unread": sorted(unread),
        "hearsay": sorted(hearsay),
        "isolated": sorted(isolated),
        "measured": measured_ids,
        "progress": {
            "trend_total": f"{total}/{th['trend_total']}（stub {len(trends) - total}件は不算入）",
            "vendor_only_ratio": f"{(len(vendor_only) / total if total else 0):.2f}"
                                 f"（上限 {th['vendor_only_max_ratio']}）",
            "primary_read_ratio": f"{((total - len(unread)) / total if total else 0):.2f}"
                                  f"（下限 {th['primary_read_min_ratio']}・原典を実読した根拠を持つ trend）",
            "independent_ratio": f"{((total - len(hearsay)) / total if total else 0):.2f}"
                                 f"（下限 {th['independent_min_ratio']}・"
                                 f"independent / attested / measured の根拠を持つ trend）",
            "self_measured": f"{len(measured_ids)}/{th['self_measured_min']} 件が measured の根拠を持つ",
            "per_category_min": f"{sum(1 for n in per_cat.values() if n >= th['per_category_min'])}"
                                f"/{len(cats)} カテゴリが {th['per_category_min']}件以上",
            "stale_ratio": f"{(len(stale) / total if total else 0):.2f}"
                           f"（上限 {th['stale_max_ratio']}・as_of={as_of} 時点）",
            "practice_linked": f"{linked_practices}/{len(practices)} の practice が"
                               f" responds_to を持つ（下限比率 {th['practice_linked_ratio']}）",
            "resolved_predictions": f"{resolved_predictions}/{th['resolved_prediction_min']} 件の"
                                    "予測が答え合わせ済み",
        },
    }


def render_coverage(cov, cfg, entities):
    cats = cfg["categories"]
    years = sorted({y for row in cov["grid"].values() for y in row if y != "unknown"}, key=int)
    cols = [(y, y) for y in years] + [("unknown", "年代不明")]
    header = "| カテゴリ | " + " | ".join(label for _k, label in cols) + " | 計 |"
    sep = "|---" * (len(cols) + 2) + "|"
    lines = [f"データの最新日: {cov['as_of']} — `python3 tools/build_graph.py` が生成（手で書き換えない）", "",
             f"trend **{cov['trend_total']}** 件（stub {cov['trend_stub_excluded']}件は不算入）"
             f"／内訳 {cov['by_status']}", "", header, sep]
    for c, conf in cats.items():
        row = cov["grid"].get(c, {})
        cells = " | ".join(str(row.get(k, 0) or "") for k, _label in cols)
        # 0件でも意味が2つある。調べた記録があるなら「未着手」ではないので、そう見せる
        n = cov["per_category"].get(c, 0)
        total_cell = str(n) if n else (f"0（調査済 {len(cov['searched'].get(c, []))}）"
                                       if cov["searched"].get(c) else "0")
        lines.append(f"| {c}（{conf['label_ja']}） | {cells} | {total_cell} |")
    if cov["grid"].get("market-unknown"):
        row = cov["grid"]["market-unknown"]
        cells = " | ".join(str(row.get(k, 0) or "") for k, _label in cols)
        lines.append(f"| **market 未設定** | {cells} |  |")
    if cov["stale"]:
        lines += ["", f"**鮮度切れ**（recheck_by < {cov['as_of']}）: {', '.join(cov['stale'])}"]
    if cov["vendor_only"]:
        lines += ["", f"**根拠が vendor だけ**: {', '.join(cov['vendor_only'])}"]
    if cov["unread"]:
        lines += ["", "**原典を実読していない**（`retrieved: primary` の根拠が1本も無い）: "
                      f"{', '.join(cov['unread'])}"]
    if cov["hearsay"]:
        lines += ["", "**利害のない根拠が無い**（independent / attested / measured が1本も無い）: "
                      f"{', '.join(cov['hearsay'])}"]
    if cov["searched"]:
        lines += ["", "**調査したが該当が無かった**（空欄との区別。`tools/record_searched.py` の記録）:"]
        for c, rows in sorted(cov["searched"].items()):
            for r in rows:
                src = f"／出典 {len(r.get('sources') or [])}本" if r.get("sources") else "／**出典0本**"
                lines.append(f"- {c}: {r.get('scope')}（{r.get('at')}・{r.get('by')}{src}）")

    # 空振りの記録は残すが、**いま当たる語は出さない**。KB が空だった頃に探された語をそのまま
    # 「無い」と出し続けると、既に入っているものを調べに行かせてしまう。
    asked = {}
    for q in read_queries():
        if q.get("hits") == 0:
            asked[q["term"]] = asked.get(q["term"], 0) + 1
    misses = {t: n for t, n in asked.items() if not search_entities(t, entities)}
    if misses:
        lines += ["", "**探されたが無かった語**（需要のシグナル。多い順）:", ""]
        lines += [f"- {term} — {n}回" for term, n in sorted(misses.items(), key=lambda x: -x[1])]
    filled = sorted(set(asked) - set(misses))
    if filled:
        lines += ["", f"探された当時は無く、いまは入っている語: {', '.join(filled)}"]

    lines += ["", "受け入れ条件の達成度:", ""]
    lines += [f"- {k}: {v}" for k, v in cov["progress"].items()]
    if cov["isolated"]:
        lines += ["", f"関係を持たない trend: {', '.join(cov['isolated'])}"]
    return "\n".join(lines)


def warn_if_hook_off():
    """clone 直後はフックが無効。気づかないまま検証なしで commit できてしまうので、走る度に言う。"""
    import subprocess
    try:
        got = subprocess.run(["git", "-C", str(ROOT), "config", "core.hooksPath"],
                             capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return
    if got != ".githooks":
        print("⚠ commit 前の検証フックが無効です。1回だけ実行してください: "
              "git config core.hooksPath .githooks", file=sys.stderr)


def main():
    check_only = "--check" in sys.argv
    warn_if_hook_off()
    cfg = load_config()
    errors = []
    try:
        entities, records = load_entities()
    except Exception as exc:
        print(f"✗ 読み込み失敗: {exc}", file=sys.stderr)
        return 1

    validate(entities, records, cfg, errors)
    check_overview_freshness(entities, errors)
    check_searched(cfg, errors)

    if errors:
        print(f"✗ {len(errors)} 件:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    edges = build_edges(entities)
    cov = coverage(entities, cfg)
    if check_only:
        print(f"✓ {len(entities)} エンティティ / {len(edges)} 関係 — 問題なし")
        return 0

    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "graph.json").write_text(
        json.dumps({"entities": entities, "edges": edges}, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8")
    (ROOT / "data" / "coverage.json").write_text(
        json.dumps(cov, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")

    cmap = OVERVIEWS / "coverage.md"
    text = cmap.read_text(encoding="utf-8")
    if MARK_START in text and MARK_END in text:
        head, rest = text.split(MARK_START, 1)
        _old, tail = rest.split(MARK_END, 1)
        cmap.write_text(f"{head}{MARK_START}\n{render_coverage(cov, cfg, entities)}\n{MARK_END}{tail}",
                        encoding="utf-8")
    else:
        print("✗ overviews/coverage.md に生成ブロックのマーカーが無い", file=sys.stderr)
        return 1

    print(f"✓ {len(entities)} エンティティ / {len(edges)} 関係")
    print(f"  trend {cov['trend_total']} 件 / " + " / ".join(f"{k}={v}" for k, v in cov["progress"].items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
