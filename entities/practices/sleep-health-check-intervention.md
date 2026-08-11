---
id: practice/sleep-health-check-intervention
uri: urn:mtn:practice/sleep-health-check-intervention
type: practice
label_ja: 睡眠状態の確認・生活環境改善・相談導線運用
label_en: Sleep assessment, lifestyle-environment improvement, and referral operations
authority:
  wikidata: null
  none_reason: "Wikidataで「睡眠状態の確認・生活環境改善・相談導線運用」「sleep health check intervention operations」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2024~"
  end: ".."
  display: "睡眠・休養を健康づくりの指標として確認し、生活・勤務環境の改善と必要時の専門相談をつなぐ運用"
saturation: spreading
evidence:
  - {field: time, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/suimin/index.html", certainty: attested, retrieved: primary, as_of: "2024-09-18"}
  - {field: saturation, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/kenkounippon21_00006.html", certainty: attested, retrieved: primary, as_of: "2024-08-11"}
channels: []
relations:
  - {type: responds_to, target: trend/sleep-rest-health-management, certainty: hypothesis, source: "https://www.mhlw.go.jp/content/10900000/001603146.pdf"}
sources:
  - https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/suimin/index.html
  - https://www.mhlw.go.jp/content/001305530.pdf
  - https://www.mhlw.go.jp/content/10900000/001603146.pdf
  - https://www.mhlw.go.jp/content/10904750/001222157.pdf
status: draft
updated: 2026-08-11
---

# 睡眠状態の確認・生活環境改善・相談導線運用

## 何をするか

対象者の睡眠による休養感、睡眠時間、就寝・起床時刻、日中の眠気、勤務・育児・学習・生活環境を定期的に確認し、本人が取り組める改善項目を
一つか二つに絞る。照明、騒音、室温、カフェイン、飲酒、運動、勤務間隔、夜間の端末利用など、生活や職場環境の変更可能な条件を記録し、
一定期間後に同じ質問で再確認する。症状が強い、長く続く、事故や健康問題につながる恐れがある場合は、自己管理だけで終わらせず医療・保健の相談先を案内する。

厚生労働省の睡眠ガイドは、健康日本21（第三次）の休養・睡眠分野を推進するため、生活指導者、政策立案者、職場管理者などを対象にしている。
このpracticeでは、睡眠時間だけを増やす目標にせず、休養感、日中の機能、生活・勤務環境、必要時の相談・受診を一つの記録でつなぐ。アプリや
ウェアラブルの数値を診断結果とみなさず、本人の自覚症状と専門家の判断を優先する。

## どのトレンドへの応答か

[trend/sleep-rest-health-management](../trends/sleep-rest-health-management.md)（睡眠・休養の健康管理ニーズの可視化）への応答とみる。
睡眠による休養感や睡眠時間が健康づくりの目標として測定されるほど、啓発だけでなく、個人が実行できる改善、職場・生活環境、必要時の相談を
つなぐ運用が必要になるためである。ただし、このpracticeを導入すれば睡眠、健康、仕事の成果、生活満足度が改善するとは確認していないため、
関係の確度は `hypothesis` とした。

## 効いた条件・効かない条件

**未実施。** 自分の事業で睡眠状態の確認や生活・勤務環境の改善、相談・受診案内を運用していない。休養感、睡眠時間、日中の眠気、欠勤・事故、
生産性、生活満足度への効果は測っていない。

成立条件は、健康情報の取得・利用目的と本人の同意が明確であること、評価項目と頻度が決まっていること、勤務や生活の改善を本人が選べること、
専門家への相談先があること、管理者が個人の睡眠データを人事評価へ直接流用しないことである。睡眠時間のランキングやアプリの数値だけを競わせ、
病気の可能性や個人差を無視する場合は、健康支援の運用とはみなさない。

**未確認**: 継続率、休養感・睡眠時間の改善、日中の眠気・事故・欠勤の変化、勤務環境改善の費用、医療相談への適切な接続率、個人情報管理の負荷。

## 飽和度の判定

`spreading` とした。国の睡眠ガイド、健康づくり支援ツール、職域・自治体向けの普及啓発が整備され、複数の実装接点がある。一方、企業・自治体・
医療・アプリ間で共通の採用率、介入品質、改善効果を比較できていないため、標準化された `commoditized` とは判定しない。

## 自分の事業にどう使うか

**未実施。** 職場やサービスで試す場合は、まず希望者を対象に、休養感、睡眠時間、日中の眠気、勤務・生活環境を匿名または目的限定で確認する。
個人が選ぶ改善策を一つに絞り、4週間程度で同じ指標を再確認し、悪化・長期化・安全上の懸念がある場合の相談先を案内する。自社には現時点でこのpracticeを
試す健康支援運用がないため、効果の主張は置かない。
