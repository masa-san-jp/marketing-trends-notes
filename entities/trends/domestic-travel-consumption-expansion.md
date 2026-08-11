---
id: trend/domestic-travel-consumption-expansion
uri: urn:mtn:trend/domestic-travel-consumption-expansion
type: trend
kind: demand-shift
stage: growing
market: cross-category
geo: japan
label_ja: 国内旅行消費の拡大
label_en: Expansion of domestic travel consumption
authority:
  wikidata: null
  none_reason: "「国内旅行消費の拡大」「domestic travel consumption expansion」で検索したが、この現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2022~"
  end: ".."
  display: 2022年以降の国内旅行消費額の回復・拡大局面
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 日本人の国内旅行消費額の増加
  note: "「国内旅行消費の拡大」は、観光庁の旅行・観光消費動向調査を要約するための記述的なラベル。旅行者の自称ではない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mlit.go.jp/kankocho/news02_00074.html", certainty: independent, retrieved: primary, as_of: "2025"}
  - {field: stage, source: "https://www.mlit.go.jp/kankocho/content/001981888.pdf", certainty: independent, retrieved: primary, as_of: "2025"}
  - {field: time, source: "https://www.mlit.go.jp/kankocho/content/001981888.pdf", certainty: independent, retrieved: primary, as_of: "2016-2025"}
predictions:
  - {claim: "2026年の日本人国内旅行消費額が2025年の26兆7,746億円を下回らない", by: "2027-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/kankocho/news02_00074.html
  - https://www.mlit.go.jp/kankocho/content/001981888.pdf
status: verified
updated: 2026-08-11
---

# 国内旅行消費の拡大

## 何が変わったか

日本人の国内旅行に使われる金額が、2022年以降の回復局面を経て拡大している。
観光庁の2025年年間速報では、日本人の国内旅行消費額は26兆7,746億円で前年比6.4％増、延べ旅行者数は5億5,366万人で前年比2.5％増、旅行単価は48,359円で前年比3.8％増だった。消費額と旅行単価は暦年で過去最高とされている。

公表資料の時系列では、国内旅行消費額は2022年17兆1,609億円、2023年21兆9,101億円、2024年25兆1,536億円、2025年26兆7,746億円と増えている。ただし、2025年10-12月期は前年同期比で消費額が減少しており、短期の四半期変動と年間の拡大は分けて読む必要がある。

## kind と stage の判定

**kind: demand-shift とした。** 観光庁の調査は、旅行者数・旅行支出という需要側の変化を測っている。旅行商品の供給量や広告費の増加を直接測ったものではない。

**stage: growing とした。** 2022年から2025年まで年間消費額が増え、2025年は過去最高となったためである。ただし、四半期では減少も観測されており、毎月・毎四半期に一方向で伸びるという意味ではない。

## 時間

コロナ禍後の回復が数値として連続して確認できる2022年から `2022~` とした。終点は `..`（継続中）。

## チャネルと伝播

特定の旅行予約サイトや広告媒体が発生チャネルだとは置かない。宿泊旅行、日帰り旅行、交通、飲食、買物、娯楽などの支出が合算された需要指標である。

## 反証（これが偽なら何が観測されるか）

- 次回の年間調査で国内旅行消費額が26兆7,746億円を下回り、旅行者数と旅行単価も同時に縮小する
- 2025年の過去最高が一時的な価格上昇だけで、実質の旅行回数や旅行者数が中期的に増えていないと判明する
- 宿泊・日帰りの複数区分で支出が減り、全体の増加が一部区分の名目値だけによると分かる

## 未着手

- 旅行目的、地域、宿泊・日帰り、交通・宿泊・飲食・買物の内訳を時系列で分解する
- 価格上昇と旅行回数・旅行者数の寄与を分けて確認する
- 2026年の年間速報で予測を答え合わせする
