# Repository-side agent harness

この文書は、GitHub issueを実行可能なSSOT taskとして投入し、claim、実装、検証、PR完了、Closed判定までを一つの閉ループとして扱うための最終仕様である。調査対象のKBデータや外部サイトの品質評価はこのハーネスの責務ではない。

## 責務境界

| 層 | 正本・入口 | 責務 |
|---|---|---|
| 入口 | `AGENTS.md`、`make preflight` | 読み順、作業境界、停止条件、環境の再現 |
| issue契約 | `tools/validate_agent_issue.py`、`agent-task/v1` | 必須節、checkbox、依存、検証コマンド、label/state |
| task状態 | `tools/agent_task.py`、`agent-task-state/v1` | `next`、`status`、`claim`、`block`、`release` |
| 統合検証 | `tools/agent_verify.py`、`agent-verify/v1` | issue、graph、回帰、schema、strict audit、export、生成物、worktree |
| 完了 | `tools/validate_agent_completion.py`、PR/issue workflows | PR本文、issue証跡、merge commit、verifier report、Close guard |
| 認証 | `tools/certify_agent_harness.py`、`agent-harness-certification/v1` | ネットワークなしの正常・異常E2Eと現在repo verifier |

このリポジトリのハーネスは、agent modelを起動したり、外部調査の内容を採点したりしない。モデルはissueを選び、変更し、定められた入口で検証結果を残す実行主体である。

## 状態遷移

```text
Open + agent-task + valid + agent-ready
  ├─ claim(actor) ───────────────> agent-in-progress + assignee
  ├─ dependency未完了 ───────────> dependency-blocked（next対象外）
  └─ contract違反 ───────────────> agent-contract-invalid

agent-in-progress ── block(reason) ──> agent-blocked
agent-in-progress ── release(owner) ─> agent-ready または pending
PR completion passed ── merge + evidence ─> Closed（close guard再検証）
Closed + completion違反 ───────────────> Open + agent-completion-invalid
```

`agent-completion-pending` は、完了checkboxをcheckedにした後、Close guardが証跡を検証する短い遷移を表す。Close guardは`agent-task` labelのissueだけに作用する。

## 標準コマンドと終了コード

```bash
make setup
make preflight
python3 tools/agent_task.py next --json
python3 tools/agent_task.py claim --issue N --actor ACTOR --json
make agent-verify ISSUE=N NOW=YYYY-MM-DD
python3 tools/validate_agent_completion.py --pr N --issue N --verify-report report.json --json
python3 tools/certify_agent_harness.py --now YYYY-MM-DD --actor ACTOR --json
```

task CLIは、正常終了0、契約・状態不適合2、環境・引数不足3、claim競合4、所有者違反5を返す。`agent-verify`は、全required check成功0、検証失敗2、開始不能3を返す。completion validatorとcertificationも、適合0、契約不適合2、開始不能3で固定する。

## JSON契約

- `agent-task-state/v1`: `action`、`issue`、`previous_state`、`state`、`changed`、`reason`
- `agent-verify/v1`: `issue`、`source_commit`、`now`、`status`、8件の`checks[]`
- `agent-completion-validation/v1`: `valid`、`closing_issues`、固定された`violations[]`
- `agent-harness-certification/v1`: `source_commit`、`now`、`actor`、`status`、scenarioごとの`status`/`exit_code`/`summary`

JSONモードではstdoutにJSON以外を出さない。検証対象日`--now`とactorは暗黙値を使わず、呼び出し元から渡す。

## GitHub permissionsと設定

workflowはファイル内で権限を宣言する。通常CIは`contents: read`、PR completionは`contents: read`、`issues: read`、`pull-requests: read`、Close guardは`contents: read`、`pull-requests: read`、`issues: write`だけを使う。branch protectionのAPI変更はハーネスの責務外である。

mainにはPR必須、`agent-completion / completion`、`validate / check`、`validate / agent-harness-e2e`をrequired status checkとして設定する。設定場所はRepository Settings > Branches > Branch protection rules（またはRulesets）である。

## 障害時の復旧

- `agent-contract-invalid`: issue本文を契約validatorで修正し、workflowが`agent-ready`を再導出する。
- `agent-in-progress`: claim ownerだけが作業を続けるか、ownerとして`release`する。別actorはclaimせずexit 4/5を記録する。
- `agent-blocked`: `agent-block:v1` markerの理由を解消してから、明示的にreleaseまたはissueを更新する。
- `agent-completion-invalid`: Close guardのmarker commentと固定violation codeを読み、証跡・merge・verifierを修正して再度pendingから実行する。Closedのままにしない。
- certification failure: JSONのfailed scenarioだけを再実行し、外部ネットワークや実issueを使わずfixtureで再現する。

bootstrap issue #79〜#84のmain直接実装を移行するときだけ`agent-manual-completion:v1`を使える。新規taskは必ずPR completion契約を使う。

## 非スコープ

- 実際のエージェントモデルの起動・性能測定
- X、Google Trends RSS、外部URLの取得品質
- branch protectionのAPI自動変更
- 一つのPRで複数のagent-task issueを閉じること
