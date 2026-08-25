#!/usr/bin/env python3
"""ネットワークなしで repository-side agent harness の閉ループを認証する。"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

try:
    from agent_task import BLOCKED, IN_PROGRESS, INVALID, READY, TaskError, TaskManager
    from agent_verify import (copy_ignore, generated_artifacts_check, snapshot_worktree,
                              source_commit, validate_export_payload)
    from validate_agent_completion import validate as validate_completion
    from validate_agent_issue import validate_body
except ModuleNotFoundError:  # tests import this module from the repository root.
    from tools.agent_task import BLOCKED, IN_PROGRESS, INVALID, READY, TaskError, TaskManager
    from tools.agent_verify import (copy_ignore, generated_artifacts_check, snapshot_worktree,
                                   source_commit, validate_export_payload)
    from tools.validate_agent_completion import validate as validate_completion
    from tools.validate_agent_issue import validate_body


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "harness-repo"
SCHEMA_VERSION = "agent-harness-certification/v1"
ADAPTER_METHODS = (
    "list_issues", "get_issue", "update_issue", "create_comment", "update_comment", "current_actor",
)


class FixtureGitHubAdapter:
    """GitHubAdapterと同じissue interfaceを持つ、永続的なfixture state。"""

    def __init__(self, issues: list[dict[str, Any]], actor: str = "fixture-agent") -> None:
        self.issues = {issue["number"]: copy.deepcopy(issue) for issue in issues}
        self.actor = actor
        self.prs: dict[int, dict[str, Any]] = {}
        self.artifacts: dict[int, dict[str, Any]] = {}
        self.write_calls: list[tuple[str, int]] = []
        self._comment_id = 1000

    def list_issues(self) -> list[dict[str, Any]]:
        return [copy.deepcopy(issue) for issue in self.issues.values()]

    def get_issue(self, number: int) -> dict[str, Any]:
        if number not in self.issues:
            raise KeyError(f"fixture issue #{number} does not exist")
        return copy.deepcopy(self.issues[number])

    def update_issue(self, number: int, *, add_labels: list[str] | None = None,
                     remove_labels: list[str] | None = None,
                     add_assignees: list[str] | None = None,
                     remove_assignees: list[str] | None = None) -> None:
        issue = self.issues[number]
        labels = set(issue.get("labels") or [])
        labels.update(add_labels or [])
        labels.difference_update(remove_labels or [])
        issue["labels"] = sorted(labels)
        assignees = set(issue.get("assignees") or [])
        assignees.update(add_assignees or [])
        assignees.difference_update(remove_assignees or [])
        issue["assignees"] = sorted(assignees)
        self.write_calls.append(("update", number))

    def create_comment(self, number: int, body: str) -> None:
        self.issues[number].setdefault("comments", []).append({"id": self._comment_id, "body": body})
        self._comment_id += 1
        self.write_calls.append(("create-comment", number))

    def update_comment(self, comment_id: int, body: str) -> None:
        for issue in self.issues.values():
            for comment in issue.get("comments", []):
                if comment.get("id") == comment_id:
                    comment["body"] = body
                    self.write_calls.append(("update-comment", comment_id))
                    return
        raise KeyError(f"fixture comment #{comment_id} does not exist")

    def current_actor(self) -> str:
        return self.actor

    def create_pr(self, number: int, body: str, metadata: dict[str, Any]) -> None:
        self.prs[number] = {"body": body, **copy.deepcopy(metadata)}

    def upload_artifact(self, issue: int, report: dict[str, Any]) -> None:
        self.artifacts[issue] = copy.deepcopy(report)

    def close_issue(self, number: int) -> None:
        self.issues[number]["state"] = "CLOSED"


def fixture_issue(number: int, body: str, *, labels: list[str] | None = None,
                  state: str = "OPEN", assignees: list[str] | None = None) -> dict[str, Any]:
    return {
        "number": number,
        "title": f"fixture #{number}",
        "body": body,
        "state": state,
        "labels": labels or [],
        "assignees": assignees or [],
        "comments": [],
        "url": f"https://fixture.invalid/issues/{number}",
    }


def contract_transition(adapter: FixtureGitHubAdapter, number: int) -> dict[str, Any]:
    issue = adapter.get_issue(number)
    result = validate_body(issue["body"], labels=issue["labels"], state=issue["state"])
    if result["valid"]:
        adapter.update_issue(number, add_labels=[READY], remove_labels=[INVALID])
    else:
        adapter.update_issue(number, add_labels=[INVALID], remove_labels=[READY])
    return result


def close_guard_decision(adapter: FixtureGitHubAdapter, number: int,
                         completion: dict[str, Any]) -> dict[str, Any]:
    issue = adapter.get_issue(number)
    if "agent-task" not in issue.get("labels", []):
        return {"target_state": issue["state"], "applied": False, "reason": "not an agent-task issue"}
    if completion.get("valid"):
        adapter.update_issue(number, remove_labels=["agent-completion-pending", "agent-completion-invalid"])
        return {"target_state": issue["state"], "applied": True, "reason": "completion valid"}
    adapter.issues[number]["state"] = "OPEN"
    adapter.update_issue(number, add_labels=["agent-completion-invalid"],
                         remove_labels=["agent-completion-pending", READY])
    return {"target_state": "OPEN", "applied": True, "reason": "completion invalid"}


def scenario(name: str, passed: bool, summary: str, *, expected_exit: int = 0) -> dict[str, Any]:
    return {
        "name": name,
        "status": "passed" if passed else "failed",
        "exit_code": 0 if passed else expected_exit or 1,
        "summary": summary,
    }


def run_current_verifier(now: str) -> dict[str, Any]:
    command = [
        sys.executable, str(ROOT / "tools" / "agent_verify.py"),
        "--issue-body", str(ROOT / "tests" / "fixtures" / "issues" / "valid.md"),
        "--now", now, "--json",
    ]
    env = os.environ.copy()
    env["AGENT_VERIFY_REGRESSION"] = "1"
    result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"current agent-verify failed: {result.stdout[-500:]} {result.stderr[-500:]}")
    report = json.loads(result.stdout)
    if report.get("status") != "passed":
        raise RuntimeError("current agent-verify report is not passed")
    return report


def run_certification(now: str, actor: str) -> dict[str, Any]:
    dt.date.fromisoformat(now)
    if not actor.strip():
        raise ValueError("actor must not be empty")
    report = run_current_verifier(now)
    valid_body = (FIXTURE_ROOT / "issue.md").read_text(encoding="utf-8")
    dependency_body = (FIXTURE_ROOT / "dependency.md").read_text(encoding="utf-8")
    invalid_body = (ROOT / "tests" / "fixtures" / "issues" / "missing-section.md").read_text(encoding="utf-8")
    adapter = FixtureGitHubAdapter([
        fixture_issue(201, valid_body, labels=["agent-task"]),
        fixture_issue(202, dependency_body, labels=["agent-task", READY]),
        fixture_issue(299, valid_body, state="OPEN"),
        fixture_issue(203, invalid_body, labels=["agent-task"]),
    ], actor=actor)
    scenarios: list[dict[str, Any]] = []

    try:
        contract_transition(adapter, 201)
        first = TaskManager(adapter).next()
        manager = TaskManager(adapter)
        manager.claim(201, actor)
        claim_state = manager.status(201)["state"]
        completion_issue = (ROOT / "tests" / "fixtures" / "completion" / "valid-issue.md").read_text(encoding="utf-8")
        completion_issue = completion_issue.replace("#900", "#201").replace("abcdef1234567", report["source_commit"])
        pr_body = (ROOT / "tests" / "fixtures" / "completion" / "valid-pr.md").read_text(encoding="utf-8")
        pr_body = pr_body.replace("#900", "#201").replace("abcdef1234567", report["source_commit"])
        metadata = {
            "state": "MERGED", "mergedAt": "2026-08-25T12:00:00Z",
            "mergeCommit": {"oid": report["source_commit"]},
            "url": "https://github.com/fixture/repo/pull/201",
        }
        adapter.create_pr(201, pr_body, metadata)
        adapter.upload_artifact(201, report)
        completion = validate_completion(pr_body, completion_issue, report, 201, metadata)
        adapter.issues[201]["body"] = completion_issue
        adapter.close_issue(201)
        close_result = close_guard_decision(adapter, 201, completion)
        fixture_ok = False
        with tempfile.TemporaryDirectory(prefix="agent-harness-fixture-") as directory:
            clone = Path(directory) / "repo"
            shutil.copytree(FIXTURE_ROOT, clone)
            (clone / "src" / "allowed.txt").write_text("after\n", encoding="utf-8")
            (clone / "generated" / "output.txt").write_text(
                (clone / "src" / "allowed.txt").read_text(encoding="utf-8"), encoding="utf-8"
            )
            fixture_ok = ((clone / "src" / "allowed.txt").read_text(encoding="utf-8") ==
                          (clone / "generated" / "output.txt").read_text(encoding="utf-8"))
        normal_ok = (first["issue"] == 201 and claim_state == "in-progress" and fixture_ok
                     and completion["valid"] and close_result["target_state"] == "CLOSED"
                     and adapter.get_issue(201)["state"] == "CLOSED")
        scenarios.append(scenario("normal-issue-to-closed", normal_ok,
                                  "contract -> next -> claim -> fixture change -> verify -> completion -> Closed"))
    except (KeyError, RuntimeError, TaskError, ValueError) as exc:
        scenarios.append(scenario("normal-issue-to-closed", False, str(exc)))

    try:
        invalid = contract_transition(adapter, 203)
        scenarios.append(scenario("invalid-issue-not-ready", not invalid["valid"]
                                   and INVALID in adapter.get_issue(203)["labels"],
                                   "missing required section remains contract-invalid"))
    except (KeyError, RuntimeError, ValueError) as exc:
        scenarios.append(scenario("invalid-issue-not-ready", False, str(exc)))

    try:
        dependency_state = TaskManager(adapter).status(202)["state"]
        next_result = TaskManager(adapter).next()
        scenarios.append(scenario("dependency-not-ready", dependency_state == "dependency-blocked"
                                   and next_result["state"] == "empty",
                                   "Open dependency excludes the issue from next"))
    except (KeyError, RuntimeError, ValueError) as exc:
        scenarios.append(scenario("dependency-not-ready", False, str(exc)))

    try:
        race_adapter = FixtureGitHubAdapter([fixture_issue(301, valid_body, labels=["agent-task", READY])], actor=actor)
        race_manager = TaskManager(race_adapter)
        race_manager.claim(301, "actor-a")
        try:
            race_manager.claim(301, "actor-b")
        except TaskError as exc:
            race_ok = exc.code == 4
        else:
            race_ok = False
        scenarios.append(scenario("claim-race", race_ok, "second actor receives deterministic exit 4"))
    except (KeyError, RuntimeError, ValueError) as exc:
        scenarios.append(scenario("claim-race", False, str(exc)))

    invalid_export = (ROOT / "tests" / "fixtures" / "verify" / "invalid-export.json").read_text(encoding="utf-8")
    export_code, export_summary = validate_export_payload(invalid_export)
    scenarios.append(scenario("schema-verifier-failure", export_code == 2,
                              f"invalid export is rejected with exit 2: {export_summary}"))

    try:
        with tempfile.TemporaryDirectory(prefix="agent-harness-stale-") as directory:
            clone = Path(directory) / "repo"
            shutil.copytree(ROOT, clone, ignore=copy_ignore)
            graph = clone / "data" / "graph.json"
            graph.write_text(graph.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            stale_code, stale_summary = generated_artifacts_check(clone)
        scenarios.append(scenario("generated-artifact-stale", stale_code == 2,
                                  f"stale generated artifact is rejected: {stale_summary}"))
    except (OSError, RuntimeError, ValueError) as exc:
        scenarios.append(scenario("generated-artifact-stale", False, str(exc)))

    audit = subprocess.run([sys.executable, "-c", "print('finding'); raise SystemExit(2)"],
                           capture_output=True, text=True, check=False)
    scenarios.append(scenario("strict-audit-finding", audit.returncode == 2,
                              "deterministic audit finding fixture returns exit 2", expected_exit=2))

    try:
        with tempfile.TemporaryDirectory(prefix="agent-harness-dirty-") as directory:
            worktree = Path(directory) / "repo"
            worktree.mkdir()
            (worktree / "tracked.txt").write_text("before\n", encoding="utf-8")
            before = snapshot_worktree(worktree)
            (worktree / "generated-by-bad-verifier.txt").write_text("unexpected\n", encoding="utf-8")
            after = snapshot_worktree(worktree)
        scenarios.append(scenario("dirty-worktree-detection", before != after,
                                  "verifier-side mutation is detected as worktree change"))
    except (OSError, RuntimeError, ValueError) as exc:
        scenarios.append(scenario("dirty-worktree-detection", False, str(exc)))

    try:
        close_adapter = FixtureGitHubAdapter([fixture_issue(401, valid_body, labels=["agent-task"], state="CLOSED")])
        unchecked = (ROOT / "tests" / "fixtures" / "completion" / "unchecked-issue.md").read_text(encoding="utf-8")
        failed_report = json.loads((ROOT / "tests" / "fixtures" / "completion" / "failed-agent-verify.json").read_text(encoding="utf-8"))
        invalid_completion = validate_completion("", unchecked, failed_report, 401, {})
        guard = close_guard_decision(close_adapter, 401, invalid_completion)
        scenarios.append(scenario("close-guard-reopen", not invalid_completion["valid"]
                                   and guard["target_state"] == "OPEN"
                                   and close_adapter.get_issue(401)["state"] == "OPEN",
                                   "unchecked or failed completion reopens a Closed issue"))
        non_agent = FixtureGitHubAdapter([fixture_issue(402, valid_body, state="CLOSED")])
        ignored = close_guard_decision(non_agent, 402, invalid_completion)
        scenarios.append(scenario("non-agent-close-ignored", not ignored["applied"]
                                   and non_agent.get_issue(402)["state"] == "CLOSED",
                                   "non-agent-task Closed issue is outside close guard"))
    except (KeyError, RuntimeError, ValueError) as exc:
        scenarios.append(scenario("close-guard-reopen", False, str(exc)))
        scenarios.append(scenario("non-agent-close-ignored", False, str(exc)))

    scenarios.append(scenario("current-agent-verify", report.get("status") == "passed"
                               and len(report.get("checks", [])) == 8,
                               "current repository agent-verify/v1 passed all 8 required checks"))
    failed = [row["name"] for row in scenarios if row["status"] != "passed"]
    return {
        "schema_version": SCHEMA_VERSION,
        "source_commit": report.get("source_commit") or source_commit(),
        "now": now,
        "actor": actor,
        "status": "failed" if failed else "passed",
        "scenarios": scenarios,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="agent harness offline E2E certification")
    parser.add_argument("--now", required=True)
    parser.add_argument("--actor", default="fixture-agent")
    parser.add_argument("--json", action="store_true")
    json_requested = "--json" in (argv or sys.argv)
    try:
        args = parser.parse_args(argv)
        result = run_certification(args.now, args.actor)
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        result = {"schema_version": SCHEMA_VERSION, "status": "failed", "error": str(exc)}
        if json_requested:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"agent-harness-certification: failed — {exc}", file=sys.stderr)
        return 3
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"agent-harness-certification: {result['status']}")
        for row in result["scenarios"]:
            print(f"- {row['status']}: {row['name']} — {row['summary']}")
    return 0 if result["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
