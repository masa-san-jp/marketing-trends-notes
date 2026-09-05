#!/usr/bin/env python3
"""agent-task issue の発見と状態遷移を行うCLI。"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from validate_agent_issue import validate_body


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "agent-task-state/v1"
READY = "agent-ready"
INVALID = "agent-contract-invalid"
IN_PROGRESS = "agent-in-progress"
BLOCKED = "agent-blocked"
CLAIM_MARKER = "<!-- agent-claim:v1 -->"
BLOCK_MARKER = "<!-- agent-block:v1 -->"
ISSUE_REF_RE = re.compile(r"(?:#(\d+)|https://github\.com/[^/\s]+/[^/\s]+/issues/(\d+))")
DEPENDENCY_RE = re.compile(r"^#{2,3}\s+依存関係\s*$", re.MULTILINE)
HEADING_RE = re.compile(r"^#{2,3}\s+.+$", re.MULTILINE)


class AdapterError(RuntimeError):
    pass


class TaskError(RuntimeError):
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code


class IssueAdapter(Protocol):
    def list_issues(self) -> list[dict[str, Any]]: ...
    def get_issue(self, number: int) -> dict[str, Any]: ...
    def update_issue(self, number: int, *, add_labels: list[str] | None = None,
                     remove_labels: list[str] | None = None,
                     add_assignees: list[str] | None = None,
                     remove_assignees: list[str] | None = None) -> None: ...
    def create_comment(self, number: int, body: str) -> None: ...
    def update_comment(self, comment_id: int, body: str) -> None: ...
    def current_actor(self) -> str: ...


def normalize_issue(raw: dict[str, Any]) -> dict[str, Any]:
    def names(rows: list[dict[str, Any]] | None) -> list[str]:
        return sorted(row.get("name") or row.get("login") for row in rows or [])

    return {
        "number": int(raw["number"]),
        "title": raw.get("title", ""),
        "body": raw.get("body") or "",
        "state": raw.get("state", "OPEN"),
        "labels": names(raw.get("labels")),
        "assignees": names(raw.get("assignees")),
        "comments": raw.get("comments") or [],
        "url": raw.get("url"),
    }


class GitHubAdapter:
    def __init__(self, repo: str):
        self.repo = repo

    def run(self, args: list[str]) -> Any:
        result = subprocess.run(["gh", *args], capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise AdapterError(result.stderr.strip() or "gh command failed")
        try:
            return json.loads(result.stdout) if result.stdout.strip() else None
        except json.JSONDecodeError as exc:
            raise AdapterError(f"gh response is not JSON: {exc}") from exc

    def list_issues(self) -> list[dict[str, Any]]:
        rows = self.run(["issue", "list", "--repo", self.repo, "--state", "open",
                         "--limit", "1000", "--json", "number,title,body,state,labels,assignees,url"])
        return [normalize_issue(row) for row in rows or []]

    def get_issue(self, number: int) -> dict[str, Any]:
        row = self.run(["issue", "view", str(number), "--repo", self.repo,
                        "--json", "number,title,body,state,labels,assignees,comments,url"])
        return normalize_issue(row)

    def get_dependency(self, reference: str) -> dict[str, Any]:
        if reference.startswith("#"):
            return self.get_issue(int(reference[1:]))
        row = self.run(["issue", "view", reference,
                        "--json", "number,title,body,state,labels,assignees,comments,url"])
        return normalize_issue(row)

    def update_issue(self, number: int, *, add_labels: list[str] | None = None,
                     remove_labels: list[str] | None = None,
                     add_assignees: list[str] | None = None,
                     remove_assignees: list[str] | None = None) -> None:
        command = ["issue", "edit", str(number), "--repo", self.repo]
        for label in add_labels or []:
            command.extend(["--add-label", label])
        for label in remove_labels or []:
            command.extend(["--remove-label", label])
        for actor in add_assignees or []:
            command.extend(["--add-assignee", actor])
        for actor in remove_assignees or []:
            command.extend(["--remove-assignee", actor])
        if len(command) > 4:
            self.run_text(command)

    def create_comment(self, number: int, body: str) -> None:
        self.run_text(["issue", "comment", str(number), "--repo", self.repo, "--body", body])

    def update_comment(self, comment_id: int, body: str) -> None:
        self.run_text(["api", "--method", "PATCH", f"repos/{self.repo}/issues/comments/{comment_id}",
                       "-f", f"body={body}"])

    def run_text(self, args: list[str]) -> None:
        result = subprocess.run(["gh", *args], capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise AdapterError(result.stderr.strip() or "gh command failed")

    def current_actor(self) -> str:
        result = subprocess.run(["gh", "api", "user", "--jq", ".login"],
                                capture_output=True, text=True, check=False)
        if result.returncode != 0 or not result.stdout.strip():
            raise AdapterError(result.stderr.strip() or "GitHub actor を取得できません")
        return result.stdout.strip()


def resolve_repo(explicit: str | None = None, environ: dict[str, str] | None = None,
                 remote_url: str | None = None) -> str:
    env = os.environ if environ is None else environ
    if explicit:
        return explicit
    if env.get("GITHUB_REPOSITORY"):
        return env["GITHUB_REPOSITORY"]
    if remote_url is None:
        result = subprocess.run(["git", "config", "--get", "remote.origin.url"],
                                cwd=ROOT, capture_output=True, text=True, check=False)
        remote_url = result.stdout.strip() if result.returncode == 0 else ""
    match = re.search(r"github\.com[:/]([^/]+/[^/]+?)(?:\.git)?$", remote_url or "")
    if match:
        return match.group(1)
    raise TaskError(3, "repository を --repo、GITHUB_REPOSITORY、origin URL から解決できません")


def dependency_numbers(body: str) -> list[int]:
    lines = body.splitlines()
    start = next((index for index, line in enumerate(lines) if DEPENDENCY_RE.match(line)), None)
    if start is None:
        return []
    values: list[int] = []
    for line in lines[start + 1:]:
        if HEADING_RE.match(line):
            break
        for first, second in ISSUE_REF_RE.findall(line):
            values.append(int(first or second))
    return sorted(set(values))


def dependency_references(body: str) -> list[str]:
    """Preserve repository identity; #196 and another repository's #196 differ."""
    match = DEPENDENCY_RE.search(body)
    if not match:
        return []
    section = body[match.end():]
    end = HEADING_RE.search(section)
    if end:
        section = section[:end.start()]
    return sorted(set(re.findall(r"https://github\.com/[^/\s]+/[^/\s]+/issues/\d+|#\d+", section)))


def marker_comment(issue: dict[str, Any], marker: str) -> dict[str, Any] | None:
    return next((comment for comment in issue.get("comments", [])
                 if marker in (comment.get("body") or "")), None)


def snapshot(issue: dict[str, Any]) -> tuple[Any, ...]:
    return (
        issue.get("state"), tuple(issue.get("labels") or []),
        tuple(issue.get("assignees") or []),
        tuple((comment.get("id"), comment.get("body")) for comment in issue.get("comments", [])),
    )


@dataclass
class State:
    name: str
    reason: str


class TaskManager:
    def __init__(self, adapter: IssueAdapter):
        self.adapter = adapter

    def validation(self, issue: dict[str, Any]) -> dict[str, Any]:
        return validate_body(issue.get("body") or "", labels=issue.get("labels") or [],
                             state=issue.get("state"))

    def dependencies_ready(self, issue: dict[str, Any]) -> tuple[bool, str]:
        for reference in dependency_references(issue.get("body") or ""):
            try:
                if reference.startswith("#"):
                    dependency = self.adapter.get_issue(int(reference[1:]))
                elif hasattr(self.adapter, "get_dependency"):
                    dependency = self.adapter.get_dependency(reference)
                else:
                    return False, f"横断依存を検証できません: {reference}"
            except AdapterError as exc:
                return False, f"依存 issue {reference} を取得できません: {exc}"
            if str(dependency.get("state", "")).upper() != "CLOSED":
                return False, f"依存 issue {reference} がClosedではありません"
        return True, "依存 issue はすべてClosedです"

    def state(self, issue: dict[str, Any]) -> State:
        if str(issue.get("state", "")).upper() == "CLOSED":
            return State("closed", "issueがClosedです")
        labels = set(issue.get("labels") or [])
        if INVALID in labels:
            return State("contract-invalid", "agent-contract-invalid labelがあります")
        validation = self.validation(issue)
        if not validation["valid"]:
            return State("contract-invalid", "; ".join(row["code"] for row in validation["violations"]))
        if BLOCKED in labels:
            return State("blocked", "agent-blocked labelがあります")
        if IN_PROGRESS in labels:
            actor = ", ".join(issue.get("assignees") or []) or "未割当"
            return State("in-progress", f"agent-in-progress（assignee={actor}）")
        if READY in labels:
            ready, reason = self.dependencies_ready(issue)
            return State("ready" if ready else "dependency-blocked", reason)
        return State("pending", "agent-ready labelがありません")

    def result(self, action: str, issue: dict[str, Any] | None, previous: str,
               state: str, changed: bool, reason: str) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "action": action,
            "issue": issue.get("number") if issue else None,
            "previous_state": previous,
            "state": state,
            "changed": changed,
            "reason": reason,
        }

    def next(self) -> dict[str, Any]:
        candidates = []
        for issue in self.adapter.list_issues():
            current = self.state(issue)
            if current.name == "ready":
                candidates.append((issue["number"], issue, current))
        if not candidates:
            return self.result("next", None, "empty", "empty", False, "実行可能なissueがありません")
        _, issue, current = sorted(candidates, key=lambda row: row[0])[0]
        return self.result("next", issue, current.name, current.name, False, current.reason)

    def status(self, number: int) -> dict[str, Any]:
        issue = self.adapter.get_issue(number)
        current = self.state(issue)
        return self.result("status", issue, current.name, current.name, False, current.reason)

    def actor(self, supplied: str | None) -> str:
        return supplied or os.environ.get("AGENT_ACTOR") or self.adapter.current_actor()

    def claim(self, number: int, actor: str | None, dry_run: bool = False) -> dict[str, Any]:
        issue = self.adapter.get_issue(number)
        previous = self.state(issue)
        if previous.name == "in-progress":
            current_actor = self.actor(actor)
            existing_claim = marker_comment(issue, CLAIM_MARKER)
            if current_actor in issue.get("assignees", []) and existing_claim:
                return self.result("claim", issue, previous.name, previous.name, False, "同じactorが既にclaim済みです")
            raise TaskError(4, "別actorがclaim中、またはclaim markerが不完全です")
        if previous.name != "ready":
            raise TaskError(2, f"issueはclaim可能なready状態ではありません: {previous.name} ({previous.reason})")
        current_actor = self.actor(actor)

        before_write = self.adapter.get_issue(number)
        if snapshot(issue) != snapshot(before_write):
            raise TaskError(4, "claim直前の再取得でissueが変化しました")
        if dry_run:
            return self.result("claim", issue, previous.name, "in-progress", True, "dry-run: writeは実行していません")

        self.adapter.update_issue(number, add_labels=[IN_PROGRESS], remove_labels=[READY],
                                  add_assignees=[current_actor])
        body = f"{CLAIM_MARKER}\nactor: {current_actor}\nissue #{number} をclaimしました。"
        existing = marker_comment(before_write, CLAIM_MARKER)
        if existing:
            self.adapter.update_comment(int(existing["id"]), body)
        else:
            self.adapter.create_comment(number, body)
        after = self.adapter.get_issue(number)
        if IN_PROGRESS not in after.get("labels", []) or current_actor not in after.get("assignees", []) \
                or marker_comment(after, CLAIM_MARKER) is None:
            raise TaskError(4, "claim後の再取得でclaim状態を確認できません")
        return self.result("claim", issue, previous.name, "in-progress", True, f"{current_actor} がclaimしました")

    def upsert_marker(self, issue: dict[str, Any], marker: str, body: str, dry_run: bool) -> None:
        if dry_run:
            return
        existing = marker_comment(issue, marker)
        if existing:
            self.adapter.update_comment(int(existing["id"]), body)
        else:
            self.adapter.create_comment(int(issue["number"]), body)

    def block(self, number: int, reason: str, actor: str | None, dry_run: bool = False) -> dict[str, Any]:
        if not reason.strip():
            raise TaskError(3, "block理由は空にできません")
        issue = self.adapter.get_issue(number)
        previous = self.state(issue)
        assignees = issue.get("assignees") or []
        current_actor = self.actor(actor)
        if IN_PROGRESS in (issue.get("labels") or []) and assignees and current_actor not in assignees:
            raise TaskError(5, f"claim owner {assignees[0]} 以外はblockできません")
        already = BLOCKED in (issue.get("labels") or []) and marker_comment(issue, BLOCK_MARKER)
        if already and (reason.strip() in (already.get("body") or "")):
            return self.result("block", issue, previous.name, "blocked", False, "同じ理由で既にblockedです")
        if not dry_run:
            self.adapter.update_issue(number, add_labels=[BLOCKED],
                                      remove_labels=[READY, IN_PROGRESS],
                                      remove_assignees=assignees)
        self.upsert_marker(issue, BLOCK_MARKER,
                           f"{BLOCK_MARKER}\nactor: {current_actor}\nreason: {reason.strip()}", dry_run)
        return self.result("block", issue, previous.name, "blocked", True,
                           "dry-run: block writeは未実行" if dry_run else reason.strip())

    def release(self, number: int, actor: str | None, dry_run: bool = False) -> dict[str, Any]:
        issue = self.adapter.get_issue(number)
        previous = self.state(issue)
        assignees = issue.get("assignees") or []
        if IN_PROGRESS not in (issue.get("labels") or []):
            if previous.name == "ready":
                return self.result("release", issue, previous.name, previous.name, False, "既にreadyです")
            raise TaskError(5, "in-progress状態のissueだけreleaseできます")
        current_actor = self.actor(actor)
        if not assignees or assignees[0] != current_actor:
            raise TaskError(5, f"releaseできるのはclaim owner {assignees[0] if assignees else '不明'} だけです")
        valid, reason = self.dependencies_ready(issue)
        contract = self.validation(issue)
        target = "ready" if valid and contract["valid"] else "pending"
        if dry_run:
            return self.result("release", issue, previous.name, target, True, "dry-run: writeは実行していません")
        add = [READY] if target == "ready" else []
        remove = [IN_PROGRESS]
        self.adapter.update_issue(number, add_labels=add, remove_labels=remove,
                                  remove_assignees=assignees)
        after = self.adapter.get_issue(number)
        actual = self.state(after)
        return self.result("release", issue, previous.name, actual.name, True,
                           reason if target == "ready" else "契約または依存がready条件を満たさないためpendingに戻しました")


def output(result: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        issue = f"#{result['issue']}" if result.get("issue") else "なし"
        print(f"{result['action']}: issue={issue} {result['previous_state']} -> {result['state']} "
              f"changed={result['changed']} — {result['reason']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="agent-task issue queue and state transitions")
    sub = parser.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--repo")
    common.add_argument("--json", action="store_true")
    sub.add_parser("next", parents=[common])
    status = sub.add_parser("status", parents=[common])
    status.add_argument("--issue", type=int, required=True)
    for name in ("claim", "release"):
        command = sub.add_parser(name, parents=[common])
        command.add_argument("--issue", type=int, required=True)
        command.add_argument("--actor")
        command.add_argument("--dry-run", action="store_true")
    block = sub.add_parser("block", parents=[common])
    block.add_argument("--issue", type=int, required=True)
    block.add_argument("--reason", required=True)
    block.add_argument("--actor")
    block.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        repo = resolve_repo(args.repo)
        manager = TaskManager(GitHubAdapter(repo))
        if args.command == "next":
            result = manager.next()
        elif args.command == "status":
            result = manager.status(args.issue)
        elif args.command == "claim":
            result = manager.claim(args.issue, args.actor, args.dry_run)
        elif args.command == "block":
            result = manager.block(args.issue, args.reason, args.actor, args.dry_run)
        else:
            result = manager.release(args.issue, args.actor, args.dry_run)
        output(result, args.json)
        return 0
    except (TaskError, AdapterError) as exc:
        result = {
            "schema_version": SCHEMA_VERSION,
            "action": args.command,
            "issue": getattr(args, "issue", None),
            "previous_state": "unknown",
            "state": "error",
            "changed": False,
            "reason": str(exc),
        }
        output(result, args.json)
        return exc.code if isinstance(exc, TaskError) else 3


if __name__ == "__main__":
    raise SystemExit(main())
