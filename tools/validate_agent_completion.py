#!/usr/bin/env python3
"""PR、issue、agent-verify report の完了契約を検証する。"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from validate_agent_issue import COMPLETION_PENDING_MARKER, validate_body


SCHEMA_VERSION = "agent-completion-validation/v1"
MANUAL_COMPLETION_MARKER = "<!-- agent-manual-completion:v1 -->"
BOOTSTRAP_MIGRATION_ISSUES = {79, 80, 81, 82, 83, 84}
PR_SECTIONS = ("実装した要件", "完了条件", "検証結果", "変更対象外")
HEADING_RE = re.compile(r"^#{2,3}\s+(.+?)\s*$")
CLOSE_RE = re.compile(r"(?im)^\s*closes\s+#(\d+)\b")
PR_URL_RE = re.compile(r"https://github\.com/[^/\s]+/[^/\s]+/pull/\d+")
COMMIT_RE = re.compile(r"\b[0-9a-f]{7,40}\b", re.IGNORECASE)
ACTION_URL_RE = re.compile(r"https://github\.com/[^/\s]+/[^/\s]+/actions/runs/\d+")
REQUIRED_CHECKS = {
    "issue-contract", "graph-and-acceptance", "regression-tests", "social-observation-schema",
    "strict-live-audit", "export-contract", "generated-artifacts", "worktree-preservation",
}


def violation(code: str, message: str, section: str | None = None) -> dict[str, str]:
    row = {"code": code, "message": message}
    if section:
        row["section"] = section
    return row


def sections(body: str, names: tuple[str, ...]) -> dict[str, str]:
    headings: list[tuple[str, int]] = []
    for index, line in enumerate(body.splitlines()):
        match = HEADING_RE.match(line)
        if match and match.group(1) in names:
            headings.append((match.group(1), index))
    lines = body.splitlines()
    result: dict[str, str] = {}
    for index, (name, start) in enumerate(headings):
        end = headings[index + 1][1] if index + 1 < len(headings) else len(lines)
        result[name] = "\n".join(lines[start + 1:end]).strip()
    return result


def validate_pr_body(body: str) -> tuple[list[dict[str, str]], list[int]]:
    violations: list[dict[str, str]] = []
    closing = [int(value) for value in CLOSE_RE.findall(body)]
    if len(closing) != 1:
        violations.append(violation("closing-issue-count", "PR本文の `Closes #N` はちょうど1件必要です"))
    parsed = sections(body, PR_SECTIONS)
    for name in PR_SECTIONS:
        if not parsed.get(name):
            violations.append(violation("missing-pr-section", f"PR必須節がありません: {name}", name))
    verification = parsed.get("検証結果", "")
    if "agent-verify/v1" not in verification or "status=passed" not in verification:
        violations.append(violation("pr-verifier-evidence", "PRの検証結果にagent-verify/v1とstatus=passedが必要です", "検証結果"))
    return violations, closing


def validate_issue_body(body: str, *, require_merged_evidence: bool = False,
                        expected_issue: int | None = None) -> list[dict[str, str]]:
    result = validate_body(body)
    violations = list(result["violations"])
    if not result.get("completion_pending"):
        violations.append(violation("completion-marker", "完了待ちmarkerがありません"))
    completion = sections(body, ("完了条件",)).get("完了条件", "")
    checkboxes = re.findall(r"^\s*-\s+\[[ xX]\]\s+.+$", completion, flags=re.MULTILINE)
    if not checkboxes:
        violations.append(violation("completion-checkbox", "完了条件checkboxがありません", "完了条件"))
    if re.search(r"^\s*-\s+\[ \]\s+", completion, flags=re.MULTILINE):
        violations.append(violation("unchecked-completion", "未チェックの完了条件があります", "完了条件"))
    evidence = sections(body, ("完了証跡",)).get("完了証跡", "")
    manual_completion = MANUAL_COMPLETION_MARKER in body
    if manual_completion and expected_issue not in BOOTSTRAP_MIGRATION_ISSUES:
        violations.append(violation("manual-completion-scope", "manual completion markerはbootstrap issueだけで使用できます"))
    # Current owner instructions permit local-only operation without enabling Actions.
    # The supplied agent-verify report is still independently checked below.
    local_verification = re.search(
        r"(?m)^- Local verification: `[^`\n]*(?:agent_verify|agent-verify)[^`\n]*`; exit_code=0; report=`[^`\n]+`\s*$",
        evidence,
    )
    required_evidence = [
        ("verify-contract", "agent-verify/v1" in evidence and "status=passed" in evidence),
        ("actions-run-url", ACTION_URL_RE.search(evidence) or local_verification),
    ]
    if manual_completion:
        required_evidence.append(("direct-commit", COMMIT_RE.search(evidence)))
    else:
        required_evidence.append(("merged-pr-url", PR_URL_RE.search(evidence)))
        if require_merged_evidence:
            required_evidence.append(("merge-commit", COMMIT_RE.search(evidence)))
    for code, present in required_evidence:
        if not present:
            violations.append(violation(code, f"完了証跡に必要な情報がありません: {code}", "完了証跡"))
    return violations


def validate_report(payload: dict[str, Any], *, expected_source_commit: str | None = None) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    if payload.get("schema_version") != "agent-verify/v1":
        violations.append(violation("verify-schema", "agent-verify/v1 report が必要です"))
    if payload.get("status") != "passed":
        violations.append(violation("verify-status", "agent-verify report のstatusはpassedである必要があります"))
    checks = payload.get("checks")
    if not isinstance(checks, list) or not checks:
        violations.append(violation("verify-checks", "agent-verify report のchecksがありません"))
    elif not all(isinstance(row, dict) for row in checks):
        violations.append(violation("verify-checks", "agent-verify report のchecks要素がobjectではありません"))
    else:
        failed = [row.get("name") for row in checks if row.get("required") and row.get("status") != "passed"]
        if failed:
            violations.append(violation("verify-required-failure", "required checkが失敗しています: " + ", ".join(failed)))
        names = {row.get("name") for row in checks if row.get("required")}
        missing = sorted(REQUIRED_CHECKS - names)
        if missing:
            violations.append(violation("verify-checks-incomplete", "required checkが不足しています: " + ", ".join(missing)))
    if not payload.get("source_commit"):
        violations.append(violation("verify-source-commit", "source_commitがありません"))
    if expected_source_commit and payload.get("source_commit") != expected_source_commit:
        violations.append(violation("verify-source-mismatch", "verifier reportのsource_commitがmerge commitと一致しません"))
    return violations


def validate(pr_body: str, issue_body: str, report: dict[str, Any], expected_issue: int | None = None,
             pr_metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    manual_completion = MANUAL_COMPLETION_MARKER in issue_body
    if manual_completion and not pr_body.strip():
        violations, closing = [], []
    else:
        violations, closing = validate_pr_body(pr_body)
    violations.extend(validate_issue_body(
        issue_body,
        require_merged_evidence=pr_metadata is not None,
        expected_issue=expected_issue,
    ))
    expected_source_commit = None
    if pr_metadata:
        merge_commit = pr_metadata.get("mergeCommit")
        if isinstance(merge_commit, dict):
            expected_source_commit = merge_commit.get("oid")
    violations.extend(validate_report(report, expected_source_commit=expected_source_commit))
    if pr_metadata is not None and not (manual_completion and not pr_metadata):
        if pr_metadata.get("state") != "MERGED" or not pr_metadata.get("mergedAt"):
            violations.append(violation("pr-not-merged", "完了証跡のPRがMergedではありません"))
    if expected_issue is not None and closing and closing != [expected_issue]:
        violations.append(violation("closing-issue-mismatch", f"PRが閉じるissueが #{expected_issue} と一致しません"))
    return {"schema_version": SCHEMA_VERSION, "valid": not violations, "closing_issues": closing, "violations": violations}


def fetch_json(command: list[str]) -> dict[str, Any]:
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "GitHub取得に失敗しました")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"GitHub responseがJSONではありません: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="PR/issue/verify report completion validator", exit_on_error=False)
    pr_group = parser.add_mutually_exclusive_group(required=True)
    pr_group.add_argument("--pr-body", type=Path)
    pr_group.add_argument("--pr", type=int)
    issue_group = parser.add_mutually_exclusive_group(required=True)
    issue_group.add_argument("--issue-body", type=Path)
    issue_group.add_argument("--issue", type=int)
    parser.add_argument("--expected-issue", type=int,
                        help="入力本文を使う場合に、Closes #N の期待値を指定する")
    parser.add_argument("--verify-report", type=Path, required=True)
    parser.add_argument("--pr-metadata", type=Path)
    parser.add_argument("--repo")
    parser.add_argument("--json", action="store_true")
    json_requested = "--json" in (argv or sys.argv)
    try:
        args = parser.parse_args(argv)
        if args.pr_body:
            pr_body = args.pr_body.read_text(encoding="utf-8")
        else:
            command = ["gh", "pr", "view", str(args.pr), "--json", "body"]
            if args.repo:
                command.extend(["--repo", args.repo])
            pr_body = fetch_json(command).get("body") or ""
        if args.issue_body:
            issue_body = args.issue_body.read_text(encoding="utf-8")
        else:
            command = ["gh", "issue", "view", str(args.issue), "--json", "body"]
            if args.repo:
                command.extend(["--repo", args.repo])
            issue_body = fetch_json(command).get("body") or ""
        report = json.loads(args.verify_report.read_text(encoding="utf-8"))
        metadata = json.loads(args.pr_metadata.read_text(encoding="utf-8")) if args.pr_metadata else None
        expected_issue = args.expected_issue if args.expected_issue is not None else args.issue
        result = validate(pr_body, issue_body, report, expected_issue, metadata)
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        payload = {"schema_version": SCHEMA_VERSION, "valid": False, "violations": [], "error": str(exc)}
        if json_requested:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"検証不能: {exc}", file=sys.stderr)
        return 3
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("agent-completion/v1: " + ("valid" if result["valid"] else "invalid"))
        for row in result["violations"]:
            print(f"- {row['code']}: {row['message']}")
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
