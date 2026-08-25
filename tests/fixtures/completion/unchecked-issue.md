<!-- agent-completion-pending:v1 -->
Contract: agent-task/v1

## 目的

未完了issueを検出する。

## 現状

完了条件が残っている。

## スコープ

- 完了判定を検証する。

## 非スコープ

- 新機能は追加しない。

## 実装要件

- 未チェックを検出する。

## 変更対象

- `tools/validate_agent_completion.py`

## 完了条件

- [ ] まだ完了していない。

## 検証コマンド

```bash
python3 -m unittest discover -s tests -v
```

## 完了証跡

- merged PR: https://github.com/example/repo/pull/900
- merge commit: abcdef1234567
- agent-verify/v1 status=passed
- Actions: https://github.com/example/repo/actions/runs/900

## 依存関係

なし
