#!/usr/bin/env python3
"""agent-task の完了判定を読み取り専用で統合する。"""

from __future__ import annotations

import argparse
import datetime as dt
import filecmp
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate_agent_issue.py"
SCHEMA_VERSION = "agent-verify/v1"
CHECK_NAMES = (
    "issue-contract", "graph-and-acceptance", "regression-tests", "social-observation-schema",
    "strict-live-audit", "export-contract", "generated-artifacts", "worktree-preservation",
)


def check_result(name: str, required: bool, status: str, exit_code: int,
                summary: str) -> dict[str, Any]:
    return {
        "name": name,
        "required": required,
        "status": status,
        "exit_code": exit_code,
        "summary": summary,
    }


def run_command(name: str, command: list[str], *, cwd: Path = ROOT,
                env: dict[str, str] | None = None) -> tuple[dict[str, Any], str]:
    result = subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True, check=False)
    combined = "\n".join(part for part in (result.stdout.strip(), result.stderr.strip()) if part)
    lines = combined.splitlines()
    summary = " / ".join(lines[-3:]) if lines else "no output"
    row = check_result(name, True, "passed" if result.returncode == 0 else "failed",
                       result.returncode, summary)
    return row, result.stdout


def source_commit(root: Path = ROOT) -> str:
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root,
                            capture_output=True, text=True, check=False)
    if result.returncode != 0 or not result.stdout.strip():
        raise RuntimeError("source_commitを取得できません")
    return result.stdout.strip()


def snapshot_worktree(root: Path = ROOT, exclude: Path | None = None) -> dict[str, str]:
    excluded = {p.resolve() for p in (exclude,) if p is not None}
    ignored_dirs = {".git", ".venv", "__pycache__"}
    snapshot: dict[str, str] = {}
    for directory, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in ignored_dirs]
        base = Path(directory)
        for name in filenames:
            path = base / name
            if path.resolve() in excluded:
                continue
            relative = str(path.relative_to(root))
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            snapshot[relative] = digest
    return snapshot


def copy_ignore(_directory: str, names: list[str]) -> set[str]:
    return {name for name in names if name in {".git", ".venv", "__pycache__"}}


def generated_artifacts_check(root: Path = ROOT) -> tuple[int, str]:
    files = [
        Path("data/graph.json"), Path("data/coverage.json"),
        Path("data/audit.json"), Path("overviews/coverage.md"),
    ]
    with tempfile.TemporaryDirectory(prefix="agent-verify-") as directory:
        temporary = Path(directory) / "repo"
        shutil.copytree(root, temporary, ignore=copy_ignore)
        build = subprocess.run([sys.executable, "tools/build_graph.py"], cwd=temporary,
                               capture_output=True, text=True, check=False)
        if build.returncode != 0:
            return 2, "temporary build_graph failed: " + (build.stderr.strip() or build.stdout.strip())
        audit = subprocess.run([sys.executable, "tools/audit.py"], cwd=temporary,
                               capture_output=True, text=True, check=False)
        if audit.returncode != 0:
            return 2, "temporary audit failed: " + (audit.stderr.strip() or audit.stdout.strip())
        mismatches = []
        for relative in files:
            current = root / relative
            regenerated = temporary / relative
            if not current.is_file():
                mismatches.append(f"missing:{relative}")
            elif not regenerated.is_file() or not filecmp.cmp(current, regenerated, shallow=False):
                mismatches.append(str(relative))
        if mismatches:
            return 2, "generated artifacts are stale: " + ", ".join(mismatches)
    return 0, "generated artifacts match a clean temporary regeneration"


def validate_export_payload(raw: str) -> tuple[int, str]:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        return 2, f"export JSON is invalid: {exc}"
    required = {"contract_version", "source_repository", "purpose", "signal_count", "signals",
                "stale_count", "generated_at", "source_commit"}
    missing = sorted(required - set(payload))
    if missing:
        return 2, "export fields missing: " + ", ".join(missing)
    if payload["contract_version"] != "research-signal-export/v1":
        return 2, "unexpected export contract_version"
    if payload["source_repository"] != "marketing-trends" or payload["purpose"] != "artistic-research":
        return 2, "unexpected export source or purpose"
    signals = payload["signals"]
    if payload["signal_count"] != len(signals):
        return 2, "signal_count does not match signals length"
    if any(signal.get("evidence_kind") == "unknown" for signal in signals):
        return 2, "export contains unknown evidence_kind"
    return 0, f"research-signal-export/v1: {payload['signal_count']} signals, stale_count={payload['stale_count']}"


def parse_now(value: str | None) -> str:
    if not value:
        raise ValueError("--now は必須です")
    try:
        parsed = dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("--now はYYYY-MM-DD形式で指定してください") from exc
    return parsed.isoformat()


def issue_command(args: argparse.Namespace) -> list[str]:
    if args.issue_body:
        return [sys.executable, str(VALIDATOR), "--body-file", str(args.issue_body), "--json"]
    command = [sys.executable, str(VALIDATOR), "--issue", str(args.issue), "--json"]
    if args.repo:
        command.extend(["--repo", args.repo])
    return command


def build_report(args: argparse.Namespace, *, root: Path = ROOT) -> dict[str, Any]:
    now = parse_now(args.now)
    before = snapshot_worktree(root, args.output)
    checks: list[dict[str, Any]] = []

    issue, _ = run_command("issue-contract", issue_command(args), cwd=root)
    checks.append(issue)
    graph, _ = run_command("graph-and-acceptance", [sys.executable, "tools/build_graph.py", "--check"], cwd=root)
    checks.append(graph)

    regression_env = os.environ.copy()
    regression_env["AGENT_VERIFY_REGRESSION"] = "1"
    regression, _ = run_command(
        "regression-tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=root, env=regression_env,
    )
    checks.append(regression)
    social, _ = run_command("social-observation-schema",
                            [sys.executable, "tools/observe_social.py", "--check"], cwd=root)
    checks.append(social)
    audit, _ = run_command(
        "strict-live-audit",
        [sys.executable, "tools/audit.py", "--dry-run", "--now", now, "--fail-on-findings"],
        cwd=root,
    )
    checks.append(audit)

    export, export_stdout = run_command(
        "export-contract", [sys.executable, "tools/export_signals.py", "--purpose", "artistic-research"], cwd=root
    )
    if export["status"] == "passed":
        export_code, export_summary = validate_export_payload(export_stdout)
        export["exit_code"] = export_code
        export["status"] = "passed" if export_code == 0 else "failed"
        export["summary"] = export_summary
    checks.append(export)

    generated_code, generated_summary = generated_artifacts_check(root)
    checks.append(check_result("generated-artifacts", True,
                               "passed" if generated_code == 0 else "failed",
                               generated_code, generated_summary))

    after = snapshot_worktree(root, args.output)
    preserved = before == after
    checks.append(check_result("worktree-preservation", True, "passed" if preserved else "failed",
                               0 if preserved else 2,
                               "作業ツリーは不変です" if preserved else "verifier実行前後でファイル内容が変化しました"))
    failed = [row["name"] for row in checks if row["required"] and row["status"] != "passed"]
    return {
        "schema_version": SCHEMA_VERSION,
        "issue": args.issue if args.issue is not None else str(args.issue_body),
        "source_commit": source_commit(root),
        "now": now,
        "status": "failed" if failed else "passed",
        "checks": checks,
    }


def emit_error(message: str, as_json: bool) -> None:
    payload = {"schema_version": SCHEMA_VERSION, "status": "failed", "error": message}
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"agent-verify: failed — {message}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="読み取り専用の統合agent verifier")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--issue", type=int)
    source.add_argument("--issue-body", type=Path)
    parser.add_argument("--repo")
    parser.add_argument("--now")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=Path)
    try:
        args = parser.parse_args(argv)
        if args.issue_body and not args.issue_body.is_file():
            raise ValueError(f"issue body がありません: {args.issue_body}")
        report = build_report(args)
    except (OSError, RuntimeError, ValueError) as exc:
        emit_error(str(exc), "--json" in (argv or sys.argv))
        return 3
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    if args.json:
        print(encoded, end="")
    else:
        print(f"agent-verify: {report['status']}")
        for row in report["checks"]:
            print(f"- {row['status']}: {row['name']} — {row['summary']}")
    return 0 if report["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
