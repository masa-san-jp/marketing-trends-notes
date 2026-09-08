# agent-task state transitions

`tools/agent_task.py` は GitHub issue の本文を #80 の validator で再検証し、ラベルだけでなく依存 issue の state と本文契約を合わせて状態を導出する。

## 状態

| 状態 | 条件 | 実行対象 |
|---|---|---|
| `contract-invalid` | validator が不適合、または `agent-contract-invalid` | いいえ |
| `dependency-blocked` | 契約は適合するが、依存 issue が未完了 | いいえ |
| `pending` | Open だが `agent-ready` がない | いいえ |
| `ready` | Open、契約適合、依存 Closed、`agent-ready` あり | `next` の対象 |
| `in-progress` | `agent-in-progress` と assignee がある | いいえ |
| `blocked` | `agent-blocked` がある | いいえ |
| `closed` | issue が Closed | いいえ |

対象 issue は Open かつ `agent-task` label があるものだけである。`next` は ready の issue 番号を昇順で1件返し、優先度や本文の意味を推測しない。

## 状態遷移

```text
contract-invalid ──本文修正──> ready
pending ──agent-ready + 依存Closed──> ready
ready ──claim──> in-progress
in-progress ──block(reason)──> blocked
in-progress ──release(owner)──> ready または pending
blocked ──手動でblock解除 + validator──> ready または pending
```

`claim` は更新直前と直後に issue を再取得する。assignee、ラベル、claim marker が期待値と違えば成功を返さず、競合として終了コード4を返す。GitHub APIにトランザクションがないため、再取得で確認できない状態は成功扱いにしない。

依存URLはrepositoryを含む識別子として取得する。同一番号の別repositoryのClosed issueで依存を満たさない。横断取得を実装していないadapterは実行不可を返す。

AAK-07は親DAGのcandidate証拠も確認するが、現行native claimのClosed条件を満たしたこととは区別する。未マージcandidateを受け入れる新たなclaim経路は本修正では追加しない。

## marker comment

- claim: `<!-- agent-claim:v1 -->`
- block: `<!-- agent-block:v1 -->`

同じ marker の comment があれば更新し、なければ1件だけ作成する。再実行でコメントを増やさない。

## コマンドと終了コード

```bash
python3 tools/agent_task.py next --json
python3 tools/agent_task.py status --issue 123 --json
python3 tools/agent_task.py claim --issue 123 --actor agent --json
python3 tools/agent_task.py block --issue 123 --actor agent --reason "依存する外部権限が未付与" --json
python3 tools/agent_task.py release --issue 123 --actor agent --json
```

mutation コマンドには `--dry-run` を付けられる。dry-run は adapter の write を呼ばない。

- `0`: 成功、または既に目的状態
- `2`: 契約、依存、ready 条件により実行不可
- `3`: 引数、repository解決、GitHub取得などの検証不能
- `4`: claim競合
- `5`: claim owner 以外の release/block など、権限のない状態変更

JSON は `schema_version: agent-task-state/v1`、`action`、`issue`、`previous_state`、`state`、`changed`、`reason` を必ず持つ。
