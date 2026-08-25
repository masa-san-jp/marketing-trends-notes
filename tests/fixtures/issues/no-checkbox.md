Contract: agent-task/v1

## 目的

完了条件のcheckboxを必須にする。

## 現状

完了条件が文章だけである。

## スコープ

- checkbox検証を追加する

## 非スコープ

- GitHub workflowは変更しない

## 実装要件

- 未チェック項目を要求する

## 変更対象

- `tools/validate_agent_issue.py`

## 完了条件

完了条件を検証できる。

## 検証コマンド

```bash
python3 -m unittest discover -s tests -v
```

## 完了証跡

テスト結果を記録する。

## 依存関係

なし
