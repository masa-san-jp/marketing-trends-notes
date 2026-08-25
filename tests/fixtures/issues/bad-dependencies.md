Contract: agent-task/v1

## 目的

依存形式を検証する。

## 現状

依存が文章で書かれている。

## スコープ

- 依存形式を検証する

## 非スコープ

- GitHub APIは呼ばない

## 実装要件

- issue参照形式だけを許可する

## 変更対象

- `tools/validate_agent_issue.py`

## 完了条件

- [ ] 不正な依存形式が検出される

## 検証コマンド

```bash
python3 -m unittest discover -s tests -v
```

## 完了証跡

テスト結果を記録する。

## 依存関係

依存先はまだ決めていない
