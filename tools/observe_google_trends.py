#!/usr/bin/env python3
"""Capture and compare Japan's Google Trends Daily Search Trends RSS.

This records public search interest as a freshness-checkable proxy. It does
not collect SNS posts and must not be used to infer public sentiment.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any


DEFAULT_URL = "https://trends.google.com/trending/rss?geo=JP&hl=ja-JP&tz=540"
RSS_NAMESPACE = {"ht": "https://trends.google.com/trending/rss"}
USER_AGENT = "marketing-trends-notes/google-trends-observer/1.0"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Google Trends Japan RSSを取得し、前回スナップショットとの差分を保存する"
    )
    parser.add_argument("--output", type=Path, help="JSONスナップショットの保存先")
    parser.add_argument("--compare", type=Path, help="比較対象の前回JSONスナップショット")
    parser.add_argument("--limit", type=int, default=10, help="保存する上位件数（既定: 10）")
    parser.add_argument("--timeout", type=float, default=20, help="HTTPタイムアウト秒（既定: 20）")
    parser.add_argument("--url", default=DEFAULT_URL, help=argparse.SUPPRESS)
    parser.add_argument("--summary", action="store_true", help="JSONではなく要約を表示する")
    return parser.parse_args()


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        try:
            parsed = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def fetch_feed(url: str, timeout: float) -> tuple[bytes, dict[str, str]]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            headers = {
                "http_date": response.headers.get("Date", ""),
                "http_cache_control": response.headers.get("Cache-Control", ""),
            }
            return response.read(), headers
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code}: {exc.reason}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"接続失敗: {exc.reason}") from exc


def parse_items(xml_bytes: bytes, limit: int) -> list[dict[str, str]]:
    if limit < 1:
        raise ValueError("--limit は1以上で指定してください")
    root = ET.fromstring(xml_bytes)
    items = []
    for item in root.findall(".//item")[:limit]:
        items.append(
            {
                "title": item.findtext("title", default=""),
                "approx_traffic": item.findtext(
                    "ht:approx_traffic", default="", namespaces=RSS_NAMESPACE
                ),
                "pub_date": item.findtext("pubDate", default=""),
            }
        )
    return items


def compare_items(
    current: list[dict[str, str]],
    previous: dict[str, Any],
    current_retrieved_at: str,
) -> dict[str, Any]:
    current_titles = [item["title"] for item in current]
    previous_items = previous.get("items", [])
    previous_titles = [item.get("title", "") for item in previous_items]
    current_set = set(current_titles)
    previous_set = set(previous_titles)
    same = sorted(current_set & previous_set)
    previous_at = parse_datetime(previous.get("retrieved_at"))
    current_at = parse_datetime(current_retrieved_at)
    gap_minutes = None
    if previous_at and current_at:
        gap_minutes = round((current_at - previous_at).total_seconds() / 60)
    return {
        "compared_to": previous.get("source_file", "previous snapshot"),
        "retrieval_gap_minutes": gap_minutes,
        "current_item_count": len(current_titles),
        "previous_item_count": len(previous_titles),
        "same_item_count": len(same),
        "overlap_ratio": round(len(same) / max(len(current_set), len(previous_set), 1), 3),
        "entered": [title for title in current_titles if title not in previous_set],
        "exited": [title for title in previous_titles if title not in current_set],
    }


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    xml_bytes, headers = fetch_feed(args.url, args.timeout)
    items = parse_items(xml_bytes, args.limit)
    retrieved_at = now_iso()
    payload: dict[str, Any] = {
        "source_url": args.url,
        "retrieved_at": retrieved_at,
        "http_date": headers["http_date"],
        "http_cache_control": headers["http_cache_control"],
        "scope": "Japan / Daily Search Trends RSS",
        "items": items,
        "interpretation_status": "provisional_public_attention_proxy",
        "not_claimed": [
            "SNS上の会話量",
            "感情の方向",
            "社会全体の代表性",
            "検索からの原因確定",
        ],
    }
    if args.compare:
        previous = json.loads(args.compare.read_text(encoding="utf-8"))
        previous["source_file"] = str(args.compare)
        payload["comparison"] = compare_items(items, previous, retrieved_at)
    return payload


def write_or_print(payload: dict[str, Any], args: argparse.Namespace) -> None:
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    if args.summary:
        comparison = payload.get("comparison")
        print(f"取得時刻: {payload['retrieved_at']}")
        print(f"項目数: {len(payload['items'])}")
        if comparison:
            print(
                "比較: {same}/{total}件共通 / overlap={overlap} / 追加={entered} / 退出={exited}".format(
                    same=comparison["same_item_count"],
                    total=comparison["previous_item_count"],
                    overlap=comparison["overlap_ratio"],
                    entered=", ".join(comparison["entered"]) or "なし",
                    exited=", ".join(comparison["exited"]) or "なし",
                )
            )
        for index, item in enumerate(payload["items"], 1):
            print(f"{index}. {item['title']} | {item['approx_traffic']}")
    elif not args.output:
        print(rendered, end="")


def main() -> int:
    args = parse_args()
    try:
        payload = build_payload(args)
        write_or_print(payload, args)
    except (OSError, RuntimeError, ValueError, ET.ParseError, json.JSONDecodeError) as exc:
        print(f"取得失敗: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
