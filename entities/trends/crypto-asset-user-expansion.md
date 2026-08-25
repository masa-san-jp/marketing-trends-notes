---
id: trend/crypto-asset-user-expansion
uri: urn:mtn:trend/crypto-asset-user-expansion
type: trend
kind: demand-shift
stage: growing
market: finance
geo: japan
label_ja: 暗号資産利用者の拡大
label_en: Expansion of crypto-asset users
authority:
  wikidata: null
  none_reason: "「暗号資産利用者の拡大」「crypto-asset user expansion Japan」で検索したが、日本の口座数・取引規模の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2020~"
  end: ".."
  display: "国内の暗号資産口座数・取引規模が拡大し、利用者保護の制度論点が再整理される局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 暗号資産の国内口座数・取引規模の拡大
  note: "「暗号資産利用者の拡大」は、金融庁の金融審議会議事録に示された国内口座数・取引金額を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.fsa.go.jp/singi/kessaiseido_wg/gijiroku/20240925.html", certainty: independent, retrieved: primary, as_of: "2024-06"}
  - {field: stage, source: "https://www.fsa.go.jp/singi/kessaiseido_wg/gijiroku/20240925.html", certainty: independent, retrieved: primary, as_of: "2024-06-2024-08"}
  - {field: time, source: "https://www.fsa.go.jp/singi/kessaiseido_wg/gijiroku/20240925.html", certainty: independent, retrieved: primary, as_of: "2020-2024"}
predictions:
  - {claim: "次回の金融庁または業界横断の公的資料で、国内暗号資産口座数が2024年6月の約1,040万口座を下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    暗号資産交換業者、アプリ、取引所、ウォレット、広告・SNS、銀行・決済との接続を通じて広がる。利用開始と継続、投資勧誘、詐欺被害の経路は同じではないため、チャネル別の因果は未確認である。
channels: []
relations: []
sources:
  - https://www.fsa.go.jp/singi/kessaiseido_wg/gijiroku/20240925.html
status: verified
updated: 2026-08-11
---

# 暗号資産利用者の拡大

## 何が変わったか

国内の暗号資産取引は、限られた投資家向けの論点から、口座数・取引規模・事業者保護を含む金融サービスの利用論点へ広がっている。金融庁の金融審議会議事録では、2024年6月時点の国内取引金額は約1.6兆円、国内口座数は約1,040万口座、2024年8月末の暗号資産交換業者は29業者で、利用者が拡大している状況と説明されている。

一方、価格変動、詐欺、破綻時の利用者財産、海外流出、ステーブルコインとの関係など保護上の論点も同時に議論されている。口座数を実利用者数や利益獲得者数と同一視せず、口座・取引・保有・被害を分けて見る必要がある。

## kind と stage の判定

**kind: demand-shift とした。** 金融庁が示すのは、国内口座数と取引金額という利用側の変化であり、交換業者の広告費や特定商品の販売実績ではない。

**stage: growing とした。** 口座数・取引規模が大きくなり、利用者保護を含む制度検討の対象になっているためである。ただし、価格変動と利用頻度、口座保有者の継続利用は分解できていない。

## 時間

金融庁の議事録で2020年以降の市場拡大と2024年の口座・取引指標を確認できるため `2020~` とした。終点は `..`（継続中）。

## チャネルと伝播

暗号資産交換業者、アプリ、取引所、ウォレット、広告・SNS、銀行・決済との接続を通じて広がる。利用開始と継続、投資勧誘、詐欺被害の経路は同じではないため、チャネル別の因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 次回以降の公的資料で口座数・取引金額・交換業者数が複数指標で縮小する
- 口座数が増えても休眠口座が大半で、継続利用や取引参加者数が増えていないと分かる
- 利用者保護の制度論点が縮小し、暗号資産が金融サービスとして継続的に扱われなくなる

## 未着手

- 口座数、稼働口座、取引金額、保有額、年代、被害相談を同じ定義で比較する
- 暗号資産、ステーブルコイン、電子決済手段、投資商品の利用を分ける
- 次回の公的資料で予測を答え合わせする
