#!/usr/bin/env python3
"""KB の共通部品 — frontmatter の読み込み、スキーマ定義、EDTF、鮮度、グラフ組み立て。

各ツール（build_graph / audit / bundle / new_entity）はここを import する。スキーマの定義はこの1箇所。
art-history-notes の kb.py をフォークし、マーケティング／トレンド用に語彙を差し替えた。
"""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ENTITIES = ROOT / "entities"
CONFIG = ROOT / "config"

# --- スキーマ -----------------------------------------------------------------

DIR_FOR_TYPE = {
    "trend": "trends", "practice": "practices", "channel": "channels", "case": "cases",
    "player": "players", "concept": "concepts", "event": "events", "source": "sources",
}
TYPES = set(DIR_FOR_TYPE)

# trend の成因（何によって起きたか）。vendor-pushed を独立させるのがこのKBの中核——
# 供給側が名付けて売り込んだ括りを、実際の需要変化と同じ棚に置いた瞬間に体系が壊れる。
TREND_KINDS = {"demand-shift", "tech-enabled", "regulation-driven", "vendor-pushed"}
# trend のライフサイクル。dead は鮮度管理から外れる（もう動かない＝確定した過去になる）
STAGES = {"emerging", "growing", "peak", "declining", "dead"}
# practice の飽和度（任意）。「みんなやっているから効かない・逆効果」を機械可読にする
SATURATIONS = {"novel", "spreading", "commoditized", "negative"}
STATUSES = {"stub", "draft", "verified"}

# 確度＝「誰が測ったか・利害があるか」。美術史の attested/scholarly をここに差し替えた。
#   measured     自分で測った数字（自社GA・売上・投稿インプレッション）
#   independent  利害のない第三者（官公庁統計・学術研究・査読論文）
#   attested     当事者の一次言明（仕様・規約・決算開示。自分に不利でも成り立つ事実）
#   vendor       その主張で儲かる側が出す市場の数字・効果の主張（ベンダーレポート・代理店調査）
#   anecdotal    事例・証言・個別の観測
#   hypothesis   自分の仮説（俯瞰の生成から除外する）
CERTAINTIES = {"measured", "independent", "attested", "vendor", "anecdotal", "hypothesis"}
# verified を名乗るのに使える確度。vendor と anecdotal だけでは verified にならない
VERIFIABLE_CERTAINTIES = {"measured", "independent", "attested"}

# stage → 再検証までの月数。emerging ほど早く腐る。dead は再検証しない（確定した過去）
RECHECK_MONTHS = {"emerging": 1, "growing": 3, "peak": 6, "declining": 6, "dead": None}

PREDICTION_OUTCOMES = {"hit", "miss", "unresolvable"}

# 構造的な関係（出典なしで書ける）
STRUCTURAL_RELATIONS = {
    "practiced_by": "practices", "example_of": "has_example", "part_of": "has_part",
    "precedes": "follows", "targets": "targeted_by", "documented_in": "documents",
    "operated_by": "operates",
}
# 解釈を含む関係（certainty と source を必須にする）
INTERPRETIVE_RELATIONS = {
    "responds_to": "answered_by", "enabled_by": "enabled", "killed_by": "killed",
    "derives_from": "derived_into", "substitutes": "substituted_by",
    "reacts_against": "reacted_against_by", "grouped_as": "groups",
    "diffused_to": "received", "influenced_by": "influenced",
}
RELATIONS = {**STRUCTURAL_RELATIONS, **INTERPRETIVE_RELATIONS}

# 空間軸に当たるのはチャネル。トレンドの「発生地」は物理座標ではなくチャネルとカテゴリ
CHANNEL_ROLES = {"originated_on", "spread_to", "commoditized_on", "observed_on"}

# 関係が指してよい相手の型。意味的に壊れた配線（killed_by が channel を指す等）を落とすため。
RELATION_TARGET_TYPES = {
    "practiced_by": {"player"}, "example_of": {"practice", "trend"},
    "precedes": {"trend", "practice", "event"}, "targets": {"concept"},
    "documented_in": {"source"}, "operated_by": {"player"},
    "responds_to": {"trend", "event"}, "enabled_by": {"event", "channel", "concept"},
    "killed_by": {"event"}, "derives_from": {"trend", "practice", "concept"},
    "substitutes": {"trend", "practice", "channel"},
    "reacts_against": {"trend", "practice", "concept"}, "grouped_as": {"trend"},
    "diffused_to": {"channel"},
    "influenced_by": None, "part_of": None,  # None = 型を限定しない
}

# verified を名乗るとき、項目ごとの根拠が要る field（evidence ブロック）
EVIDENCE_FIELDS_FOR_VERIFIED = {"trend": {"time", "kind", "stage"}, "practice": {"time"}}

URI_PREFIX = "urn:mtn:"

# --- EDTF（ISO 8601-2）Level 1 サブセット --------------------------------------
# 受ける形: 2024 / 2024-05 / 2024-05-20 / 202X（2020年代）/ 2024~（およそ）/ 2024?（不確か）
#          .. （開いた端）/ null（不明）
EDTF_RE = re.compile(r"^(?:\.\.|(\d{4}|\d{3}X|\d{2}XX|\dXXX)(?:-\d{2}(?:-\d{2})?)?[?~%]?)$")


def edtf_ok(value):
    return value is None or (isinstance(value, str) and bool(EDTF_RE.match(value)))


def edtf_year_range(value):
    """EDTF 値から (最小年, 最大年) を返す。開いた端・不明は None。ソートと集計に使う。"""
    if not value or value == "..":
        return (None, None)
    head = str(value).split("-")[0].rstrip("?~%")
    if "X" not in head:
        return (int(head), int(head))
    lo = int(head.replace("X", "0"))
    hi = int(head.replace("X", "9"))
    return (lo, hi)


# --- 鮮度 ----------------------------------------------------------------------

def recheck_deadline(stage, valid_as_of):
    """stage と確認日から再検証期限（ISO 日付文字列）を導出する。dead は None（再検証しない）。

    期限を書く側に計算させない——手で計算した期限は stage を変えたときに直し忘れる。
    """
    import datetime
    months = RECHECK_MONTHS.get(stage)
    if months is None or not valid_as_of:
        return None
    d = datetime.date.fromisoformat(str(valid_as_of))
    month = d.month - 1 + months
    year, month = d.year + month // 12, month % 12 + 1
    try:
        return datetime.date(year, month, d.day).isoformat()
    except ValueError:  # 月末の桁あふれ（1/31 + 1ヶ月）は月末に丸める
        import calendar
        return datetime.date(year, month, calendar.monthrange(year, month)[1]).isoformat()


def data_as_of(entities):
    """生成物の「いま」。時計を使わず、データの最新日（updated の最大値）を使う。

    時計を使うと生成物が走らせた日ごとに変わり、CI の「生成物が最新か」が時差だけで落ちる。
    データの最新日なら決定的で、エンティティを書き足すたびに前へ進む。生きた時計での鮮度は
    `audit.py --now` で見る（docs/freshness.md）。
    """
    return max((str(m.get("updated") or "") for m in entities.values()), default="")


# --- 読み込み -----------------------------------------------------------------

def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("frontmatter がない（先頭が --- で始まっていない）")
    _, block, body = text.split("---\n", 2)
    return yaml.safe_load(block) or {}, body


def load_config():
    return yaml.safe_load((CONFIG / "markets.yaml").read_text(encoding="utf-8"))


def load_entities():
    """{id: meta} と、id 順の (path, meta, body) を返す。検証はしない。"""
    entities, records = {}, []
    for path in sorted(ENTITIES.rglob("*.md")):
        meta, body = read_frontmatter(path)
        meta["path"] = str(path.relative_to(ROOT))
        records.append((path, meta, body))
        if meta.get("id"):
            entities[meta["id"]] = meta
    return entities, records


def edges_of(meta):
    """1エンティティの frontmatter から出るエッジを列挙する。"""
    out = []
    for r in meta.get("relations") or []:
        out.append({"from": meta.get("id"), "type": r.get("type"), "to": r.get("target"),
                    "certainty": r.get("certainty"), "source": r.get("source")})
    for c in meta.get("channels") or []:
        out.append({"from": meta.get("id"), "type": c.get("role"), "to": c.get("target")})
    return out


def build_edges(entities):
    """全エッジ＋逆向きの派生エッジ。target が alias（旧ID）なら実IDに解決してから積む——
    解決しないと、旧IDを指すエッジが graph・audit・bundle のどこからも実体に繋がらない。"""
    aliases = alias_map(entities)
    edges = []
    for meta in entities.values():
        for e in edges_of(meta):
            e["to"] = resolve(e["to"], entities, aliases)
            edges.append(e)
    derived = [
        {"from": e["to"], "type": RELATIONS[e["type"]], "to": e["from"], "derived": True}
        for e in edges if e["type"] in RELATIONS and e["to"] in entities
    ]
    return edges + derived


QUERY_LOG = ROOT / "data" / "queries.jsonl"


def log_query(term, hits):
    """検索を記録する。**該当なしこそ残す**——探されたのに無かった、という需要が消えないように。

    これが無いと系が一方通行になる（書く→読まれる→何も返らない）。記録した語は被覆マップに出て、
    次に何を埋めるかの判断材料になる。
    """
    import datetime, json
    QUERY_LOG.parent.mkdir(exist_ok=True)
    row = {"ts": datetime.datetime.now().isoformat(timespec="seconds"), "term": term, "hits": hits}
    with QUERY_LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_queries():
    import json
    if not QUERY_LOG.exists():
        return []
    return [json.loads(l) for l in QUERY_LOG.read_text(encoding="utf-8").splitlines() if l.strip()]


def search_entities(term, entities):
    """語で当たる id を返す（label と本文を見る）。bundle の --search と被覆マップで同じ結果を使う。"""
    hits = []
    needle = term.lower()
    for eid, meta in sorted(entities.items()):
        body = read_frontmatter(ROOT / meta["path"])[1]
        haystack = " ".join(str(meta.get(k) or "") for k in ("label_ja", "label_en", "id")) + body
        if needle in haystack.lower():
            hits.append(eid)
    return hits


def resolve(ref, entities, aliases):
    """id か alias を id に解決する。slug を変えても参照が切れないようにするため。"""
    return ref if ref in entities else aliases.get(ref, ref)


def alias_map(entities):
    out = {}
    for eid, meta in entities.items():
        for a in meta.get("aliases") or []:
            out[a] = eid
    return out
