---
id: practice/generative-ai-workflow-governance
uri: urn:mtn:practice/generative-ai-workflow-governance
type: practice
label_ja: 生成AIの業務プロセス組み込み・利用ガバナンス
label_en: Generative AI workflow integration and usage governance
authority:
  wikidata: null
  none_reason: "Wikidataで「生成AIの業務プロセス組み込み・利用ガバナンス」「generative AI workflow governance」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2024~"
  end: ".."
  display: "企業の生成AI導入・試験利用が広がり、組織実装と管理を設計する2020年代"
saturation: spreading
evidence:
  - {field: time, source: "https://www.ipa.go.jp/digital/chousa/dx-trend/rcu1hd0000017uk8-att/dx-trend-2026.pdf", certainty: independent, retrieved: primary, as_of: "2025年度"}
channels: []
relations:
  - {type: responds_to, target: trend/generative-ai-business-adoption, certainty: hypothesis, source: "https://www.ipa.go.jp/digital/chousa/dx-trend/rcu1hd0000017uk8-att/dx-trend-2026.pdf"}
sources:
  - https://www.ipa.go.jp/digital/chousa/dx-trend/dx-trend-2026.html
  - https://www.ipa.go.jp/digital/chousa/dx-trend/rcu1hd0000017uk8-att/dx-trend-2026.pdf
  - https://www.ipa.go.jp/pressrelease/2026/press20260515.html
status: draft
updated: 2026-08-11
---

# 生成AIの業務プロセス組み込み・利用ガバナンス

## 何をするか

生成AIを個人の試行で終わらせず、対象業務を一つ選び、入力データの分類、利用可能なツール、出力の確認者、保存・削除、
事故時の報告、業務プロセスへの組み込み方を定義する。導入前後で処理時間、手戻り、品質、人的レビュー、インシデント、
費用を記録し、AIの出力を最終判断そのものとみなさない。

IPAの「DX動向2026」では、生成AIの利用が個人利用・試験利用に集中し、部署の業務プロセスへの組み込みは11.9％、全社的な
サービスへの組み込みは18.6％にとどまる。またAI導入・運用上の課題として、専門人材不足50.1％、生成AIの効果やリスクへの
理解不足45.8％、利用ルールや基準の作成の難しさ39.7％が挙げられている。そこでこのpracticeでは、ツール導入ではなく、
業務責任者とガバナンス、効果測定を一つの運用にする。

## どのトレンドへの応答か

[trend/generative-ai-business-adoption](../trends/generative-ai-business-adoption.md)（企業の生成AI導入拡大）への応答とみる。
導入率が上がるほど、個人利用と業務プロセス・全社サービスへの組み込みを分け、利用ルールと効果測定を整える必要が増えるためである。
ただし、このpracticeを採用すれば業務効率、売上、顧客満足度が改善するとは確認していないため、関係の確度は`hypothesis`とした。

## 成立条件・失敗条件

**効果未確認**:（対象事業で生成AIを業務プロセスに組み込み、利用ガバナンスを運用していない）。処理時間、品質、再作業、売上、
顧客満足度、インシデントへの効果は測っていない。

成立条件は、業務の責任者と人間による確認範囲が決まっていること、機密情報・個人情報・著作物等の入力ルールがあること、
承認済みツールとログの扱いが定義されていること、出力品質を評価する基準があることである。全社ルールだけを配布しても、
対象業務、判断者、例外処理、測定指標が決まっていなければ、個人の試行から組織的な実装へ移ったとはみなさない。

**未確認**: 業務カテゴリ別の効果、導入・運用コスト、ルール遵守率、人的レビューの負荷、誤出力・情報漏洩・権利処理の発生率、
組織実装と顧客価値・売上の因果関係。

## 飽和度の判定

`spreading` とした。企業調査でAIの利用拡大とガバナンス課題が同時に観測され、利用規程やリスク管理を整える必要性は広がっている。
一方、業務プロセスへの組み込み率、ルールの実効性、効果測定の標準化はまだ比較できていないため、`commoditized`とは判定しない。

## 利用上の注意

**効果未確認**: 対象事業者で生成AIを使う業務がある場合は、まず文書要約や情報検索など一つの低リスク業務を対象に、入力禁止情報、
確認者、利用ログ、処理時間、手戻り、品質評価を決めて試行する。その後、部署プロセスへ広げる前に、誤出力・権利・情報管理の
レビューを行う。外部資料では現時点でこのpracticeを試す業務運用がないため、効果の主張は置かない。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
