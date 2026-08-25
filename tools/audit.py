#!/usr/bin/env python3
"""体系の食い違いと偏りを検査して、次に調べることを KB 自身に出させる。

`build_graph.py --check` が見ているのは**壊れているか**（必須項目・参照先・語彙）。それだけだと、
形は正しいが中身が腐っている状態を誰も指摘しない。マーケティングの知識は美術史と違って
**放っておくだけで偽になる**ので、この層がこのKBでは本体に近い。

    python3 tools/audit.py                    # 検査して data/audit.json を書き、被覆マップに反映
    python3 tools/audit.py --dry-run          # 表示だけ
    python3 tools/audit.py --dry-run --now 2027-01-01   # 生きた時計で鮮度を見る（書き込みなし）
    python3 tools/audit.py --dry-run --fail-on-findings  # findings があれば終了コード2

生成物を決定的に保つため、既定の「いま」は時計ではなくデータの最新日（updated の最大値）。
--now は表示専用（--dry-run が必須）。理由は docs/freshness.md。

検査するもの（すべてマーケティングの構造そのものに関するもの）:
  1. 鮮度切れ — recheck_by を過ぎた trend（stage 別）。このKBで最優先の指摘
  2. ベンダー単独根拠 — evidence が vendor だけ。売り言葉を事実として持っている疑い
  3. 未判定の予測 — by を過ぎたのに resolved が null（答え合わせしていない）
  4. 応答なきトレンド — responds_to で繋がる practice が無い（打ち手に落ちていない）
  5. 単一チャネル観測 — 1つの channel でしか観測していない（「TikTok で流行っている＝世の中の
     トレンド」の誤りを機械が指す）
  6. kind の偏り — あるカテゴリの trend が全部同じ kind（kind がカテゴリの言い換えに堕ちた疑い）
  7. 時間の逆行 — 派生元より先に始まっている／命名年が対象の開始より前
  8. 説明なき死 — stage: dead なのに killed_by が無い（何が殺したか不明のまま）

これらは commit を止めない（壊れてはいないので）。**次に何を調べるかの材料として出す。**
"""

import argparse
import json
import sys
from collections import defaultdict

import yaml

from kb import (ROOT, build_edges, data_as_of, edtf_year_range, load_config, load_entities)

OVERVIEWS = ROOT / "overviews"
OUT = ROOT / "data" / "audit.json"
COVERAGE = OVERVIEWS / "coverage.md"
MARK_START = "<!-- generated:audit:start -->"
MARK_END = "<!-- generated:audit:end -->"


def start_year(meta):
    return edtf_year_range((meta.get("time") or {}).get("start"))[0]


def counted_trends(entities):
    return {i: m for i, m in entities.items()
            if m.get("type") == "trend" and m.get("status") in ("draft", "verified")}


def check_stale(entities, now, findings):
    """recheck_by を過ぎた trend。emerging の鮮度切れは特に速く腐る。"""
    by_stage = defaultdict(list)
    for tid, meta in sorted(counted_trends(entities).items()):
        if meta.get("stage") == "dead":
            continue
        recheck = str((meta.get("freshness") or {}).get("recheck_by") or "")
        if recheck and recheck < now:
            by_stage[meta.get("stage")].append((tid, recheck))
    for stage in ("emerging", "growing", "peak", "declining"):
        for tid, recheck in by_stage.get(stage, []):
            findings.append({"kind": "stale", "about": tid,
                             "text": f"{entities[tid]['label_ja']}（{stage}）の再検証期限 {recheck} を"
                                     f"過ぎている。実データで確かめて valid_as_of を更新するか、"
                                     "stage を動かす"})


def check_vendor_only(entities, findings):
    """根拠が vendor だけの trend。その主張で儲かる側の数字しか無い状態。"""
    for tid, meta in sorted(counted_trends(entities).items()):
        rows = meta.get("evidence") or []
        if rows and all(c.get("certainty") == "vendor" for c in rows):
            findings.append({"kind": "vendor-only", "about": tid,
                             "text": f"{meta['label_ja']} の根拠が vendor だけ。官公庁統計・決算・"
                                     "公開された計測・官公庁統計・決算のどれかで裏を取るか、kind: vendor-pushed を疑う"})


def check_unresolved_predictions(entities, now, findings):
    """期限を過ぎた予測の答え合わせ。当てることではなく、外したと記録することが価値。"""
    for eid, meta in sorted(entities.items()):
        for pr in meta.get("predictions") or []:
            by = str(pr.get("by") or "").rstrip("?~%")
            _lo, hi = edtf_year_range(by)
            # 年だけ・年月だけの期限は、その期間が終わってから「過ぎた」と判定する
            due = {4: f"{by}-12-31", 7: f"{by}-31"}.get(len(by), by) if "X" not in by \
                else (f"{hi}-12-31" if hi else "")
            if due and due < now and not pr.get("resolved"):
                findings.append({"kind": "unresolved-prediction", "about": eid,
                                 "text": f"{meta['label_ja']} の予測「{pr.get('claim')}」"
                                         f"（期限 {by}）が未判定のまま。hit / miss / "
                                         "unresolvable を記録する"})


def check_unanswered_trends(entities, edges, findings):
    """practice が1つも応答していない trend。観測しただけで打ち手に落ちていない。"""
    answered = {e["to"] for e in edges
                if e["type"] == "responds_to" and not e.get("derived")
                and (entities.get(e["from"]) or {}).get("type") == "practice"}
    for tid, meta in sorted(counted_trends(entities).items()):
        if tid not in answered:
            findings.append({"kind": "unanswered", "about": tid,
                             "text": f"{meta['label_ja']} に応答する practice が無い。"
                                     "打ち手に落ちていない（判断材料として未完成）"})


def check_single_channel(entities, findings):
    """1つの channel でしか観測していない trend。プラットフォーム内現象と世の中の変化の混同を疑う。"""
    for tid, meta in sorted(counted_trends(entities).items()):
        if (meta.get("channel_scope") or {}).get("status") != "mapped":
            continue
        targets = {c.get("target") for c in meta.get("channels") or []}
        if len(targets) == 1:
            findings.append({"kind": "single-channel", "about": tid,
                             "text": f"{meta['label_ja']} は {next(iter(targets))} でしか観測して"
                                     "いない。他チャネル・チャネル外（検索・購買・調査統計）でも"
                                     "起きているか確かめる"})


def check_kind_bias(entities, findings):
    """kind がカテゴリの言い換えになっていないか（このカテゴリ＝全部 vendor-pushed、等）。"""
    by_cat = defaultdict(list)
    for tid, meta in counted_trends(entities).items():
        by_cat[meta.get("market")].append(meta.get("kind"))
    for cat, kinds in sorted(by_cat.items()):
        if len(kinds) >= 2 and len(set(kinds)) == 1:
            findings.append({"kind": "kind-bias", "about": cat,
                             "text": f"{cat} の trend {len(kinds)}件が全部 {kinds[0]}。"
                                     "kind がカテゴリの言い換えになっていないか、別の kind の例を1件探す"})


def check_time_order(entities, edges, findings):
    """派生・後続の関係が時間と矛盾していないか。命名が対象より先に無いか。"""
    for e in edges:
        if e.get("derived") or e["type"] not in ("derives_from", "precedes"):
            continue
        a, b = entities.get(e["from"]), entities.get(e["to"])
        if not a or not b:
            continue
        ya, yb = start_year(a), start_year(b)
        if ya is None or yb is None:
            continue
        if e["type"] == "derives_from" and ya < yb:
            findings.append({"kind": "time-order", "about": e["from"],
                             "text": f"{a['label_ja']}（{ya}）が派生元 {b['label_ja']}（{yb}）より先に始まっている"})
        if e["type"] == "precedes" and ya > yb:
            findings.append({"kind": "time-order", "about": e["from"],
                             "text": f"{a['label_ja']}（{ya}）が後続とした {b['label_ja']}（{yb}）より後に始まっている"})
    for eid, meta in entities.items():
        naming = meta.get("naming") or {}
        named = edtf_year_range(naming.get("named_when"))[0]
        start = start_year(meta)
        if named and start and named < start:
            findings.append({"kind": "time-order", "about": eid,
                             "text": f"{meta['label_ja']}: 命名年 {named} が対象の開始 {start} より前"})


def check_unexplained_death(entities, findings):
    """dead なのに killed_by が無い。何が殺したかは、次のトレンドの寿命を測る材料になる。"""
    for tid, meta in sorted(counted_trends(entities).items()):
        if meta.get("stage") != "dead":
            continue
        if not any(r.get("type") == "killed_by" for r in meta.get("relations") or []):
            findings.append({"kind": "unexplained-death", "about": tid,
                             "text": f"{meta['label_ja']} は dead だが killed_by が無い。"
                                     "何が殺したのか（規制・代替・飽和）を event で特定する"})


def render(findings):
    if not findings:
        return "食い違い・偏りの指摘はなし。"
    order = ["stale", "vendor-only", "unresolved-prediction", "unanswered", "single-channel",
             "kind-bias", "time-order", "unexplained-death"]
    label = {"stale": "鮮度切れ", "vendor-only": "根拠がベンダーだけ",
             "unresolved-prediction": "答え合わせしていない予測", "unanswered": "応答なきトレンド",
             "single-channel": "単一チャネル観測", "kind-bias": "kind のカテゴリ偏り",
             "time-order": "時間の矛盾", "unexplained-death": "説明なき死"}
    lines = []
    for k in order:
        rows = [f for f in findings if f["kind"] == k]
        if rows:
            lines.append(f"**{label[k]}**")
            lines += [f"- {f['text']}" for f in rows]
            lines.append("")
    return "\n".join(lines).rstrip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--now", help="鮮度判定に使う日付（YYYY-MM-DD）。--dry-run のときだけ有効")
    ap.add_argument("--fail-on-findings", action="store_true",
                    help="dry-run の結果に findings があれば終了コード2")
    a = ap.parse_args()
    if a.now and not a.dry_run:
        print("--now は --dry-run と一緒に使う（生成物は時計に依存させない）", file=sys.stderr)
        return 1
    if a.fail_on_findings and not a.dry_run:
        print("--fail-on-findings は --dry-run と一緒に使う", file=sys.stderr)
        return 1

    entities, _ = load_entities()
    edges = build_edges(entities)
    now = a.now or data_as_of(entities)
    findings = []

    check_stale(entities, now, findings)
    check_vendor_only(entities, findings)
    check_unresolved_predictions(entities, now, findings)
    check_unanswered_trends(entities, edges, findings)
    check_single_channel(entities, findings)
    check_kind_bias(entities, findings)
    check_time_order(entities, edges, findings)
    check_unexplained_death(entities, findings)

    print(render(findings))
    if a.fail_on_findings and findings:
        return 2
    if not a.dry_run:
        OUT.parent.mkdir(exist_ok=True)
        OUT.write_text(json.dumps({"as_of": now, "findings": findings},
                                  ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        text = COVERAGE.read_text(encoding="utf-8")
        if MARK_START in text and MARK_END in text:
            head, rest = text.split(MARK_START, 1)
            _old, tail = rest.split(MARK_END, 1)
            COVERAGE.write_text(f"{head}{MARK_START}\n{render(findings)}\n{MARK_END}{tail}",
                                encoding="utf-8")
        else:
            print("overviews/coverage.md に監査の生成ブロックが無い", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
