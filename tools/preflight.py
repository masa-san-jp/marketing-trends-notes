#!/usr/bin/env python3
"""エージェント作業前の読み取り専用環境検査。"""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "agent-preflight/v1"
VERSION_RE = re.compile(r"^(\d+)\.(\d+)$")
REQUIREMENT_RE = re.compile(r"^([A-Za-z0-9_.-]+)==([^\s#]+)")


def check(name: str, status: str, required: bool, detail: str) -> dict[str, object]:
    return {"name": name, "status": status, "required": required, "detail": detail}


def expected_python(root: Path) -> str:
    path = root / ".python-version"
    return path.read_text(encoding="utf-8").strip()


def actual_python() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}"


def read_git(root: Path, args: list[str]) -> tuple[int, str, str]:
    result = subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=False
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def check_python(root: Path) -> dict[str, object]:
    expected = expected_python(root)
    if not VERSION_RE.fullmatch(expected):
        return check("python", "failed", True, f".python-version が不正です: {expected!r}")
    actual = actual_python()
    status = "passed" if actual == expected else "failed"
    return check("python", status, True, f"required={expected}, actual={actual}")


def package_distribution_name(name: str) -> str:
    return name.lower().replace("-", "_").replace(".", "_")


def check_dependencies(root: Path) -> dict[str, object]:
    missing: list[str] = []
    wrong: list[str] = []
    requirements = root / "requirements.txt"
    for line in requirements.read_text(encoding="utf-8").splitlines():
        match = REQUIREMENT_RE.match(line.strip())
        if not match:
            continue
        name, required_version = match.groups()
        try:
            installed_version = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            missing.append(name)
            continue
        if installed_version != required_version:
            wrong.append(f"{name}={installed_version} (required {required_version})")
    if missing or wrong:
        detail = []
        if missing:
            detail.append("missing=" + ",".join(missing))
        if wrong:
            detail.append("version_mismatch=" + ",".join(wrong))
        return check("dependencies", "failed", True, "; ".join(detail))
    return check("dependencies", "passed", True, "requirements.txt の固定バージョンを満たしています")


def check_command(
    name: str,
    command: str,
    required: bool,
    command_lookup: Callable[[str], str | None],
) -> dict[str, object]:
    path = command_lookup(command)
    if path:
        return check(name, "passed", required, f"{command}: {path}")
    return check(name, "failed" if required else "skipped", required, f"{command} が見つかりません")


def check_git(root: Path) -> dict[str, object]:
    code, value, error = read_git(root, ["rev-parse", "--show-toplevel"])
    if code != 0:
        return check("git-repository", "failed", True, error or "git repository ではありません")
    try:
        resolved = Path(value).resolve()
        expected = root.resolve()
    except OSError as exc:
        return check("git-repository", "failed", True, str(exc))
    if resolved != expected:
        return check("git-repository", "failed", True, f"root={resolved} expected={expected}")
    return check("git-repository", "passed", True, str(resolved))


def check_hooks(root: Path) -> dict[str, object]:
    code, value, error = read_git(root, ["config", "--get", "core.hooksPath"])
    if code != 0:
        return check("hooks-path", "failed", True, error or "core.hooksPath が未設定です")
    if value != ".githooks":
        return check("hooks-path", "failed", True, f"actual={value!r}, expected='.githooks'")
    return check("hooks-path", "passed", True, value)


def check_optional_environment() -> list[dict[str, object]]:
    x_status = "passed" if os.environ.get("X_BEARER_TOKEN") else "skipped"
    x_detail = "X_BEARER_TOKEN は設定済み（値は表示しません）" if x_status == "passed" else "X_BEARER_TOKEN 未設定。X観測は任意です"
    return [
        check("github-cli", "passed" if shutil.which("gh") else "skipped", False,
              "gh が利用可能です" if shutil.which("gh") else "gh 未設定。issue操作時に必要です"),
        check("x-environment", x_status, False, x_detail),
        check("network", "skipped", False, "preflight はネットワークへ接続しません"),
    ]


def collect_checks(
    root: Path = ROOT,
    *,
    require_gh: bool = False,
    command_lookup: Callable[[str], str | None] = shutil.which,
) -> list[dict[str, object]]:
    checks = [check_python(root), check_dependencies(root)]
    checks.append(check_command("git-command", "git", True, command_lookup))
    checks.append(check_git(root))
    checks.append(check_hooks(root))
    gh = check_command("github-cli", "gh", require_gh, command_lookup)
    if not require_gh and gh["status"] == "failed":
        gh["status"] = "skipped"
    checks.append(gh)
    optional = check_optional_environment()
    checks.extend(row for row in optional if row["name"] != "github-cli")
    return checks


def report(checks: list[dict[str, object]]) -> dict[str, object]:
    failed = [row["name"] for row in checks if row["required"] and row["status"] != "passed"]
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "failed" if failed else "passed",
        "checks": checks,
        "failed_required": failed,
    }


def render_human(result: dict[str, object]) -> str:
    lines = [f"preflight: {result['status']}"]
    for row in result["checks"]:
        marker = "required" if row["required"] else "optional"
        lines.append(f"- {row['status']}: {row['name']} ({marker}) — {row['detail']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="読み取り専用のエージェント環境検査")
    parser.add_argument("--json", action="store_true", help="JSONだけをstdoutへ出す")
    parser.add_argument("--require-gh", action="store_true", help="gh CLIを必須にする")
    args = parser.parse_args(argv)
    result = report(collect_checks(require_gh=args.require_gh))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_human(result))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
