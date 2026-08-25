#!/usr/bin/env python3
"""agent-task/v1 の issue 本文を決定的に検証する。"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "agent-task-validation/v1"
CONTRACT = "Contract: agent-task/v1"
SECTIONS = (
    "目的", "現状", "スコープ", "非スコープ", "実装要件", "変更対象",
    "完了条件", "検証コマンド", "完了証跡", "依存関係",
)
HEADING_RE = re.compile(r"^#{2,3}\s+(.+?)\s*$")
CHECKBOX_RE = re.compile(r"^\s*-\s+\[[ xX]\]\s+(.+?)\s*$", re.MULTILINE)
UNCHECKED_RE = re.compile(r"^\s*-\s+\[ \]\s+(.+?)\s*$", re.MULTILINE)
ISSUE_REF_RE = re.compile(r"^\s*-\s+(?:#\d+|https://github\.com/[^/\s]+/[^/\s]+/issues/\d+)(?:\s+.*)?\s*$")
FORBIDDEN_PLACEHOLDER_RE = re.compile(r"TODO|TBD|後で決める|ここに記入|記入してください", re.IGNORECASE)


def violation(code: str, message: str, section: str | None = None) -> dict[str, str]:
    row = {"code": code, "message": message}
    if section:
        row["section"] = section
    return row


def without_code_spans(body: str) -> str:
    """契約語や禁止語を説明する inline/fenced code の中身は本文値として判定しない。"""
    without_fences = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    return re.sub(r"`[^`\n]*`", "", without_fences)


def section_map(body: str, violations: list[dict[str, str]]) -> dict[str, str]:
    headings: list[tuple[str, int]] = []
    for index, line in enumerate(body.splitlines()):
        match = HEADING_RE.match(line)
        if match and match.group(1) in SECTIONS:
            headings.append((match.group(1), index))

    positions: dict[str, list[int]] = {name: [] for name in SECTIONS}
    for name, index in headings:
        positions[name].append(index)
    for name in SECTIONS:
        if not positions[name]:
            violations.append(violation("missing-section", f"必須節がありません: {name}", name))
        elif len(positions[name]) > 1:
            violations.append(violation("duplicate-section", f"必須節が重複しています: {name}", name))

    order = [index for name, index in headings if name in SECTIONS]
    expected_order = [SECTIONS.index(name) for name, _ in headings if name in SECTIONS]
    if len(order) == len(SECTIONS) and expected_order != sorted(expected_order):
        violations.append(violation("section-order", "必須節の順序が契約と異なります"))

    result: dict[str, str] = {}
    lines = body.splitlines()
    for offset, (name, start) in enumerate(headings):
        if name not in SECTIONS or positions[name][0] != start:
            continue
        end = headings[offset + 1][1] if offset + 1 < len(headings) else len(lines)
        result[name] = "\n".join(lines[start + 1:end]).strip()
    return result


def validate_body(body: str, *, labels: list[str] | None = None, state: str | None = None) -> dict[str, Any]:
    violations: list[dict[str, str]] = []
    semantic_body = without_code_spans(body)
    if semantic_body.count(CONTRACT) != 1:
        violations.append(violation("contract-marker", f"{CONTRACT!r} は本文に1回だけ必要です"))
    if FORBIDDEN_PLACEHOLDER_RE.search(semantic_body):
        violations.append(violation("placeholder", "テンプレート未確定語（TODO/TBD/後で決める等）が残っています"))
    sections = section_map(body, violations)
    for name in SECTIONS:
        content = sections.get(name, "")
        if not content:
            violations.append(violation("empty-section", f"必須節が空です: {name}", name))

    completion = sections.get("完了条件", "")
    completion_items = CHECKBOX_RE.findall(completion)
    unchecked_items = UNCHECKED_RE.findall(completion)
    if not completion_items:
        violations.append(violation("completion-checkbox", "完了条件に checkbox が1件以上必要です", "完了条件"))
    if not unchecked_items:
        violations.append(violation("open-completion-checkbox", "起票時点では未チェックの完了条件が1件以上必要です", "完了条件"))
    for item in completion_items:
        if len(item.strip()) < 8 or re.fullmatch(r"対応する|改善する|よくする", item.strip()):
            violations.append(violation("unobservable-completion", f"観測可能でない完了条件です: {item}", "完了条件"))

    verification = sections.get("検証コマンド", "")
    bash_blocks = re.findall(r"```bash\s*\n(.*?)```", verification, flags=re.DOTALL | re.IGNORECASE)
    commands = []
    for block in bash_blocks:
        commands.extend(line.strip() for line in block.splitlines()
                        if line.strip() and not line.strip().startswith("#"))
    if not bash_blocks or not commands:
        violations.append(violation("verification-command", "検証コマンドに bash block と実行コマンドが必要です", "検証コマンド"))
    dependencies = sections.get("依存関係", "")
    dependency_lines = [line.strip() for line in dependencies.splitlines() if line.strip()]
    if dependency_lines and not dependency_lines[0].startswith("なし"):
        invalid = [line for line in dependency_lines if not ISSUE_REF_RE.match(line)]
        if invalid:
            violations.append(violation("dependency-format", "依存関係は「なし」または issue 参照の箇条書きにしてください", "依存関係"))

    if labels is not None and "agent-task" not in labels:
        violations.append(violation("missing-agent-task-label", "agent-task label がありません"))
    if state is not None and state not in {"OPEN", "open"}:
        violations.append(violation("issue-not-open", f"実行対象 issue の state が OPEN ではありません: {state}"))

    return {
        "schema_version": SCHEMA_VERSION,
        "valid": not violations,
        "violations": violations,
    }


def fetch_issue(number: int, repo: str | None) -> dict[str, Any]:
    command = ["gh", "issue", "view", str(number), "--json", "body,state,labels,url"]
    if repo:
        command.extend(["--repo", repo])
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "GitHub issue の取得に失敗しました")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"GitHub response がJSONではありません: {exc}") from exc


def render_human(result: dict[str, Any]) -> str:
    if result["valid"]:
        return "agent-task/v1: valid"
    lines = ["agent-task/v1: invalid"]
    for row in result["violations"]:
        suffix = f" [{row['section']}]" if row.get("section") else ""
        lines.append(f"- {row['code']}{suffix}: {row['message']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="agent-task/v1 issue contract validator", exit_on_error=False)
    parser.add_argument("--body-file", type=Path)
    parser.add_argument("--issue", type=int)
    parser.add_argument("--repo")
    parser.add_argument("--json", action="store_true")
    try:
        args = parser.parse_args(argv)
    except argparse.ArgumentError as exc:
        print(str(exc), file=sys.stderr)
        return 3
    if (args.body_file is None) == (args.issue is None):
        print("--body-file または --issue のどちらか一方が必要です", file=sys.stderr)
        return 3

    context: dict[str, Any] = {}
    try:
        if args.body_file is not None:
            body = args.body_file.read_text(encoding="utf-8")
            result = validate_body(body)
        else:
            context = fetch_issue(args.issue, args.repo)
            result = validate_body(
                context.get("body") or "",
                labels=[row["name"] for row in context.get("labels") or []],
                state=context.get("state"),
            )
            result["issue"] = args.issue
            result["url"] = context.get("url")
            result["state"] = context.get("state")
    except (OSError, RuntimeError, ValueError) as exc:
        result = {
            "schema_version": SCHEMA_VERSION,
            "valid": False,
            "violations": [],
            "error": str(exc),
        }
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"検証不能: {exc}", file=sys.stderr)
        return 3

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_human(result))
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
