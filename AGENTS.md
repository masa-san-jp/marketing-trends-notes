# Agent entrypoint

このファイルは、このリポジトリで作業する実行エージェントの入口である。ここに要件を複製せず、正本へリンクして実行順と停止条件だけを定める。

## 正本と読む順番

1. 実行対象の GitHub issue を読む。issue #1 は KB のミッション正本、issue #78 は repository-side agent harness の正本である。
2. このファイルを読み、dirty worktree と作業境界を確認する。
3. [README.md](README.md) で構造と標準コマンドを確認する。
4. [docs/schema.md](docs/schema.md) を読み、エンティティを変更する場合は必須項目と本文型に従う。
5. 調査タスクは [docs/investigation-task.md](docs/investigation-task.md) を1件分の手順として使う。
6. 鮮度の変更は [docs/freshness.md](docs/freshness.md)、環境や認証は [docs/local-environment.md](docs/local-environment.md) を読む。
7. `agent-task` issue の契約は [docs/agent-task-contract.md](docs/agent-task-contract.md) を読む。
8. issue の発見・claim・block・release は [docs/agent-task-state.md](docs/agent-task-state.md) と `tools/agent_task.py` のJSON結果を使う。
9. PRの完了契約とClosed guardは [`.github/pull_request_template.md`](.github/pull_request_template.md)、`tools/validate_agent_completion.py`、`.github/workflows/agent-completion.yml`、`.github/workflows/agent-close-guard.yml` を正本として使う。
10. ハーネス全体の責務、状態、JSON、権限、復旧は [docs/agent-harness.md](docs/agent-harness.md) を正本として使う。

## 作業契約

- 1 issue = 1 task。issue の目的・scope・非スコープ・完了条件を先に確認する。
- issue に書かれていない設計変更、閾値変更、型・関係語彙の追加をしない。必要なら issue に戻して停止する。
- 作業開始前に `git status --short --branch` を確認する。
- 既存の変更を自分のものと仮定しない。`git reset`、`git checkout`、`git restore`、`git stash`、広い範囲の削除を使わない。
- scope 外のファイルを変更しない。必要になった変更は完了証跡に理由を記録する。
- `data/` と `overviews/coverage.md` の生成ブロックを手で編集しない。入力を直し、生成コマンドを実行する。
- 調査内容は出典URL、certainty、retrieved、as_of を正しく記録する。確定できないことは推測せず `未確認` として残す。
- X token やその他の秘密をリポジトリ、issue、PR、ログに書かない。

## PR完了とClosedの手順

通常の `agent-task` は、次の順に完了させる。

1. PR本文に `Closes #N` を1件だけ書き、テンプレートの4節を埋める。
2. issue本文に `agent-completion-pending:v1` marker、checked済みの完了条件、PR URL、検証 run URL、`agent-verify/v1 status=passed` を記録する。merge commit SHAはmerge後に追記する。
3. PRの `agent-completion / completion` check と通常のCIが成功してからmergeする。
4. merge後にissueの完了証跡へmerge commit SHAを追記してClosedにする。close guardが再検証し、不足時はReopenする。

branch protectionでは、`main` に対してPR必須、required status check `agent-completion / completion`、通常の `validate / validate` を設定する。設定はRepository Settings > Branches > Branch protection rules（またはRulesets）で行い、このリポジトリからAPI設定を自動変更しない。

ハーネス導入時にmainへ直接実装済みのbootstrap issue #79〜#84だけは、移行期間の証跡として `agent-manual-completion:v1` markerとcommit SHA、成功run URLを使える。新規issueでこのmarkerを使ってはならない。

## 開始・実装・検証

開始時:

```bash
make preflight
git status --short --branch
```

環境が無ければ `make setup` を実行する。通常の検証は次の順で行う。

```bash
make test
python3 tools/build_graph.py --check
python3 tools/audit.py --dry-run --now YYYY-MM-DD --fail-on-findings
```

`YYYY-MM-DD` は検証対象日へ置き換える。issue 契約を含む `make agent-verify` を最終ゲートにする。

```bash
make agent-verify ISSUE_BODY=tests/fixtures/issues/valid.md NOW=2026-08-25
```

実装中に外部調査を行う場合は、[docs/investigation-task.md](docs/investigation-task.md) の1件手順に従い、手元の記憶で空欄を埋めない。

## 停止条件

次の場合は変更を広げず、理由と再開に必要な条件を issue コメントまたはPRに記録する。

- 完了条件または非スコープが曖昧で、既存の正本から決められない
- 検証が失敗し、原因が自分の変更か既存の未完成変更か切り分けられない
- 外部出典、ネットワーク、GitHub権限、認証が必要だが利用できない
- issue の要件を満たすためにスキーマ、閾値、別 issue の目的を変更する必要がある
- 他エージェントの変更を消す、上書きする、または推測で修正する必要がある

## 完了報告

- 完了条件を1項目ずつ確認し、実行したコマンドと終了コードを記録する。
- 生成物、テスト、CIの結果を記録する。
- issueを自己判断でClosedにしない。完了証跡を残し、通常はPRのmergeとclose guardに委ねる。bootstrap issueの移行処理ではvalidatorの許可条件を満たした後だけClosedにする。
- GitHubや外部サービスへ書き込めない場合、書き込んだふりをせず、必要な操作と理由を報告する。
