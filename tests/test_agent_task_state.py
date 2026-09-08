import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from agent_task import (BLOCKED, CLAIM_MARKER, IN_PROGRESS, READY, TaskError, TaskManager,
                        dependency_numbers, resolve_repo, normalize_issue)  # noqa: E402


class GitHubIdentityTests(unittest.TestCase):
    def test_assignees_use_login_never_mutable_display_name(self):
        raw = {"number": 86, "labels": [{"name": "agent-in-progress"}],
               "assignees": [{"name": "Same display name", "login": "actor-one"},
                             {"name": "Same display name", "login": "actor-two"}]}
        issue = normalize_issue(raw)
        self.assertEqual(["actor-one", "actor-two"], issue["assignees"])
        raw["assignees"][0]["name"] = "Renamed"
        self.assertEqual(issue["assignees"], normalize_issue(raw)["assignees"])
        self.assertEqual(["agent-in-progress"], issue["labels"])

    def test_missing_login_does_not_authorize_display_name(self):
        self.assertEqual([], normalize_issue({"number": 86, "assignees": [{"name": "actor-one"}]})["assignees"])


class MemoryAdapter:
    def __init__(self, issues):
        self.issues = {issue["number"]: copy.deepcopy(issue) for issue in issues}
        self.write_calls = []
        self.next_comment_id = 10

    def list_issues(self):
        return [copy.deepcopy(issue) for issue in self.issues.values()]

    def get_issue(self, number):
        if number not in self.issues:
            raise RuntimeError(f"missing issue {number}")
        return copy.deepcopy(self.issues[number])

    def update_issue(self, number, *, add_labels=None, remove_labels=None,
                     add_assignees=None, remove_assignees=None):
        self.write_calls.append(("update", number))
        issue = self.issues[number]
        labels = set(issue["labels"])
        labels.update(add_labels or [])
        labels.difference_update(remove_labels or [])
        issue["labels"] = sorted(labels)
        assignees = set(issue["assignees"])
        assignees.update(add_assignees or [])
        assignees.difference_update(remove_assignees or [])
        issue["assignees"] = sorted(assignees)

    def create_comment(self, number, body):
        self.write_calls.append(("create-comment", number))
        self.issues[number]["comments"].append({"id": self.next_comment_id, "body": body})
        self.next_comment_id += 1

    def update_comment(self, comment_id, body):
        self.write_calls.append(("update-comment", comment_id))
        for issue in self.issues.values():
            for comment in issue["comments"]:
                if comment["id"] == comment_id:
                    comment["body"] = body
                    return
        raise RuntimeError(f"missing comment {comment_id}")

    def current_actor(self):
        return "fixture-agent"


def valid_body(dependency=None):
    body = (ROOT / "tests/fixtures/issues/valid.md").read_text(encoding="utf-8")
    if dependency is not None:
        body = body.replace("なし\n", f"- #{dependency}\n")
    return body


class CrossRepositoryDependencyTests(unittest.TestCase):
    def test_closed_local_issue_cannot_satisfy_open_external_dependency(self):
        url = "https://github.com/masa-san-jp/agentic-art-orchestration/issues/196"
        issue = {"number": 86, "body": valid_body().replace("なし\n", "- " + url + "\n"),
                 "state": "OPEN", "labels": ["agent-task", READY], "assignees": [], "comments": []}
        adapter = MemoryAdapter([issue, {"number": 196, "state": "CLOSED"}])
        calls = []
        def get_dependency(reference):
            calls.append(reference)
            return {"state": "OPEN", "url": reference}
        adapter.get_dependency = get_dependency
        manager = TaskManager(adapter)
        self.assertEqual("dependency-blocked", manager.state(issue).name)
        with self.assertRaises(TaskError): manager.claim(86, "fixture-agent")
        self.assertEqual([url, url], calls)
        self.assertEqual([], adapter.write_calls)

    def test_adapter_without_external_lookup_fails_closed(self):
        issue = {"number": 86, "body": valid_body().replace("なし\n", "- https://github.com/other/repo/issues/196\n"),
                 "state": "OPEN", "labels": ["agent-task", READY], "assignees": [], "comments": []}
        adapter = MemoryAdapter([issue, {"number": 196, "state": "CLOSED"}])
        self.assertEqual("dependency-blocked", TaskManager(adapter).state(issue).name)
        self.assertEqual([], adapter.write_calls)


def load_issues():
    rows = json.loads((ROOT / "tests/fixtures/github/issues.json").read_text(encoding="utf-8"))
    issues = []
    for row in rows:
        issue = {
            "number": row["number"],
            "title": f"fixture #{row['number']}",
            "body": valid_body(row.get("depends_on", [None])[0]) if row.get("depends_on") else valid_body(),
            "state": row["state"],
            "labels": row["labels"],
            "assignees": row["assignees"],
            "comments": row["comments"],
            "url": f"https://example.test/issues/{row['number']}",
        }
        issues.append(issue)
    return issues


class AgentTaskStateTests(unittest.TestCase):
    def test_dependency_parser_and_next_only_returns_ready(self):
        self.assertEqual(dependency_numbers(valid_body(104)), [104])
        adapter = MemoryAdapter(load_issues())
        result = TaskManager(adapter).next()
        self.assertEqual(result["issue"], 101)
        self.assertEqual(result["state"], "ready")

    def test_status_excludes_invalid_blocked_in_progress_and_closed(self):
        manager = TaskManager(MemoryAdapter(load_issues()))
        self.assertEqual(manager.status(105)["state"], "contract-invalid")
        self.assertEqual(manager.status(106)["state"], "blocked")
        self.assertEqual(manager.status(107)["state"], "in-progress")
        self.assertEqual(manager.status(108)["state"], "closed")
        self.assertEqual(manager.status(103)["state"], "dependency-blocked")

    def test_claim_is_idempotent_and_competing_actor_gets_exit_four(self):
        adapter = MemoryAdapter(load_issues())
        manager = TaskManager(adapter)
        first = manager.claim(101, "alice")
        self.assertEqual(first["state"], "in-progress")
        self.assertIn(IN_PROGRESS, adapter.issues[101]["labels"])
        self.assertIn("alice", adapter.issues[101]["assignees"])
        self.assertEqual(sum(CLAIM_MARKER in c["body"] for c in adapter.issues[101]["comments"]), 1)
        second = manager.claim(101, "alice")
        self.assertFalse(second["changed"])
        self.assertEqual(len(adapter.issues[101]["comments"]), 1)
        with self.assertRaises(TaskError) as raised:
            manager.claim(101, "bob")
        self.assertEqual(raised.exception.code, 4)

    def test_block_requires_reason_and_marker_is_idempotent(self):
        adapter = MemoryAdapter(load_issues())
        manager = TaskManager(adapter)
        with self.assertRaises(TaskError) as raised:
            manager.block(101, "  ", "alice")
        self.assertEqual(raised.exception.code, 3)
        manager.block(101, "外部権限待ち", "alice")
        manager.block(101, "外部権限待ち", "alice")
        self.assertIn(BLOCKED, adapter.issues[101]["labels"])
        self.assertEqual(sum("agent-block:v1" in c["body"] for c in adapter.issues[101]["comments"]), 1)

    def test_release_requires_owner_and_returns_ready(self):
        adapter = MemoryAdapter(load_issues())
        manager = TaskManager(adapter)
        manager.claim(101, "alice")
        with self.assertRaises(TaskError) as raised:
            manager.release(101, "bob")
        self.assertEqual(raised.exception.code, 5)
        result = manager.release(101, "alice")
        self.assertEqual(result["state"], "ready")
        self.assertIn(READY, adapter.issues[101]["labels"])
        self.assertNotIn(IN_PROGRESS, adapter.issues[101]["labels"])

    def test_dry_run_never_calls_adapter_write(self):
        adapter = MemoryAdapter(load_issues())
        manager = TaskManager(adapter)
        self.assertEqual(manager.claim(101, "alice", dry_run=True)["state"], "in-progress")
        self.assertEqual(manager.block(101, "dry-run", "alice", dry_run=True)["state"], "blocked")
        adapter.issues[101]["labels"].append(IN_PROGRESS)
        adapter.issues[101]["assignees"].append("alice")
        self.assertEqual(manager.release(101, "alice", dry_run=True)["state"], "ready")
        self.assertEqual(adapter.write_calls, [])

    def test_repo_resolution_precedence_and_github_urls(self):
        self.assertEqual(resolve_repo("explicit/repo", {"GITHUB_REPOSITORY": "env/repo"}), "explicit/repo")
        self.assertEqual(resolve_repo(None, {"GITHUB_REPOSITORY": "env/repo"}), "env/repo")
        self.assertEqual(resolve_repo(None, {}, "git@github.com:owner/repo.git"), "owner/repo")
        self.assertEqual(resolve_repo(None, {}, "https://github.com/owner/repo.git"), "owner/repo")


if __name__ == "__main__":
    unittest.main()
