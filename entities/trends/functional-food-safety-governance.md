---
id: trend/functional-food-safety-governance
uri: urn:mtn:trend/functional-food-safety-governance
type: trend
kind: regulation-driven
stage: growing
market: health-wellness
geo: japan
label_ja: 機能性表示食品の安全・表示管理強化
label_en: Strengthening safety and claims governance for foods with function claims
authority:
  wikidata: null
  none_reason: "Wikidataで「機能性表示食品の安全・表示管理強化」「safety and claims governance for foods with function claims」を確認したが、この制度対応の変化そのものの項目は確認できない"
time:
  start: "2024~"
  end: ".."
  display: "紅麹関連事案を受けた2024年以降の制度見直し"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 機能性表示食品の制度見直し
  note: "消費者が自称する呼称ではなく、消費者庁の制度改正・届出管理の動きをこのKBでまとめた名称"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.caa.go.jp/notice/entry/038499/", certainty: attested, retrieved: primary, as_of: "2024-06-27"}
  - {field: time, source: "https://www.caa.go.jp/notice/assets/food_labelling_cms_240903_01.pdf", certainty: attested, retrieved: primary, as_of: "2024-08-30"}
  - {field: stage, source: "https://www.caa.go.jp/notice/entry/043728/", certainty: attested, retrieved: primary, as_of: "2025-10-01"}
channels: []
relations: []
sources:
  - https://www.caa.go.jp/policies/policy/food_labeling/foods_with_function_claims
  - https://www.caa.go.jp/notice/entry/038499/
  - https://www.caa.go.jp/notice/assets/food_labelling_cms_240903_01.pdf
  - https://www.caa.go.jp/notice/entry/041585/
  - https://www.caa.go.jp/notice/entry/043728/
status: verified
updated: 2026-08-11
---

# 機能性表示食品の安全・表示管理強化

## 何が変わったか

機能性表示食品は、事業者の責任で安全性・機能性の科学的根拠などを消費者庁長官に届け出て表示する制度であり、特定保健用食品と
異なり、消費者庁による個別審査を経ない。紅麹関連製品の事案を受け、消費者庁は2024年6月に食品表示基準の改正を諮問し、制度の
信頼性を高める方向で見直しを進めた。

見直しでは、機能性表示食品等の届出者が、健康被害と疑われる情報を因果関係が不明な段階でも収集し、条件に該当する情報を速やかに
都道府県等と消費者庁へ提供する義務が明記された。消費者庁・厚生労働省の説明資料では、重篤事例は1例でも、同じ所見の症例が概ね
30日以内に複数発生した場合は、知った日から15日以内の情報提供としている。2025年3月と10月には、届出手引き・質疑応答集も掲載・
改正された。

この変化は、機能性の訴求文を作るだけでなく、根拠資料の再確認、健康被害情報の収集・報告、表示変更・撤回判断までを含む管理運用を
販売前後の責任として扱う方向である。ただし、制度が強化されたことと、すべての商品の安全性や消費者の信頼が改善したことは分けて
扱う。

## kind と stage の判定

**kind: regulation-driven とした。** 食品表示基準の改正、健康被害情報の提供義務、届出手引きの改正という制度変更が、事業者の表示・
安全管理の条件を直接変えているためである。健康食品市場の需要増や広告手法の変化を直接測ったトレンドとは区別する。

**stage: growing とした。** 2024年の制度見直し方針、2024年の健康被害情報提供ルール、2025年の届出手引きの掲載・改正が続き、制度対応の
対象と実務資料が増えている。一方、商品カテゴリ別の対応率、表示変更・撤回の割合、消費者の信頼回復や購買行動の変化はこの記録だけでは
比較できないため、peakやcommoditizedとは判定しない。

## 時間

始点は紅麹関連事案を受けた食品表示基準改正の諮問が公表された `2024~` とした。これは健康食品一般の始まりではなく、機能性表示食品の
安全・表示管理が制度見直しの対象として明確になった観測時点である。終点は `..`（継続中）。

## チャネルと伝播

特定の広告媒体から広がった変化ではなく、食品表示、商品ページ、届出データベース、品質保証、顧客相談、行政への報告を通じて伝わる
制度対応である。そのため `channels` は張らない。**未確認**: 店頭、EC、定期購入、専門家経由など、消費者が安全・表示管理の変化をどの接点で
認識し、商品選択を変えたか。

## 反証（これが偽なら何が観測されるか）

- 制度見直しが事業者の実務条件を変えていないなら、2025年以降の届出手引き・質疑応答集の改正や健康被害情報の収集・報告体制の更新が続かないはず
- 安全・表示管理の強化が消費者の選択条件に波及しているなら、独立調査で制度理解、表示確認、購入・継続利用、相談行動の変化が確認されるはず
- 表示根拠の管理が実効化しているなら、届出の変更・撤回、表示修正、健康被害情報の報告が、制度変更前後で同じ定義の時系列として追跡できるはず

## 未着手

- 2025年以降の届出データベースで、新規届出・変更・撤回・販売状況更新の件数を同じ定義で確認する
- 事業者が根拠資料の再検証、健康被害情報の収集、表示変更・撤回をどの程度実装しているかを商品カテゴリ別に整理する
- 制度見直し前後で、機能性表示食品に対する消費者の認知、表示確認、信頼、購買・継続利用がどう変わったかを独立調査で確認する
- このtrendに応答するpractice（表示根拠・健康被害情報・撤回判断をつなぐ運用）の採用率と安全・表示上の実績を整理する
