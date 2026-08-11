#!/usr/bin/env python3
"""Validate and summarize atmosphere observations without inferring public opinion."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILE = ROOT / "data" / "social-observations.jsonl"
PLATFORMS = {"x"}
ATTENTION = {"low", "medium", "high"}
PERSISTENCE = {"burst", "short", "persistent", "unknown"}
SPREAD = {"within_cluster", "cross_cluster", "cross_platform", "unknown"}
REQUIRED = {
    "id",
    "platform",
    "observed_window",
    "geo",
    "view",
    "query_scope",
    "sample",
    "signal",
    "interpretation",
    "scope",
    "sources",
    "observed_by",
}


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonnegative_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def parse_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def validate_url(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("https://")


def validate_record(record: Any, line_number: int, seen_ids: set[str]) -> list[str]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["JSONオブジェクトではありません"]

    missing = sorted(REQUIRED - record.keys())
    if missing:
        errors.append(f"必須フィールドがありません: {', '.join(missing)}")

    record_id = record.get("id")
    if not nonempty_string(record_id):
        errors.append("id は空でない文字列にしてください")
    elif record_id in seen_ids:
        errors.append(f"id が重複しています: {record_id}")
    else:
        seen_ids.add(record_id)

    if record.get("platform") not in PLATFORMS:
        errors.append("platform は現在 x のみ指定できます")

    window = record.get("observed_window")
    if not isinstance(window, dict):
        errors.append("observed_window はオブジェクトにしてください")
    else:
        start = parse_datetime(window.get("start"))
        end = parse_datetime(window.get("end"))
        if start is None:
            errors.append("observed_window.start はISO 8601日時にしてください")
        if end is None:
            errors.append("observed_window.end はISO 8601日時にしてください")
        if start is not None and end is not None and start > end:
            errors.append("observed_window.start は end 以前にしてください")

    for field in ("geo", "view", "query_scope", "interpretation", "observed_by"):
        if not nonempty_string(record.get(field)):
            errors.append(f"{field} は空でない文字列にしてください")

    sample = record.get("sample")
    if not isinstance(sample, dict):
        errors.append("sample はオブジェクトにしてください")
    else:
        posts = sample.get("posts_observed")
        accounts = sample.get("unique_accounts")
        if not nonnegative_integer(posts) or posts == 0:
            errors.append("sample.posts_observed は1以上の整数にしてください")
        if not nonnegative_integer(accounts):
            errors.append("sample.unique_accounts は0以上の整数にしてください")
        if isinstance(posts, int) and isinstance(accounts, int) and accounts > posts:
            errors.append("sample.unique_accounts は posts_observed 以下にしてください")
        for field in ("collection_method", "method_version"):
            if not nonempty_string(sample.get(field)):
                errors.append(f"sample.{field} は空でない文字列にしてください")

    signal = record.get("signal")
    if not isinstance(signal, dict):
        errors.append("signal はオブジェクトにしてください")
    else:
        if signal.get("attention") not in ATTENTION:
            errors.append("signal.attention は low / medium / high のいずれかにしてください")
        for field in ("affects", "hooks"):
            value = signal.get(field)
            if not isinstance(value, list) or not value or not all(nonempty_string(item) for item in value):
                errors.append(f"signal.{field} は空でない文字列の配列にしてください")
        if not nonempty_string(signal.get("cultural_form")):
            errors.append("signal.cultural_form は空でない文字列にしてください")
        if signal.get("persistence") not in PERSISTENCE:
            errors.append("signal.persistence の値が不正です")
        if signal.get("spread") not in SPREAD:
            errors.append("signal.spread の値が不正です")

    scope = record.get("scope")
    if not isinstance(scope, dict):
        errors.append("scope はオブジェクトにしてください")
    else:
        if scope.get("population_claim") is not False:
            errors.append("scope.population_claim は false に固定してください")
        notes = scope.get("bias_notes")
        if not isinstance(notes, list) or not notes or not all(nonempty_string(item) for item in notes):
            errors.append("scope.bias_notes は空でない文字列の配列にしてください")

    sources = record.get("sources")
    if not isinstance(sources, list) or not sources or not all(validate_url(item) for item in sources):
        errors.append("sources は1件以上のhttps URLの配列にしてください")

    examples = record.get("examples", [])
    if not isinstance(examples, list) or len(examples) > 5:
        errors.append("examples は最大5件の配列にしてください")
    else:
        for index, example in enumerate(examples, start=1):
            if not isinstance(example, dict):
                errors.append(f"examples[{index}] はオブジェクトにしてください")
                continue
            if set(example) - {"url", "role", "note"}:
                errors.append(f"examples[{index}] に転載用の未許可フィールドがあります")
            if not validate_url(example.get("url")):
                errors.append(f"examples[{index}].url はhttps URLにしてください")
            for field in ("role", "note"):
                if not nonempty_string(example.get(field)):
                    errors.append(f"examples[{index}].{field} は空でない文字列にしてください")

    return [f"line {line_number}: {error}" for error in errors]


def load_records(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    if not path.exists():
        return [], []

    records: list[dict[str, Any]] = []
    errors: list[str] = []
    seen_ids: set[str] = set()
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            record = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: JSONとして読めません: {exc.msg}")
            continue
        errors.extend(validate_record(record, line_number, seen_ids))
        if isinstance(record, dict):
            records.append(record)
    return records, errors


def print_summary(records: list[dict[str, Any]]) -> None:
    print(f"観測: {len(records)} 件")
    if not records:
        print("観測ログはまだありません。現在のトレンドを主張するデータではありません。")
        return
    for label, values in (
        ("platform", (record.get("platform") for record in records)),
        ("view", (record.get("view") for record in records)),
        ("attention", (record.get("signal", {}).get("attention") for record in records)),
    ):
        print(f"{label}: " + ", ".join(f"{key}={count}" for key, count in Counter(values).most_common()))
    affects = Counter(
        affect
        for record in records
        for affect in record.get("signal", {}).get("affects", [])
    )
    print("affects: " + ", ".join(f"{key}={count}" for key, count in affects.most_common()))


def main() -> int:
    parser = argparse.ArgumentParser(description="SNS空気感観測ログの検証・集計")
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE, help="JSONLファイル")
    parser.add_argument("--check", action="store_true", help="形式を検証する")
    parser.add_argument("--summary", action="store_true", help="検証後に集計を表示する")
    args = parser.parse_args()
    if not args.check and not args.summary:
        args.check = True

    records, errors = load_records(args.file)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if args.check:
        if args.file.exists():
            print(f"✓ {len(records)} 件: {args.file}")
        else:
            print("✓ 0 件（観測ログなし）")
    if args.summary:
        print_summary(records)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
