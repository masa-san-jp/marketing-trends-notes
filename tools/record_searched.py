#!/usr/bin/env python3
"""「調査したが、載せるに足る trend が無かった」を1行残す。

被覆マップの空欄には2つの意味がある——まだ手が届いていないのか、調べた上で無かったのか。
区別しないと、調べ終わったところを何度も調べ直し、手つかずのところは手つかずのまま残る。

使い方:

    python3 tools/record_searched.py --market gaming --geo japan \
        --scope "2024年以降の国内ゲーム市場の需要側の変化" \
        --source https://... --source https://...

`--source` は「何に当たったか」。0本でも記録はできるが、**0本の記録は調査ではない**ので
`--scope` に何をどう探したかを書く。
"""
import argparse
import datetime
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kb import SEARCHED_LOG, load_config


def main():
    cfg = load_config()
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--market", required=True, choices=sorted(cfg["categories"]))
    p.add_argument("--geo", choices=sorted(cfg["geographies"]))
    p.add_argument("--scope", required=True, help="何を、どの範囲で探したか（1行）")
    p.add_argument("--source", action="append", default=[], help="当たった出典URL（複数可）")
    p.add_argument("--by", default="aiko-pr")
    p.add_argument("--at", help="調査日 YYYY-MM-DD（既定は今日）")
    args = p.parse_args()

    row = {
        "at": args.at or datetime.date.today().isoformat(),
        "market": args.market,
        "geo": args.geo,
        "scope": args.scope,
        "sources": args.source,
        "by": args.by,
    }
    SEARCHED_LOG.parent.mkdir(exist_ok=True)
    with SEARCHED_LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"記録した: {row['market']} — {row['scope']}")
    print("被覆マップに反映するには python3 tools/build_graph.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
