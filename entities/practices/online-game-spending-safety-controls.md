---
id: practice/online-game-spending-safety-controls
uri: urn:mtn:practice/online-game-spending-safety-controls
type: practice
label_ja: オンラインゲームの年齢・課金・相談安全運用
label_en: Age, spending, and support safety operations for online games
authority:
  wikidata: null
  none_reason: "Wikidataで「オンラインゲームの年齢・課金・相談安全運用」「online-game age spending support safety operations」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2022~"
  end: ".."
  display: "オンラインゲームの配信・課金・未成年者保護・相談・返金をつなぐ運用"
saturation: spreading
evidence:
  - {field: time, source: "https://www.caa.go.jp/notice/entry/029257/", certainty: independent, retrieved: primary, as_of: "2022-06-29"}
  - {field: saturation, source: "https://www.caa.go.jp/policies/policy/consumer_policy/caution/caution_022", certainty: attested, retrieved: primary, as_of: "2026-08-11"}
channels: []
relations:
  - {type: responds_to, target: trend/online-game-spending-protection, certainty: hypothesis, source: "https://www.caa.go.jp/policies/policy/consumer_policy/caution/caution_022"}
sources:
  - https://www.caa.go.jp/policies/policy/consumer_policy/caution/caution_022
  - https://www.caa.go.jp/policies/policy/consumer_policy/caution/internet/trouble/online.html
  - https://www.caa.go.jp/notice/entry/029257/
  - https://www.kportal.caa.go.jp/teaching-material/001514/
status: draft
updated: 2026-08-11
---

# オンラインゲームの年齢・課金・相談安全運用

## 何をするか

ゲームごとに対象年齢、年齢確認、無料と有料の境界、ゲーム内通貨・アイテムの価格と換算、購入確認、保護者承認、支出上限、利用履歴、
返金・利用停止・相談窓口を一覧化する。未成年者向けには、登録情報を正しく入力すること、保護者への確認、端末・決済アカウントの管理を説明し、
高額購入、短時間の連続購入、年齢不一致、チャージバック、問い合わせを検知したときの確認・停止・支援の手順を決める。

消費者庁は、無料のはずのゲームで高額請求が発生すること、子どもが知らない間に課金すること、年齢を偽って利用できる事例を注意喚起している。
また、課金トラブルの相談対応マニュアルでは、事実関係の聞き取り、事業者への返金交渉、ゲームへののめり込みや家庭・精神保健福祉の相談が整理されている。
このpracticeでは、課金を増やす施策と安全運用を分け、利用者が支出と相談先を理解できる表示・記録を持つ。

## どのトレンドへの応答か

[trend/online-game-spending-protection](../trends/online-game-spending-protection.md)（オンラインゲーム課金・未成年者保護の運用強化）への応答とみる。
デジタル課金と未成年者の利用が広がるほど、年齢・決済・表示・保護者承認・相談・返金を個別の窓口に分けず、一つの安全運用として管理する必要があるためである。
ただし、このpracticeを導入すれば高額課金、相談、返金、離脱、顧客満足が改善するとは確認していないため、関係の確度は `hypothesis` とした。

## 効いた条件・効かない条件

**未実施。** 自分の事業でオンラインゲームを配信・運営しておらず、年齢確認、保護者承認、支出上限、課金表示、相談・返金対応を一つの運用で測っていない。
高額課金、誤課金、返金、相談解決時間、継続率、売上、顧客満足への効果は未確認である。

成立条件は、ゲーム・決済・顧客サポート・法務・未成年者対応の責任者が決まっていること、購入前後の表示と履歴を確認できること、本人・保護者からの相談を
受けられること、停止・返金・消費生活センターへの案内を含むエスカレーションがあることである。保護者承認の画面だけを置き、年齢不一致や課金履歴、相談後の対応を
確認しなければ、安全運用とはみなさない。

**未確認**: ゲーム・プラットフォーム別の実装率、課金表示の理解度、年齢・保護者確認の通過率、支出上限の利用率、高額課金・返金・相談の発生率と解決時間、
安全施策と売上・継続率の関係。

## 飽和度の判定

`spreading` とした。消費者庁の注意喚起、相談対応マニュアル、教育教材、関係機関・業界団体の取組があり、事業者が設計する材料は広がっている。一方、
ゲーム横断の実装率、表示の分かりやすさ、安全指標、返金・相談対応の品質は比較できていないため、標準化された `commoditized` とは判定しない。

## 自分の事業にどう使うか

**未実施。** ゲーム事業で試す場合は、一つのタイトルと決済経路に限定し、対象年齢、無料・有料境界、価格、保護者承認、上限、購入履歴、相談・返金先を確認する。
テスト利用者の課金理解、誤購入、相談、返金、利用停止を記録し、未成年者保護上の不明点が残る場合は配信地域や課金機能を広げない。自社には現時点でこのpracticeを
試すゲーム事業がないため、効果の主張は置かない。
