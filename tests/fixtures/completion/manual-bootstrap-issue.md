<!-- agent-manual-completion:v1 -->
<!-- agent-completion-pending:v1 -->
Contract: agent-task/v1

## 目的

bootstrap issue の直接実装を移行する。

## 現状

実装と検証が完了している。

## スコープ

- 既存実装の完了証跡を確定する。

## 非スコープ

- 新しい機能は追加しない。

## 実装要件

- 移行用の完了証跡を検証する。

## 変更対象

- `tools/validate_agent_completion.py`

## 完了条件

- [x] validatorがexit 0になる。

## 検証コマンド

```bash
python3 -m unittest discover -s tests -v
```

## 完了証跡

- direct commit: abcdef1234567
- agent-verify/v1 status=passed
- Actions: https://github.com/example/repo/actions/runs/900

## 依存関係

なし
