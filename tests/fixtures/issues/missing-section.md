Contract: agent-task/v1

## 目的

契約違反を検出する。

## 現状

非スコープ節が欠けている。

## スコープ

- validatorを検証する

## 実装要件

- 必須節を検証する

## 変更対象

- `tools/validate_agent_issue.py`

## 完了条件

- [ ] 欠落節が固定コードで検出される

## 検証コマンド

```bash
python3 -m unittest discover -s tests -v
```

## 完了証跡

テスト結果を記録する。

## 依存関係

なし
