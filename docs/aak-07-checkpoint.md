# AAK-07 qualified checkpoint — 2026-09-08

Issue86 / draft PR87 / branch `agent/aak-07-research-intake`。

AAK-SPEC/PLAN pin `b0e7c7f8d0a1f756fa708deef4fb380a62e45e0d`、base `26684f9f433f4616a31258cdeabc422151b5ae84`、qualified code `7be3d5ff495a91f3ce75159c96e9fc0ec383aa57`。

AAK-07-AC1..5は合成fixtureと正規owner gateでPASS。主要10 tests、full57 tests（skipなし）、実Issue本文validator、固定時計fixtureおよび実Issue本文のagent-verifyは全8 required checks PASS。nested regressionの既存6 skipは再帰防止で、standalone fullでは全件実行。actual parentの閉じたartifact/receipt schemaも検証済み。入力・receipt・knowledge commitは[aak-07-evidence.json](aak-07-evidence.json)、正規verifier reportは[aak-07-verification.json](aak-07-verification.json)。

親PR201はmainへ `f3dbc46d49861dd3c77b8cb387e25ff4414e974c` として統合済み。Issue196の受入・merge証拠同期後CLOSEDを確認し、実Issue86の契約・依存確認後に正規claimした。GitHubのdisplay nameをloginと誤認するclaim再確認の不具合を修復。Issueはcompletion-pendingへ進め、merge前にClosedにしない。

実装: native Markdownをowner revision境界で保存、参照集合をnative validatorで検証、source identityの重複排除、連続revision、Git CAS/idempotent receipt、index failureの再開、時計に基づく失効と未確認再検証task、地域・チャネル適用、訂正・撤回、既存Research export CLIへの明示store接続。local-only完了証跡を受理する既存文書要件をcompletion validatorへ同期した。Actionsを有効にする必要はない。

実観測・実Masa profile・実制作プラン・AAK02の実エージェント受入は実施していない。コード資格済み、main統合・公開は未実施。次は親DAGのAAK09で資格済みowner code/knowledgeを固定して固有性と機構接地へ接続する。
