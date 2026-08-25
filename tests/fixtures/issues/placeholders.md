Contract: agent-task/v1

## 目的

TODOが残ったissueを拒否する。

## 現状

TODOが本文に残っている。

## スコープ

- TODOを検出する

## 非スコープ

- KBデータは変更しない

## 実装要件

- TODOを拒否する

## 変更対象

- `tools/validate_agent_issue.py`

## 完了条件

- [ ] TODOが固定コードで検出される

## 検証コマンド

```bash
python3 -m unittest discover -s tests -v
```

## 完了証跡

テスト結果を記録する。

## 依存関係

なし
