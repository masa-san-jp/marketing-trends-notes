Contract: agent-task/v1

## 目的

検証エージェントが契約適合のissue本文を判定できるようにする。

## 現状

issue本文を機械検証するコマンドがない。

## スコープ

- validatorとfixtureを追加する

## 非スコープ

- GitHub issueの状態遷移は変更しない

## 実装要件

1. 必須節と完了条件を検証する。
2. JSONと終了コードを固定する。

## 変更対象

- `tools/validate_agent_issue.py`
- `tests/test_agent_issue_contract.py`

## 完了条件

- [ ] valid fixture が exit 0 になる
- [ ] invalid fixture が固定 violation code で exit 2 になる

## 検証コマンド

```bash
python3 tools/validate_agent_issue.py --body-file tests/fixtures/issues/valid.md --json
python3 -m unittest discover -s tests -v
```

## 完了証跡

完了時にcommit、CI run URL、fixtureごとの終了コードをissueコメントへ記録する。

## 依存関係

なし
