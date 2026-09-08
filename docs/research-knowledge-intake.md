# Research observation intake (AAK-07)

要件正本はIssue86とそこにpinされたAAK-SPEC/AAK-PLAN v1。ここは実装済みCLIの説明であり追加仕様ではない。

`tools/research_intake.py` はResearchが得た外部観測の派生ノートを、明示されたownerのローカルbare Git storeへ保存する。remote書込やLLM/daemonは不要。知識正本はstoreの `entities/observation-history/records/<record_id>/<revision>.json` 内のnative Markdown documentと参照文書。親へ本文を複製しない。共有可能と判断された派生知識だけを入力し、原典全文、raw、個人情報、認証情報を渡さない。

各recordは `market-observation/v1`。閉じたフィールドはconfig/market-observation.schema.jsonを参照する。`document` は既存frontmatter + 本文型。trend/practiceをそのまま利用しcontextはnative conceptへ写像する。`reference_documents` は参照するchannelやtrend等の同ownerのnative文書。候補を含む参照集合全体を既存build_graph validatorへ渡す。未解決参照、型・語彙の不一致、vendor-only verified、未読原典のverified化を既存gateが拒否する。新しい第9のentity型や閾値変更はない。

`source_checks` は出典URL、retrieved、実読日時checked_at、取得内容のSHA256、geo、channelsを保持する。これは外部workerが実際の原典確認から作る証跡であり、URLやhashがあるだけでこのツールが原典を読んだことにはならない。再引用を独立した出典へ変換しない。`epistemic_status` はobserved/externally-supported/inferred/proposed/simulated/unknownを区別し、合成入力はsimulatedとする。

`as_of` は原資料のデータ時点、`checked_at` は実読日時、`observed_at` は観測記録日時であり、freshness更新時もas_ofを書き換えない。stageの期限計算は既存kb.recheck_deadlineを使用する。primary確認が無い場合はunknown、期限切れはstaleのまま保持する。期限切れ・未確認の検索結果は再検証taskをPENDINGとして返す。workerは予算内で原典を確認できた時だけsource_checksを更新した次revisionをcommitする。予算が無い・失敗しただけでfreshnessを延長しない。

## CLI

以下の値は呼出し元のinstance profile/collectionから取得する。storeはコードcheckoutの外で、既存データと重ならない専用パスを指定する。`--now` は実運用では実時計を渡す。2026-09-05等の固定時計はfixture限定。

```bash
.venv/bin/python tools/research_intake.py init --store-root "$STORE" --creator "$CREATOR" --instance "$INSTANCE" --collection "$COLLECTION" --now "$NOW"
.venv/bin/python tools/research_intake.py prepare --store-root "$STORE" --creator "$CREATOR" --collection "$COLLECTION" --now "$NOW" --record "$CANDIDATE"
.venv/bin/python tools/research_intake.py commit --store-root "$STORE" --creator "$CREATOR" --collection "$COLLECTION" --now "$NOW" --record "$CANDIDATE" --expected-parent "$PARENT" --operation-id "$OPERATION" --run-id "$RUN"
.venv/bin/python tools/research_intake.py retrieve --store-root "$STORE" --creator "$CREATOR" --collection "$COLLECTION" --now "$NOW" --geo japan --channel channel/example
.venv/bin/python tools/export_signals.py --purpose artistic-research --knowledge-store "$STORE" --creator "$CREATOR" --collection "$COLLECTION" --geo japan --channel channel/example --now "$NOW"
.venv/bin/python tools/research_intake.py exchange --store-root "$STORE" --creator "$CREATOR" --collection "$COLLECTION" --now "$NOW"
```

prepare/validateは候補検証のみ。commitはexpected-parentに対するGit ref CASで原子的に保存し、同operationの同一入力再実行はNO_CHANGE。同operationの異なる入力やrevision衝突はCONFLICT。同一出典・主張field・as_of・地域・チャネルを別名で二重取込できない。異時点観測や出典訂正は同recordの連続revisionで追加し、旧版を保持する。

`knowledge-write-receipt/v1` はtarget_commitとindex_commitを分離する。index失敗はINDEX_PENDINGであり成功済みGit commitを失わない。同operation再試行またはindexコマンドで再生成できる。`observation-index.json` は再生成可能なGit外cacheで、検索は指定knowledge snapshotから再構築する。新しいprocessで再読込でき、index削除も履歴へ影響しない。

`invalidate` は `lifecycle: revoked` の次revisionとcommitと同じ引数を受け取る。撤回は履歴から消さず、通常Research signal exportから除外し、exchangeにはrevokedとinvalidates参照を出す。古いsnapshotを明示すれば当時の版を読み取れるため、利用側はsnapshotと有効性を記録する。

地域とチャネルは厳密一致で検索する。異なる対象はNOT_APPLICABLE。比較・判断へ採用した場合はResearch側が使ったrecord/revisionとknowledge commitを判断の根拠へ記録する。検索できただけで判断への再利用完了としない。exportはnative research-signal-export/v1を維持し、観測日、地域、知識snapshotをconstraintsへ運ぶ。code refはsource_commit、knowledge refはconstraintsおよびexchangeのknowledge_commitで分離する。人気を芸術評価の唯一の基準へ変換しない。

`exchange` は本文を含まないartifact-record/v1一覧。ownerのpayload_ref/hash、帰属、epistemic status、適用条件、出典と改訂・撤回参照を返す。owner Gitへの保存成功とAAK-02の実エージェント統合受入は別の状態である。

既存のentities/*.mdを読むexport、graph、coverage、auditの既定動作は維持する。新規storeのデータは勝手に公開mainへ移設しない。

## 検証

`tests.test_research_knowledge_intake` は実際の一時bare Git、別processの再読込、固定時計、二重取込、地域・チャネル誤適用、未読原典、vendor、CAS、訂正・撤回、INDEX_PENDING復旧を検証する。全入力は合成であり実観測の証跡ではない。最後にIssue86本文validatorとmake agent-verifyを実行する。
