# agent-task/v1 issue contract

`agent-task` label を付ける issue は、実行エージェントが追加の設計会話なしに実装できる SSOT でなければならない。この文書が契約の正本であり、[issue form](../.github/ISSUE_TEMPLATE/agent-task.yml)、[validator](../tools/validate_agent_issue.py)、workflow はこの version を実装する。

## 必須の先頭行

本文に次を1回だけ置く。

```text
Contract: agent-task/v1
```

## 必須節

次の節をこの順序で各1回だけ置く。GitHub Issue Form が生成する `###` と、手書き本文の `##` は同じ節として扱う。見出し名は完全一致させる。

1. `目的`
2. `現状`
3. `スコープ`
4. `非スコープ`
5. `実装要件`
6. `変更対象`
7. `完了条件`
8. `検証コマンド`
9. `完了証跡`
10. `依存関係`

各節は空でなく、`TODO`、`TBD`、`後で決める`、`ここに記入` などのテンプレート未確定語を残さない。

## 完了条件の規則

起票時点では、`## 完了条件` に少なくとも1件の `- [ ] ...` が必要である。各項目は、ファイル、コマンド終了コード、状態、URL、件数などの観測可能な完了結果を表す。抽象的な「よくする」「対応する」だけの項目は不適合とする。

完了時に全項目を `[x]` にすることと、完了証跡へ実行結果を書くことは、後続の completion validator が検査する。
全項目をチェックしてからClosedにするまでの短い遷移では、本文に
`<!-- agent-completion-pending:v1 -->` を置く。このmarkerがある本文はvalidatorが完了待ちとして扱い、
`agent-ready`には戻さない。

## 検証コマンドの規則

`## 検証コマンド` には `bash` fenced code block を少なくとも1つ持たせる。ブロック内に、終了コードで成否を判断できる空でないコマンドを1つ以上書く。検証結果を `|| true` で成功扱いにしてはならない。

## 依存関係の規則

依存がなければ `なし` と書く。依存がある場合は、各行を `- #123` または `- https://github.com/OWNER/REPO/issues/123` の形式にする。依存 issue の完了はタスク選択側で検査する。

## 状態ラベル

- `agent-task`: この契約の対象
- `agent-ready`: 契約適合、依存解決済み、実行可能
- `agent-contract-invalid`: 契約不適合。実行対象外
- `agent-completion-pending`: 完了条件と証跡をclose guardが検証中

`agent-ready` と `agent-contract-invalid` は validator workflow が導出する。エージェントは本文を読まずにラベルだけを信頼してはならず、取得時に validator を再実行する。

## 検証結果

`tools/validate_agent_issue.py --json` は `schema_version: agent-task-validation/v1`、`valid`、`violations` を返す。契約違反は終了コード2、入力・GitHub取得不能は終了コード3、適合は終了コード0である。
