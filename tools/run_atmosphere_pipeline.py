#!/usr/bin/env python3
"""Run the local atmosphere-observation checks as one supervised pipeline.

The default mode is deterministic and does not access the network.  Google
Trends RSS collection is opt-in because it is an external observation, while
the X environment check remains non-blocking when no token is configured.

Examples:
    python3 tools/run_atmosphere_pipeline.py --dry-run --skip-rss
    python3 tools/run_atmosphere_pipeline.py --collect-rss \
        --output-dir /path/to/Agentic-Art-Output/marketing-atmosphere \
        --compare /path/to/previous.json --summary
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def now_local() -> datetime:
    return datetime.now().astimezone()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="空気感観測に必要なローカル検証と任意のRSS取得を一括実行する"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="検証だけを実行する（RSS取得・生成物更新なし）",
    )
    parser.add_argument(
        "--skip-rss",
        action="store_true",
        help="Google Trends RSSを実行しない（CI向け。既定でも未指定時はRSSを取得しない）",
    )
    parser.add_argument(
        "--collect-rss",
        action="store_true",
        help="Google Trends Japan RSSを取得する（ネットワークアクセス）",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="RSSスナップショットの保存先ディレクトリ（--collect-rssと併用）",
    )
    parser.add_argument(
        "--rss-output",
        type=Path,
        help="RSSスナップショットの保存先ファイル（--collect-rssと併用）",
    )
    parser.add_argument(
        "--compare",
        type=Path,
        help="RSS比較対象の前回スナップショット（--collect-rssと併用）",
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="パイプライン実行レポートJSONの保存先（指定時のみ書き込む）",
    )
    parser.add_argument(
        "--now",
        help="auditに渡す基準日（YYYY-MM-DD。既定はローカル日付）",
    )
    parser.add_argument(
        "--require-x-token",
        action="store_true",
        help="X_BEARER_TOKENを必須にする（通常は未設定でもスキップ）",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="RSS取得時に観測要約を表示する",
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> list[str]:
    errors: list[str] = []
    if args.dry_run and args.collect_rss:
        errors.append("--dry-run と --collect-rss は同時に指定できません")
    if args.skip_rss and args.collect_rss:
        errors.append("--skip-rss と --collect-rss は同時に指定できません")
    rss_options = (args.output_dir, args.rss_output, args.compare)
    if any(option is not None for option in rss_options) and not args.collect_rss:
        errors.append("--output-dir / --rss-output / --compare は --collect-rss と併用してください")
    if args.output_dir and args.rss_output:
        errors.append("--output-dir と --rss-output はどちらか一方だけ指定してください")
    if args.now:
        try:
            datetime.strptime(args.now, "%Y-%m-%d")
        except ValueError:
            errors.append("--now はYYYY-MM-DD形式で指定してください")
    if args.compare and not args.compare.is_file():
        errors.append(f"比較対象がありません: {args.compare}")
    return errors


def run_command(
    name: str,
    command: list[str],
    *,
    capture_stdout_for_status: bool = False,
) -> dict[str, Any]:
    print(f"\n[{name}]")
    print("$ " + " ".join(command))
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    status = "passed" if result.returncode == 0 else "failed"
    print(f"status: {status}")
    record = {
        "name": name,
        "status": status,
        "returncode": result.returncode,
        "command": command,
    }
    if capture_stdout_for_status:
        record["stdout"] = result.stdout
    return record


def rss_output_path(args: argparse.Namespace, started_at: datetime) -> Path | None:
    if args.rss_output:
        return args.rss_output
    if args.output_dir:
        stamp = started_at.strftime("%Y%m%d-%H%M%S%z")
        return args.output_dir / f"google-trends-rss-{stamp}.json"
    return None


def run_pipeline(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    started_at = now_local()
    audit_date = args.now or started_at.date().isoformat()
    checks: list[dict[str, Any]] = []

    checks.append(
        run_command(
            "graph validation",
            [PYTHON, "tools/build_graph.py", "--check"],
        )
    )
    checks.append(
        run_command(
            "social observation validation",
            [PYTHON, "tools/observe_social.py", "--check"],
        )
    )
    checks.append(
        run_command(
            "freshness audit",
            [PYTHON, "tools/audit.py", "--dry-run", "--now", audit_date],
        )
    )

    x_command = [PYTHON, "tools/check_x_env.py"]
    if args.require_x_token:
        x_command.append("--require-token")
    x_result = run_command(
        "X environment (non-blocking by default)",
        x_command,
        capture_stdout_for_status=True,
    )
    if x_result["status"] == "passed":
        x_result["status"] = (
            "skipped"
            if not args.require_x_token and "SKIP:" in x_result.get("stdout", "")
            else "passed"
        )
    x_result.pop("stdout", None)
    checks.append(x_result)

    rss_result: dict[str, Any]
    if args.collect_rss:
        output_path = rss_output_path(args, started_at)
        rss_command = [PYTHON, "tools/observe_google_trends.py"]
        if output_path:
            rss_command.extend(["--output", str(output_path)])
        if args.compare:
            rss_command.extend(["--compare", str(args.compare)])
        if args.summary or output_path:
            rss_command.append("--summary")
        rss_result = run_command("Google Trends RSS collection", rss_command)
        rss_result["output"] = str(output_path) if output_path else None
        rss_result["compare"] = str(args.compare) if args.compare else None
    else:
        reason = "dry-run/skip requested" if args.dry_run or args.skip_rss else "not requested"
        print(f"\n[Google Trends RSS collection]\nstatus: skipped ({reason})")
        rss_result = {
            "name": "Google Trends RSS collection",
            "status": "skipped",
            "reason": reason,
            "output": None,
            "compare": None,
        }
    checks.append(rss_result)

    finished_at = now_local()
    required_failures = [
        check["name"]
        for check in checks
        if check["status"] == "failed" and check["name"] != "X environment (non-blocking by default)"
    ]
    if args.require_x_token and x_result["status"] == "failed":
        required_failures.append(x_result["name"])

    report = {
        "pipeline": "atmosphere-observation",
        "started_at": started_at.isoformat(timespec="seconds"),
        "finished_at": finished_at.isoformat(timespec="seconds"),
        "dry_run": args.dry_run,
        "audit_date": audit_date,
        "checks": checks,
        "required_failures": required_failures,
        "status": "failed" if required_failures else "passed_with_gaps",
        "interpretation": {
            "x_without_token": "skipped_without_blocking" if x_result["status"] == "skipped" else "checked",
            "google_trends": "public_search_interest_proxy_only",
            "not_claimed": [
                "SNS上の会話量",
                "感情の方向",
                "社会全体の代表性",
                "検索からの原因確定",
            ],
        },
    }
    return report, 1 if required_failures else 0


def main() -> int:
    args = parse_args()
    errors = validate_args(args)
    if errors:
        for error in errors:
            print(f"エラー: {error}", file=sys.stderr)
        return 2

    report, exit_code = run_pipeline(args)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"実行レポート: {args.report}")
    print(f"\nPIPELINE: {report['status']}")
    if report["required_failures"]:
        print("失敗: " + ", ".join(report["required_failures"]), file=sys.stderr)
    else:
        print("X未設定はスキップ可能。RSS未取得時は公開検索関心の空白を残します。")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
