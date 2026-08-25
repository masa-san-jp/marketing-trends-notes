Contract: agent-task/v1

## 目的

fixture issue をハーネスE2Eで完走させる。

## 現状

実行前のfixtureである。

## スコープ

- 許可されたfixtureファイルを変更する。

## 非スコープ

- 外部サービスへ接続しない。

## 実装要件

- `src/allowed.txt` と対応する生成物を更新する。

## 変更対象

- `src/allowed.txt`
- `generated/output.txt`

## 完了条件

- [ ] fixtureの入力と生成物が一致する。

## 検証コマンド

```bash
python3 tools/certify_agent_harness.py --now 2026-08-25 --actor fixture-agent --json
```

## 完了証跡

完了時にcommit、PR、検証結果を記録する。

## 依存関係

なし
