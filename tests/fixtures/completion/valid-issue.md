<!-- agent-completion-pending:v1 -->
Contract: agent-task/v1

## 目的

実装完了を証跡付きで確定する。

## 現状

実装と検証が完了している。

## スコープ

- 完了証跡を検証する。

## 非スコープ

- 新しい機能は追加しない。

## 実装要件

- completion validatorを通す。

## 変更対象

- `tools/validate_agent_completion.py`

## 完了条件

- [x] validatorがexit 0になる。

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
