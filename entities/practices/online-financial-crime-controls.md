---
id: practice/online-financial-crime-controls
uri: urn:mtn:practice/online-financial-crime-controls
type: practice
label_ja: オンライン金融取引の本人確認・異常検知・顧客通知・被害対応
label_en: Integrated identity verification, anomaly detection, customer alerts, and incident response for online finance
authority:
  wikidata: null
  none_reason: "Wikidataで「オンライン金融取引の本人確認・異常検知・顧客通知・被害対応」「integrated online financial crime controls」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2023~"
  end: ".."
  display: "フィッシング・不正送金・SNS型投資詐欺への対応として、本人確認から異常検知・顧客通知・停止・回復までをつなぐ運用"
saturation: spreading
evidence:
  - {field: time, source: "https://www.fsa.go.jp/news/r6/20250627/01.pdf", certainty: attested, retrieved: primary, as_of: "2025-06-27"}
  - {field: saturation, source: "https://www.fsa.go.jp/news/r7/sonota/20260416/20260416.html", certainty: attested, retrieved: primary, as_of: "2026-04-16"}
channels: []
relations:
  - {type: responds_to, target: trend/online-financial-crime-governance, certainty: hypothesis, source: "https://www.fsa.go.jp/news/r7/sonota/20260416/20260416.html"}
sources:
  - https://www.fsa.go.jp/news/r6/20250627/01.pdf
  - https://www.fsa.go.jp/news/r7/sonota/20260416/20260416.html
  - https://www.fsa.go.jp/news/r7/ginkou/20260630.html
  - https://www.npa.go.jp/bureau/safetylife/sos47/new-topics/260213/03.html
status: draft
updated: 2026-08-11
---

# オンライン金融取引の本人確認・異常検知・顧客通知・被害対応

## 何をするか

オンライン口座の開設、ログイン、端末変更、送金先登録、高額・普段と異なる取引を、同じ本人確認の強さで処理しない。取引のリスクに応じて
追加認証や顧客確認を行い、認証情報の窃取だけで送金まで進まないようにする。金融庁が金融機関に求めている強固な認証、なりすましサイト・
メール対策、疑わしい取引の検知、取引限度額、顧客への警告・確認を、次の運用表にまとめる。

- 本人確認・認証: 新規口座、端末・連絡先変更、送金先登録、初回・高リスク取引ごとに必要な確認方法と追加認証を定義する
- 異常検知: 金額、時間帯、端末、接続元、送金先登録直後の取引、過去の利用パターンなどから要確認の条件を定義し、判定理由を記録する
- 顧客通知・確認: 検知時に、攻撃を受けているチャネルとは別の確認手段を含め、顧客が取引を止めたり正当性を確認したりできる通知を行う
- 被害対応: 取引の一時停止、口座の凍結・解約、追加認証、金融機関・警察との情報共有、顧客への説明、回復・補償判断を一つのケース記録で追う

検知モデルやルールを導入するだけで終わらせず、検知から顧客確認、停止・凍結、調査、回復までの責任者・期限・エスカレーション先を決める。
正常な顧客の取引を過度に止めないため、検知率だけでなく、誤検知率、顧客確認の完了率、検知から停止までの時間、回復・補償の結果、相談・
苦情を同じ定義で記録する。

## どのトレンドへの応答か

[trend/online-financial-crime-governance](../trends/online-financial-crime-governance.md)（オンライン金融犯罪対策の高度化）への応答とみる。
金融庁は、インターネットバンキングの不正送金等をめぐり、強固な認証、なりすまし対策、異常取引の検知、取引限度額、顧客への注意喚起、
金融機関間の情報共有などの強化を求めている。これらを顧客接点と被害対応までつなぐ実装単位として整理したpracticeである。

ただし、このpracticeを導入すれば不正送金や詐欺被害、誤検知、顧客負担が減るとは確認していない。trendへの応答関係も、制度上の要請と運用上の
必要性から置いた**私の仮説**（`certainty: hypothesis`）である。

## 効いた条件・効かない条件

**未実施**（自分の事業で金融口座、送金、決済、不正検知、顧客通知を運用していない）。金融機関別の導入率、検知精度、被害抑止額、停止までの
時間、顧客確認の完了率、誤検知、補償・回復の結果は測っていない。

成立条件は、本人確認と取引監視の責任者が分断されていないこと、検知理由を調査できるログが残ること、顧客が安全に確認できる連絡経路があること、
停止・凍結・情報共有を実行できる権限と連絡網があること、誤検知を解除し顧客に説明できること、そして検知から回復までの指標を同じ定義で追える
ことである。多要素認証だけを追加する、または警告メールを送るだけでは、このpracticeの実装とはみなさない。

**未確認**: 金融機関・サービス別の導入率、本人確認方式ごとの不正抑止効果、ルール・モデル別の精度、顧客通知から停止までの時間、誤検知による
利用停止・問い合わせ、金融機関間の情報共有による回復率。

## 飽和度の判定

`spreading` とした。金融庁の要請・モニタリング、金融機関の対策資料、警察・業界の啓発があり、本人確認、異常検知、顧客通知、口座停止・
情報共有を組み合わせた運用を設計する材料は整備されている。一方、金融機関横断の採用率、運用品質、誤検知と顧客負担、被害抑止・回復の実績は
比較できていないため、`commoditized`とは判定しない。

## 自分の事業にどう使うか

**未実施。** 金融取引を扱う事業で試す場合は、まず一つの取引フローに限定し、口座開設・ログイン・送金先登録・送金・顧客通知・停止・回復の状態遷移を
記録する。正常系と不正疑いのケースを分け、検知から顧客確認・停止までの時間、誤検知、問い合わせ、回復・補償の判断を測定する。自社には現時点で
このpracticeを試す金融サービスがないため、効果の主張は置かない。
