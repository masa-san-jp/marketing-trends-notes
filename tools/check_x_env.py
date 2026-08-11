#!/usr/bin/env python3
"""Check local X API settings without printing credential values."""

from __future__ import annotations

import argparse
import os
import re
import stat
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_FILE = ROOT / ".env"
KNOWN_KEYS = {"X_BEARER_TOKEN", "X_API_BASE_URL", "X_API_TIMEOUT_SECONDS"}
KEY_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]*$")
PLACEHOLDER_VALUES = {"", "changeme", "replace_me", "your_token_here", "your-bearer-token"}


def parse_dotenv(path: Path) -> tuple[dict[str, str], list[str]]:
    values: dict[str, str] = {}
    errors: list[str] = []
    if not path.exists():
        return values, errors

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            errors.append(f".env {line_number}行目: KEY=VALUE形式ではありません")
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not KEY_PATTERN.fullmatch(key):
            errors.append(f".env {line_number}行目: キー名が不正です")
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        if key in KNOWN_KEYS:
            values[key] = value
    return values, errors


def merged_settings(path: Path) -> tuple[dict[str, str], list[str]]:
    file_values, errors = parse_dotenv(path)
    values = dict(file_values)
    for key in KNOWN_KEYS:
        if key in os.environ:
            values[key] = os.environ[key]
    return values, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="ローカルX API環境の確認（秘密値は表示しません）")
    parser.add_argument("--file", type=Path, default=DEFAULT_ENV_FILE, help="読み込む.envファイル")
    parser.add_argument("--require-token", action="store_true", help="Bearer Tokenを必須にする")
    parser.add_argument("--strict-permissions", action="store_true", help=".envが自分以外から読める場合に失敗する")
    args = parser.parse_args()

    values, errors = merged_settings(args.file)
    warnings: list[str] = []
    token = values.get("X_BEARER_TOKEN", "").strip()
    if not token or token.lower() in PLACEHOLDER_VALUES or token.startswith("<"):
        if args.require_token:
            errors.append("X_BEARER_TOKEN が未設定です（値は出力しません）")
        else:
            warnings.append("X_BEARER_TOKEN は未設定です")
    else:
        print("X_BEARER_TOKEN: 設定済み（値は非表示）")

    base_url = values.get("X_API_BASE_URL", "https://api.x.com").strip()
    parsed_url = urlparse(base_url)
    if parsed_url.scheme != "https" or not parsed_url.netloc:
        errors.append("X_API_BASE_URL はhttps URLにしてください")
    else:
        print(f"X_API_BASE_URL: {base_url}")

    timeout = values.get("X_API_TIMEOUT_SECONDS", "30").strip()
    try:
        timeout_value = float(timeout)
        if timeout_value <= 0:
            raise ValueError
    except ValueError:
        errors.append("X_API_TIMEOUT_SECONDS は0より大きい数値にしてください")
    else:
        print(f"X_API_TIMEOUT_SECONDS: {timeout_value:g}秒")

    if args.file.exists() and os.name != "nt":
        mode = stat.S_IMODE(args.file.stat().st_mode)
        if mode & 0o077:
            message = ".env が自分以外から読める権限です。chmod 600 .env を実行してください"
            if args.strict_permissions:
                errors.append(message)
            else:
                warnings.append(message)

    for warning in warnings:
        print(f"警告: {warning}", file=sys.stderr)
    if errors:
        for error in errors:
            print(f"エラー: {error}", file=sys.stderr)
        return 1
    print("✓ ローカルX API環境の形式は確認できました（API通信は未実行）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
