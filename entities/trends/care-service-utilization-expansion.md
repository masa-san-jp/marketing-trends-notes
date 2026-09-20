---
id: trend/care-service-utilization-expansion
uri: urn:mtn:trend/care-service-utilization-expansion
type: trend
kind: demand-shift
stage: growing
market: health-wellness
geo: japan
label_ja: 介護サービス利用の拡大
label_en: Expansion of long-term care service utilization
authority:
  wikidata: null
  none_reason: "「介護サービス利用の拡大」「long-term care service utilization expansion Japan」で検索したが、日本の介護サービス受給者数・費用の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2020~"
  end: ".."
  display: "介護サービス・介護予防サービスの受給者数と費用額が増加する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 介護サービス受給者数・費用額の増加
  note: "「介護サービス利用の拡大」は、厚生労働省の介護給付費等実態統計を要約する記述的なラベルで、利用者の満足度や供給量を推定するものではない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/kyufu/2026/dl/202602_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "2026-02審査分", tense: completed}
  - {field: stage, source: "https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/kyufu/2026/dl/202602_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "2025-2026-02", tense: completed}
  - {field: time, source: "https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/kyufu/24/index.html", certainty: independent, retrieved: primary, as_of: "2024年度", tense: completed}
  - {field: prediction, source: "https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/kyufu/2026/dl/202603_gaiyou.pdf", certainty: independent, retrieved: primary, as_of: "2026-03審査分", tense: completed}
predictions:
  - {claim: "次回の同統計で介護サービス受給者数が2026年2月審査分の482.86万人を下回らない", by: "2027-12", resolved: "2026-08-12", outcome: miss}
channel_scope:
  status: not-applicable
  note: >-
    在宅介護、訪問、通所、施設、介護予防、ケアマネジメント、自治体、家族、福祉用具、見守り、オンライン相談など複数の接点がある。利用増加を生む個別の紹介・選択経路は未確認である。
channels: []
relations: []
sources:
  - https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/kyufu/2026/dl/202602_gaiyou.pdf
  - https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/kyufu/2026/dl/202603_gaiyou.pdf
  - https://www.mhlw.go.jp/toukei/saikin/hw/kaigo/kyufu/24/index.html
status: verified
updated: 2026-09-21
---

# 介護サービス利用の拡大

## 見出している未来（何に向かって動いているか）

**未確認**: `docs/sources-directory.md` 層0の出典（内閣府「国民生活に関する世論調査」の調査票・集計表一覧、消費者庁「消費者意識基本調査」、Pantone、Getty Images、Google Trends、SNS空気感ログ）を確認したが、介護サービスの利用者・家族が今後の利用について何を意向・期待しているかを直接示す設問・記述は見つからなかった。厚生労働省の関連ページ（介護人材確保の方針）は職員確保の必要数についての記述であり、利用者側の意向データではない。

## 足元の根拠（完了した事実）

介護サービスの利用者数と費用額が増加し、本人・家族・自治体・事業者が、在宅・通所・施設・予防を組み合わせて生活を支える前提が大きくなっている。厚生労働省の2026年2月審査分では、介護サービス受給者数は482.86万人で前年同月比1.9％増、介護予防サービスは101.22万人で5.1％増だった。介護サービス費用額は9,874.71億円で2.8％増となっている。

2026年3月審査分の介護サービス受給者数は480.09万人で、2月の482.86万人を下回った。このため、次回統計に対する「482.86万人以上」という予測はmissと判定した。ただし、前年同月比では1.9％増であり、単月の低下を長期的な縮小とは解釈しない。

これは高齢者全体の人数やサービス品質、介護事業者の利益を直接表さない。要介護度、サービス種類、地域、供給制約、家族介護、自己負担、利用継続を分けて観測する必要がある。

## kind と stage の判定

**kind: demand-shift とした。** 観測対象は介護サービスの受給者数と費用額という利用結果であり、特定事業者の広告や営業活動ではない。

**stage: growing とした。** 2026年2月審査分で受給者数・費用額が前年同月を上回り、年次・月次の公的統計で継続的に把握されているためである。ただし、費用増には報酬改定・価格・要介護度・サービス構成も含まれる。

## 時間

厚生労働省の年次・月次統計で2020年代の受給者数と費用を追えるため `2020~` とした。終点は `..`（継続中）。

## チャネルと伝播

在宅介護、訪問、通所、施設、介護予防、ケアマネジメント、自治体、家族、福祉用具、見守り、オンライン相談など複数の接点がある。利用増加を生む個別の紹介・選択経路は未確認である。

## 反証（これが偽なら何が観測されるか）

- 次回以降の統計で受給者数・費用額が複数区分で減少する
- 費用額だけ増え、受給者数・利用日数・サービス種類が増えず、制度単価や構成変化だけで説明される
- 地域・要介護度・在宅/施設を分けると、利用拡大が一部の区分に限られる

## 未着手

- 2026年9月21日、層0出典（内閣府世論調査、消費者庁調査、Pantone、Getty Images、Google Trends、SNS空気感ログ）を確認したが、介護サービス利用者・家族の今後の利用意向を示す一次資料が見つからず、第一節を`**未確認**:`とした
- 要介護度、サービス種類、在宅・通所・施設、地域、年齢、自己負担を分解する
- 受給者数、利用日数、費用、供給事業所、人手不足、家族介護を接続する
- 2026年3月審査分で予測を答え合わせし、480.09万人（482.86万人未満）のmissを記録した
