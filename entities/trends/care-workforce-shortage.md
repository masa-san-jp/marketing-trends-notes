---
id: trend/care-workforce-shortage
uri: urn:mtn:trend/care-workforce-shortage
type: trend
kind: demand-shift
stage: growing
market: health-wellness
geo: japan
label_ja: 介護人材の需給ギャップ拡大
label_en: Expansion of the care-workforce supply gap
authority:
  wikidata: null
  none_reason: "「介護人材の需給ギャップ拡大」「care workforce supply gap in Japan」で検索したが、日本の介護職員必要数と現有人材の差そのもののWikidata項目は確認できない"
time:
  start: "2022~"
  end: ".."
  display: "介護サービス需要に対して必要な職員数が増え、採用・定着・生産性向上を同時に進める局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 介護職員の必要数の増加
  note: "「介護人材の需給ギャップ拡大」は、厚生労働省の第9期介護保険事業計画に基づく必要数推計を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-11-12"
evidence:
  - {field: kind, source: "https://www.mhlw.go.jp/content/12004000/001274765.pdf", certainty: independent, retrieved: primary, as_of: "2022-2040年度"}
  - {field: stage, source: "https://www.mhlw.go.jp/stf/newpage_02977.html", certainty: independent, retrieved: primary, as_of: "2022-2040年度"}
  - {field: time, source: "https://www.mhlw.go.jp/content/12004000/001274765.pdf", certainty: independent, retrieved: primary, as_of: "2022-2040年度"}
predictions:
  - {claim: "2026年度の介護職員必要数が第9期推計の約240万人となり、2022年度の約215万人を上回る", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    介護事業所の採用、入門研修、資格取得、給与・勤務シフト、外国人材、介護ロボット、ICT、家族支援を通じて、介護サービスの供給能力へ伝わる。職員数の増加が利用者のアウトカムを改善する因果は未確認である。
channels: []
relations: []
sources:
  - https://www.mhlw.go.jp/stf/newpage_02977.html
  - https://www.mhlw.go.jp/content/12004000/001274765.pdf
status: verified
updated: 2026-08-12
---

# 介護人材の需給ギャップ拡大

## 何が変わったか

介護サービスの見込み量に対して必要な職員数が増え、利用者数の増加だけでなく、採用、育成、定着、外国人材、業務分担、テクノロジー活用を同時に設計する必要が高まっている。厚生労働省の第9期介護保険事業計画に基づく推計では、介護職員は2022年度の約215万人に対し、2026年度に約240万人、2040年度に約272万人が必要となる。

これはサービス見込み量などに基づく必要数の推計であり、実際の採用可能数、賃金、離職、サービス品質、地域差を直接表すものではない。必要数の増加だけで事業所の不足人数や利用者の待機状況を算定することはできない。

## kind と stage の判定

**kind: demand-shift とした。** 高齢化と介護サービス見込み量に伴う人材需要の変化を観測しており、特定の介護事業者の採用施策ではないためである。

**stage: growing とした。** 必要数が2022年度から2026年度、2040年度へ増える推計となっており、採用・定着・生産性向上の施策が同時に求められているためである。

## 時間

現有人材約215万人と必要数の比較が示される `2022~` を始点とした。終点は `..`（継続中）。

## チャネルと伝播

介護事業所の採用、入門研修、資格取得、給与・勤務シフト、外国人材、介護ロボット、ICT、家族支援を通じて、介護サービスの供給能力へ伝わる。職員数の増加が利用者のアウトカムを改善する因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 介護人材需要の拡大が続くなら、必要数の推計が2026年度・2040年度に向けて縮小することはないはず
- 人材不足が供給制約なら、採用難、離職、サービス休止、待機、賃金、ICT投資にも地域差が現れるはず
- 生産性向上が不足を埋めるなら、職員数だけでなく、一人当たり業務量とサービス品質の改善が観測されるはず

## 未着手

- 必要数、現有人材、求人、採用、離職、賃金、サービス休止を地域・職種別に追う
- 研修、外国人材、業務分担、ICT導入が定着と品質に与える影響を比較する
- 第10期介護保険事業計画で推計と実績を答え合わせする
