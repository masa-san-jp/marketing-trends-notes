#!/usr/bin/env python3
"""必須項目が埋まった雛形を作る。調査する側が「何を書くか」を思い出さなくて済むようにするため。

    python3 tools/new_entity.py trend short-video-mainstream --ja ショート動画の主流化
    python3 tools/new_entity.py practice retail-media --ja リテールメディア広告
    python3 tools/new_entity.py channel tiktok --ja TikTok --en TikTok

TODO: が1つでも残っていると build_graph.py が落ちる（必須項目が空だから）。埋めれば通る。
trend の freshness.recheck_by は空のままでよい——`--stage` を渡せばここで計算して埋める。
埋め方が分からなくなったら docs/investigation-task.md（手順と判定表）。
"""

import argparse
import sys
from datetime import date

from kb import (DIR_FOR_TYPE, ENTITIES, SATURATIONS, STAGES, TREND_KINDS, URI_PREFIX,
                recheck_deadline)

COMMON = """---
id: {eid}
uri: {uri}
type: {etype}
label_ja: {ja}
label_en: {en}
authority:
  wikidata: null
  none_reason: null      # 典拠が1つも無いときだけ「何を検索して無かったか」を書く
time:
  start: null            # EDTF: 2016 / 202X（2020年代）/ 2020~（およそ）/ null
  end: null              # 継続中は ".."
  display: null          # 原表記（「コロナ禍以降」等）をそのまま残す
{extra}channels: []            # 例 [{{role: originated_on, target: channel/tiktok}}]
relations: []
sources:
  - TODO: 出典URLを1本以上
status: stub
updated: {today}
---

# {ja}

TODO: 本文。型ごとの見出しは docs/schema.md の「本文の型」に従う。
"""

TREND_EXTRA = """kind: {kind}             # {kinds}
stage: {stage}           # {stages}
market: TODO             # config/markets.yaml の categories から1つ
geo: TODO                # config/markets.yaml の geographies から1つ
naming:
  self_identified: TODO  # 当事者（消費者・実践者）がこの名を使うか（true / false）
  named_by: null         # 名付けたのは誰か（player の id。不明なら null にして note に経緯）
  named_when: null       # EDTF
  original_label: {ja}
  note: null
freshness:
  valid_as_of: {today}   # 最後に実データで確認した日
  recheck_by: {recheck}  # stage から自動導出。stage を変えたら build_graph が再計算を要求する
evidence: []             # [{{field, source, certainty, as_of, retrieved}}]
                         # verified には time / kind / stage の根拠と、retrieved: primary が1本要る
predictions: []          # 任意 [{{claim: ..., by: EDTF, resolved: null, outcome: null}}]
"""

PRACTICE_EXTRA = """saturation: null        # 任意: {sats}
evidence: []             # [{{field, source, certainty, as_of, retrieved}}]
"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("type", choices=sorted(DIR_FOR_TYPE))
    p.add_argument("slug")
    p.add_argument("--ja", required=True)
    p.add_argument("--en", default="null")
    p.add_argument("--kind", choices=sorted(TREND_KINDS), help="trend のとき。省略すると TODO")
    p.add_argument("--stage", choices=sorted(STAGES), help="trend のとき。省略すると TODO")
    a = p.parse_args()

    today = date.today().isoformat()
    extra = ""
    if a.type == "trend":
        recheck = recheck_deadline(a.stage, today) if a.stage else None
        extra = TREND_EXTRA.format(
            kind=a.kind or "TODO", kinds=" / ".join(sorted(TREND_KINDS)),
            stage=a.stage or "TODO", stages=" / ".join(sorted(STAGES)),
            ja=a.ja, today=today, recheck=recheck or "null")
    if a.type == "practice":
        extra = PRACTICE_EXTRA.format(sats=" / ".join(sorted(SATURATIONS)))

    eid = f"{a.type}/{a.slug}"
    path = ENTITIES / DIR_FOR_TYPE[a.type] / f"{a.slug}.md"
    if path.exists():
        print(f"✗ もうある: {path}", file=sys.stderr)
        return 1
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(COMMON.format(eid=eid, uri=URI_PREFIX + eid, etype=a.type, ja=a.ja, en=a.en,
                                  extra=extra, today=today), encoding="utf-8")
    print(f"✓ {path.relative_to(path.parents[2])} を作った。TODO を埋めて "
          f"`python3 tools/build_graph.py --check` を通す")
    return 0


if __name__ == "__main__":
    sys.exit(main())
