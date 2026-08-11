---
id: practice/functional-food-evidence-safety-withdrawal
uri: urn:mtn:practice/functional-food-evidence-safety-withdrawal
type: practice
label_ja: 機能性表示食品の根拠・健康被害情報・撤回管理
label_en: Evidence, adverse-health-information, and withdrawal governance for foods with function claims
authority:
  wikidata: null
  none_reason: "Wikidataで「機能性表示食品の根拠・健康被害情報・撤回管理」「evidence safety withdrawal governance for foods with function claims」を確認したが、この運用の型そのものの項目は確認できない"
time:
  start: "2024~"
  end: ".."
  display: "2024年の制度見直し後、届出前後の根拠・安全情報・表示変更をつなぐ運用"
saturation: spreading
evidence:
  - {field: time, source: "https://www.caa.go.jp/notice/assets/food_labelling_cms_240903_01.pdf", certainty: attested, retrieved: primary, as_of: "2024-08-30"}
channels: []
relations:
  - {type: responds_to, target: trend/functional-food-safety-governance, certainty: hypothesis, source: "https://www.caa.go.jp/notice/entry/038499/"}
sources:
  - https://www.caa.go.jp/policies/policy/food_labeling/foods_with_function_claims
  - https://www.caa.go.jp/notice/assets/food_labelling_cms_240903_01.pdf
  - https://www.caa.go.jp/notice/entry/041585/
  - https://www.caa.go.jp/notice/entry/043728/
status: draft
updated: 2026-08-11
---

# 機能性表示食品の根拠・健康被害情報・撤回管理

## 何をするか

商品・機能性関与成分・表示文言・一日摂取目安量・注意事項・科学的根拠を対応付けた台帳を作り、届出資料、パッケージ、商品ページ、
広告、FAQのどの表現がどの根拠に基づくかを版管理する。販売後は、相談窓口と品質保証をつなぎ、健康被害と疑われる情報を受け付けたら、
医師の診断情報を含む必要な項目を収集し、報告・販売継続・表示変更・回収・撤回の判断を同じ記録に残す。

消費者庁・厚生労働省の説明資料では、機能性表示食品等について、健康被害との因果関係が不明でも対象となり得る情報提供のルールを示し、
重篤事例は1例でも、同じ所見の症例が概ね30日以内に複数発生した場合は、知った日から15日以内の情報提供としている。2025年には、
届出手引き・質疑応答集の掲載と改正も行われた。このpracticeでは、広告審査だけで終わらず、根拠の再確認、健康被害情報、表示変更・
撤回を一つのライフサイクルとして扱う。

## どのトレンドへの応答か

[trend/functional-food-safety-governance](../trends/functional-food-safety-governance.md)（機能性表示食品の安全・表示管理強化）への応答とみる。
制度が、機能性の表示を事業者の責任で行うことに加え、健康被害情報の収集・提供や届出後の管理を求める方向へ変わったためである。
ただし、このpracticeを導入すれば健康被害、表示違反、回収費用、消費者不信が減るとは確認していないため、関係の確度は`hypothesis`とした。

## 効いた条件・効かない条件

**未実施**（自分の事業で機能性表示食品の届出、品質保証、健康被害情報の報告、撤回判断を運用していない）。根拠台帳の更新率、相談から
報告までの時間、表示変更・撤回の判断時間、回収量、顧客反応、安全性への効果は測っていない。

成立条件は、表示文言と根拠資料を商品単位で追跡できること、薬事・品質・法務・顧客対応の責任者と判断期限が決まっていること、相談を
医療・品質情報へ引き上げる窓口があること、ロット追跡・販売停止・回収・撤回の権限と記録があることである。広告表現だけを審査しても、
販売後の健康被害情報や根拠の更新を管理できなければ、このpracticeの実装とはみなせない。

**未確認**: 事業者の導入率、商品カテゴリ別の根拠再検証率、健康被害情報の受付から報告までの時間、表示変更・撤回の発生率、導入前後の
回収費用・消費者相談・信頼指標。

## 飽和度の判定

`spreading` とした。健康被害情報提供の資料、届出手引き、質疑応答集、届出データベースなど、事業者が管理運用を設計するための材料は
整備されている。一方、企業横断の採用率、運用品質、報告の速さ、表示変更・撤回の実効性は比較できていないため、`commoditized`とは判定しない。

## 自分の事業にどう使うか

**未実施。** 機能性を表示する食品を扱う場合は、まず一商品について表示文言・科学的根拠・注意事項・相談窓口・ロット・販売先を台帳化し、
相談受付から品質判断、行政への情報提供、販売停止・表示変更・撤回までの連絡経路を机上で確認する。自社には現時点でこのpracticeを試す
食品事業がないため、効果の主張は置かない。
