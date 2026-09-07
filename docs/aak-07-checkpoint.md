# AAK-07 active checkpoint — 2026-09-08

親PR201はmainへ `f3dbc46d49861dd3c77b8cb387e25ff4414e974c` として統合済み。Issue196の5 synthetic ACとmerge証跡を同期しCLOSEDを確認。実Issue86の本文・ラベル・stateと依存をvalidatorで確認後、正規claim済み（actor `masa-san-jp`、branch `agent/aak-07-research-intake`）。display nameではなくloginでclaim所有者を確認する修復を実施し、native再試行はexit 0。state tests 11 PASS。取込機能は実装中、AAK07 AC1..5は最終検証前。以下は過去の停止記録。

# AAK-07 checkpoint — 2026-09-05

Issue: https://github.com/masa-san-jp/marketing-trends-notes/issues/86

SSOT specification / implementation plan pin: `b0e7c7f8d0a1f756fa708deef4fb380a62e45e0d`。
Base: `de1f77730d3856e7e81d591de48da5aed79a983a`。
Branch: `agent/aak-07-research-intake`。

前提修正のみ。native task toolが横断URLを同repoの整数Issueへ縮約する不具合を修正した。別repoの同番号Closed issueと実依存Open issueの組合せ、および横断取得不能adapterについて、claimを拒否しwriteが無いことを試験した。

実Issue本文・label `agent-task`・state `open`を取得し、owner validatorでvalidを確認した。TaskManager.statusはpending、claimはexit 2（agent-readyなし）。GitHubのclaim/label/assignee/完了checkboxは変更していない。これは実snapshotを用いたread-only観測であり、live claim成功ではない。

親AAK-04の資格済みcandidateは `83f7e9e8d1c6e25b39351aebb6eb15cb12da4685`、`instance-profile/v1`、PR #201。synthetic focused 14 / full 580 tests (1 existing skip) PASSの証拠は確認済み。ただし親Issue #196はOpen、Marketingのnative claimはClosed依存を要求し、未マージcandidate受入経路を持たない。現行gateを迂回しない。

検証:

- Python 3.14.6、PyYAML 6.0.3、正規hooksPathを用意しmake preflight PASS。
- task state tests: 9 PASS。
- make test: 44 PASS。
- 実Issue bodyのvalidate_agent_issue: PASS。
- 実Issue bodyのagent_verify --now 2026-09-05: PASS（regression 44 tests / 6 nested gate skips、graph 127 entities / 133 relations、export 60 signals、生成物再生成一致）。

AAK-07-AC1..4: NOT_RUN（knowledge intake未実装）。AAK-07-AC5は前提コードでの実Issue/既存gate PASS、機能完成時には再検証する。統合実証・merge・公開: NOT_RUN。

再開: ownerが親依存を正式に統合・完了させるか、仕様・native契約を同期したcandidate qualification経路を承認した後、実Issueを再取得してvalidatorとdependencies_readyを実行する。条件成立後のみagent-readyを設定し、正規TaskManager.claimで取得する。次にAAK-07のintake、鮮度、再検証task、export、指定test_research_knowledge_intakeを実装する。現在の前提修正を再作成しない。

この境界の影響を受けないAAK-08を親DAGに従って継続する。ここは再開証跡であり追加仕様ではない。
