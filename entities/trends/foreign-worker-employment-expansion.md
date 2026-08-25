---
id: trend/foreign-worker-employment-expansion
uri: urn:mtn:trend/foreign-worker-employment-expansion
type: trend
kind: demand-shift
stage: growing
market: cross-category
geo: japan
label_ja: 外国人雇用の拡大
label_en: Expansion of foreign-worker employment
authority:
  wikidata: null
  none_reason: "「外国人雇用の拡大」「foreign-worker employment expansion in Japan」で検索したが、日本の外国人雇用届出数の変化そのもののWikidata項目は確認できない"
time:
  start: "2007~"
  end: ".."
  display: "外国人労働者と雇用事業所が過去最多となり、採用・労務・顧客対応の前提を変える局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 外国人労働者数の増加
  note: "「外国人雇用の拡大」は、厚生労働省の外国人雇用状況届出を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-11-12"
evidence:
  - {field: kind, source: "https://www.mhlw.go.jp/stf/newpage_68794.html", certainty: independent, retrieved: primary, as_of: "2025-10"}
  - {field: stage, source: "https://www.mhlw.go.jp/stf/newpage_68794.html", certainty: independent, retrieved: primary, as_of: "2007-2025"}
  - {field: time, source: "https://www.mhlw.go.jp/stf/newpage_68794.html", certainty: independent, retrieved: primary, as_of: "2007-2025"}
predictions:
  - {claim: "次回公表される外国人労働者数が2025年10月末の2,571,037人を下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    求人媒体、職業紹介、在留資格手続、給与・勤怠、翻訳・研修、社内コミュニケーション、店舗・現場接客を通じて、雇用とサービス提供へ伝わる。外国人雇用の増加が消費行動や生産性をどう変えるかは未確認である。
channels: []
relations: []
sources:
  - https://www.mhlw.go.jp/stf/newpage_68794.html
status: verified
updated: 2026-08-12
---

# 外国人雇用の拡大

## 何が変わったか

日本で働く外国人と、外国人を雇用する事業所が増え、採用、在留資格確認、労務管理、教育、現場コミュニケーション、顧客対応を分けずに設計する必要が高まっている。厚生労働省によると、2025年10月末の外国人労働者数は2,571,037人で前年比11.7％増、外国人を雇用する事業所数は371,215所で前年比8.5％増となり、いずれも届出義務化以降で過去最多だった。

在留資格別では専門的・技術的分野が865,588人で前年比20.4％増となった。数値は事業主から提出された届出の集計であり、特別永住者、外交、公用の在留資格は対象外であるため、日本にいる外国人全体や潜在的な採用需要を直接表すものではない。

## kind と stage の判定

**kind: demand-shift とした。** 観測対象は労働力と雇用事業所の構成変化であり、特定の採用サービスや企業の施策ではないためである。

**stage: growing とした。** 労働者数・雇用事業所数が過去最多を更新し、専門的・技術的分野も増えている一方、在留資格、国籍、職種、地域による違いが大きく、均質な市場とはいえないためである。

## 時間

届出制度が義務化された `2007~` を始点とした。終点は `..`（継続中）。

## チャネルと伝播

求人媒体、職業紹介、在留資格手続、給与・勤怠、翻訳・研修、社内コミュニケーション、店舗・現場接客を通じて、雇用とサービス提供へ伝わる。外国人雇用の増加が消費行動や生産性をどう変えるかは未確認である。

## 反証（これが偽なら何が観測されるか）

- 外国人雇用の拡大が続くなら、労働者数と雇用事業所数が複数年同時に減少することはないはず
- 専門人材の増加がサービス設計を変えるなら、職種・在留資格別に採用要件や業務分担の差が現れるはず
- 届出数の増加が実需を反映するなら、求人、在留資格、入職・離職、定着の指標にも同方向の変化が現れるはず

## 未着手

- 国籍、在留資格、職種、地域、企業規模別に雇用の増加を分解する
- 採用、入社後教育、翻訳、勤怠、評価、定着の実務負担を比較する
- 次回の外国人雇用状況届出で予測を答え合わせする
