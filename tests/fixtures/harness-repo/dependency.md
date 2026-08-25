Contract: agent-task/v1

## 目的

依存状態をfixtureで確認する。

## 現状

依存先が未完了である。

## スコープ

- 依存状態を判定する。

## 非スコープ

- 依存先を変更しない。

## 実装要件

- 依存未完了をreadyから除外する。

## 変更対象

- fixture state

## 完了条件

- [ ] 依存未完了の状態を検出する。

## 検証コマンド

```bash
python3 tools/certify_agent_harness.py --now 2026-08-25 --actor fixture-agent --json
```

## 完了証跡

fixture検証結果を記録する。

## 依存関係

- #299
