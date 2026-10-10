#!/usr/bin/env python3
"""element-request/v1 を1件読み、Haiku 5.5 に答えの値だけを出させて element-answer/v1 で返す adapter。

    python3 tools/card_excerpts.py next --entity trend/anxiety-multiplication | python3 tools/haiku_answerer.py

stdin に依頼1件（JSON）、stdout に答え1件（JSON）。呼び出しは依頼1件ごとに独立で、会話の履歴を持たない
（`claude -p`、ツール・MCP・スキル・セッション保存なし、CLAUDE.md の無い一時ディレクトリで実行）。
値の確認はこの adapter ではしない。確認とやり直しは呼び出し側（card_excerpts.py）の責務。
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile

MODEL = "claude-haiku-5-5"
EFFORT = "max"
TIMEOUT_SECONDS = 600

SYSTEM_PROMPT = (
    "あなたは要素ごとの依頼に、答えの値だけを返す答え手です。"
    "前置き、説明、引用符、記号の飾り、改行を付けず、依頼の answer_format に合う値そのものを1つだけ出力します。"
    "text で本文の抜き書きを求められたときは、inputs にある文字列を一字も変えず、そのまま連続した1行で写します。"
    "previous_failure があれば、その理由を直した値を返します。"
)


def build_prompt(request: dict) -> str:
    shown = {k: request[k] for k in ("element_id", "instruction", "inputs", "answer_format", "checks", "previous_failure")}
    return (
        "次の依頼に答えてください。出力は答えの値だけです。\n\n"
        + json.dumps(shown, ensure_ascii=False, indent=2)
    )


def ask_model(prompt: str) -> str:
    # CLAUDE.md を拾わないよう、ホーム配下ではない一時ディレクトリで実行する。
    with tempfile.TemporaryDirectory(prefix="haiku-answerer-") as cwd:
        result = subprocess.run(
            ["claude", "-p", "--model", MODEL, "--effort", EFFORT,
             "--tools", "", "--strict-mcp-config", "--disable-slash-commands",
             "--no-session-persistence", "--system-prompt", SYSTEM_PROMPT],
            input=prompt, capture_output=True, text=True, encoding="utf-8",
            cwd=cwd, timeout=TIMEOUT_SECONDS, check=False)
    if result.returncode:
        raise RuntimeError(f"claude が終了コード {result.returncode}: {result.stderr.strip()[:300]}")
    return result.stdout


def main() -> int:
    try:
        request = json.load(sys.stdin)
        value = ask_model(build_prompt(request)).strip()
        answer = {"contract_version": "element-answer/v1",
                  **{k: request[k] for k in ("run_id", "element_id", "attempt")},
                  "value": value}
        sys.stdout.write(json.dumps(answer, ensure_ascii=False, sort_keys=True))
        return 0
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
