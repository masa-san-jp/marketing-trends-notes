#!/usr/bin/env python3
"""境界へ出すための研究信号を書き出す（鮮度と利害を落とさない）。

    python3 tools/export_signals.py --purpose artistic-research
    python3 tools/export_signals.py --purpose artistic-research --entity trend/anxiety-multiplication
    python3 tools/export_signals.py --purpose artistic-research --limit 5 --output signals.json

親の `tools/adapters.py::adapt_marketing_signal` が受け取る境界DTOの形に合わせてある。

**このKBの一番の特徴は「事実が腐る」ことなので、鮮度をそのまま運ぶ。**
`freshness.recheck_by` を境界の `revalidate_at` へ、`valid_as_of` を `retrieved_at` へ写す。
recheck 期限を過ぎたものは `status: stale` として**落とさずに**出す——
cross-repository-contract が「staleは削除せず制約として伝播する」と定めているため。

**出典の利害も落とさない。** `evidence[].certainty` が `vendor` の項目を持つ信号は
`vendor_interest` を true にする。受け手が「売り手が言っていること」を区別できなくなるのを防ぐ。
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

try:
    from kb import ROOT, load_entities
except ModuleNotFoundError:  # tools.export_signals として読まれた場合
    from tools.kb import ROOT, load_entities

CONTRACT = "research-signal-export/v1"
ADAPTER_VERSION = "1.0.0"
SOURCE_REPOSITORY = "marketing-trends"

# このKBの certainty 語彙 → 境界の evidence kind
EVIDENCE_KIND = {
    "independent": "primary",
    "vendor": "secondary",
    "anecdotal": "anecdotal",
    "self-reported": "secondary",
}


def _head_commit() -> str:
    return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True, check=True).stdout.strip()


def _iso(dt: datetime) -> str:
    return dt.isoformat(timespec="seconds")


def _to_stamp(value: str | None, fallback: datetime) -> str:
    """`2026-11-10` や `2026-11` を境界のタイムスタンプへ。精度は落とさず日を補わない場合は月初に寄せる。"""
    if not value:
        return _iso(fallback)
    parts = str(value).split("-")
    try:
        year = int(parts[0])
        month = int(parts[1]) if len(parts) > 1 else 1
        day = int(parts[2]) if len(parts) > 2 else 1
        return _iso(datetime(year, month, day, tzinfo=timezone(timedelta(hours=9))))
    except (ValueError, IndexError):
        return _iso(fallback)


def _freshness_status(recheck_by: str | None, today: date) -> str:
    """recheck 期限を過ぎていれば stale。**落とさずに stale として運ぶ。**"""
    if not recheck_by:
        return "unknown"
    parts = str(recheck_by).split("-")
    try:
        year = int(parts[0])
        month = int(parts[1]) if len(parts) > 1 else 12
        day = int(parts[2]) if len(parts) > 2 else 28
        return "current" if date(year, month, day) >= today else "stale"
    except (ValueError, IndexError):
        return "unknown"


def build_record(meta: dict, commit: str, now: datetime, purpose: str) -> dict | None:
    """1つの trend を境界DTOへ変換する。出典が1本も無いものは出さない。"""
    evidence = meta.get("evidence") or []
    sources = meta.get("sources") or []
    if not sources:
        return None

    fresh = meta.get("freshness") or {}
    recheck_by = fresh.get("recheck_by")
    valid_as_of = fresh.get("valid_as_of")
    status = _freshness_status(recheck_by, now.date())
    revalidate_at = _to_stamp(recheck_by, now)

    vendor_interest = any(item.get("certainty") == "vendor" for item in evidence)
    kinds = {EVIDENCE_KIND.get(item.get("certainty"), "unknown") for item in evidence}
    evidence_kind = "primary" if "primary" in kinds else (sorted(kinds)[0] if kinds else "unknown")

    predictions = meta.get("predictions") or []
    unresolved = [p for p in predictions if p.get("resolved") in (None, False)]
    # 語彙は境界側が閉じている（none / pending / confirmed / refuted / unknown）。
    # 「答え合わせ前」は pending、当たり外れが付いたものは outcome を見て分ける。
    if not predictions:
        prediction_status = "none"
    elif unresolved:
        prediction_status = "pending"
    elif all(p.get("outcome") == "hit" for p in predictions):
        prediction_status = "confirmed"
    elif any(p.get("outcome") == "miss" for p in predictions):
        prediction_status = "refuted"
    else:
        prediction_status = "unknown"

    unknowns = []
    if status == "stale":
        unknowns.append(f"鮮度の再確認期限（{recheck_by}）を過ぎている。値が現在も有効かは未確認")
    if not evidence:
        unknowns.append("項目ごとの根拠（evidence）が無く、出典URLだけがある")
    if unresolved:
        unknowns.append(f"未解決の予測が {len(unresolved)} 件ある（答え合わせ前）")

    slug = meta["id"].split("/", 1)[1]
    return {
        "signal_id": f"marketing:{slug}",
        "repository": SOURCE_REPOSITORY,
        "commit": commit,
        "entity_id": meta["id"],
        "source_locator": meta["path"],
        "evidence_locator": f"{meta['path']}#evidence",
        "evidence_kind": evidence_kind,
        "statement": f"{meta.get('label_ja')}（{meta.get('label_en')}）は "
                     f"stage={meta.get('stage')} として記録されている",
        "certainty": {
            "level": "observed" if evidence_kind == "primary" else "inferred",
            "basis": f"evidence の certainty は {sorted({i.get('certainty') for i in evidence}) or '無し'}。"
                     f"vendor 由来を含むか: {vendor_interest}",
        },
        "unknowns": unknowns or ["このトレンドの未着手事項は本文にある"],
        "constraints": [
            f"{purpose} の目的内でのみ利用する",
            "stale を current として扱わない",
            "vendor 由来の主張を独立した検証済みの事実へ昇格させない",
        ],
        "validity": {"status": "valid" if status != "stale" else "expired",
                     "checked_at": _to_stamp(valid_as_of, now)},
        "freshness": {
            "status": status,
            "retrieved_at": _to_stamp(valid_as_of, now),
            "revalidate_at": revalidate_at,
        },
        "generated_at": _iso(now),
        "adapter_version": ADAPTER_VERSION,
        "stage": meta.get("stage") or "unknown",
        "revalidate_at": revalidate_at,
        "expires_at": revalidate_at,
        # 取得の「時刻」と「方法」を分けて持つ。certainty（利害）と混ぜない。
        "retrieved": {
            "at": _to_stamp(valid_as_of, now),
            "method": "direct" if evidence_kind == "primary" else "secondary",
        },
        "vendor_interest": "declared" if vendor_interest else "none",
        "counterevidence": [c for c in (meta.get("counterevidence") or [])],
        "prediction_status": prediction_status,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="境界へ出す研究信号を書き出す")
    ap.add_argument("--purpose", required=True)
    ap.add_argument("--entity", help="1件だけ出す（例: trend/anxiety-multiplication）")
    ap.add_argument("--limit", type=int, default=0, help="0 なら全件")
    ap.add_argument("--output", help="書き出し先。省略時は標準出力")
    args = ap.parse_args()

    loaded = load_entities()
    entities = loaded[0] if isinstance(loaded, tuple) else loaded
    commit = _head_commit()
    now = datetime.now(timezone(timedelta(hours=9))).replace(microsecond=0)

    if args.entity and args.entity not in entities:
        print(f"ERROR: そのIDは無い: {args.entity}", file=sys.stderr)
        return 1
    targets = [entities[args.entity]] if args.entity else [
        meta for meta in entities.values() if meta.get("type") == "trend"
    ]

    records = []
    for meta in sorted(targets, key=lambda m: m["id"]):
        record = build_record(meta, commit, now, args.purpose)
        if record:
            records.append(record)
        if args.limit and len(records) >= args.limit:
            break

    stale = sum(1 for r in records if r["freshness"]["status"] == "stale")
    payload = {
        "contract_version": CONTRACT,
        "source_repository": SOURCE_REPOSITORY,
        "source_commit": commit,
        "purpose": args.purpose,
        "generated_at": _iso(now),
        "signal_count": len(records),
        "stale_count": stale,
        "signals": records,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"{len(records)} 件を書き出した（うち鮮度切れ {stale} 件）-> {args.output}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
