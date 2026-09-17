---
id: trend/video-distribution-expansion
uri: urn:mtn:trend/video-distribution-expansion
type: trend
kind: tech-enabled
stage: growing
market: entertainment-content
geo: japan
label_ja: 映像配信市場の拡大
label_en: Expansion of video distribution
authority:
  wikidata: null
  none_reason: "「映像配信市場の拡大」「video distribution market Japan」で検索したが、日本の映像配信市場の構造変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2016~"
  end: ".."
  display: "SVOD・TVOD・EST・AVOD等の映像配信市場が拡大する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 映像作品配信市場の拡大
  note: "「映像配信市場の拡大」は、文化庁の審議会で示された配信市場の時系列を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2021", tense: completed}
  - {field: stage, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2016-2021", tense: completed}
  - {field: time, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2016-2021", tense: completed}
  - {field: current-status, source: "https://ictr.co.jp/report/20250423.html/", certainty: vendor, retrieved: primary, as_of: "2025-04-23", tense: intended}
predictions:
  - {claim: "次回の公的なコンテンツ市場調査で、映像配信市場規模が2021年の約4,230億円を下回らない", by: "2028-12", resolved: null, outcome: null}
  - {claim: "ICT総研の次回同種調査で、有料動画配信サービス利用者数が2027年予測値（4,120万人）に向けて増加を続け、2026年時点で2024年末実績（3,450万人）を下回らない", by: "2027-06", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    定額配信、都度課金、買い切り、広告型配信、動画共有プラットフォーム、スマートフォン、テレビ接続機器などを通じて広がる。資料は個別サービスが需要を発生させた因果を特定していない。
channels: []
relations: []
sources:
  - https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/
  - https://ictr.co.jp/report/20250423.html/
status: verified
updated: 2026-09-17
---

# 映像配信市場の拡大

## 見出している未来（何に向かって動いているか）

有料動画配信サービスの利用者数は、今後も増加を続けると見込まれている。株式会社ICT総研が
2025年4月23日に発表した「2025年有料動画配信サービス利用動向に関する調査」では、有料動画
配信サービス利用者数が2020年末の2,630万人から2022年末3,390万人、2024年末3,450万人へ増加
してきた実績を踏まえ、2025年に3,890万人、2027年には4,120万人へ拡大すると予測している。
このうち定額制サービスの利用者は2027年に3,830万人に達する見通しとされている。

これはICT総研という市場調査会社自身の予測であり（`vendor`）、視聴者自身が「今後も契約を
続けたいか」と回答した意向調査ではない。同調査では、無料動画サービスのみを利用する層が
65.2％を占め、動画配信サービスを一切利用しない層も16.0％存在することも報告されている。

## 足元の根拠（完了した事実）

映像作品の視聴・流通が、放送・劇場・パッケージだけでなく、定額配信（SVOD）、都度払い（TVOD）、買い切り型（EST）、広告型（AVOD）などの配信サービスへ広がっている。文化庁の審議会資料では、映像作品の配信市場は2016年の約1,630億円から2021年の約4,230億円へ拡大したと説明されている。

配信の拡大は視聴接点だけでなく、ライセンス期間、独占・非独占、視聴回数等の情報、クリエイターへの対価還元にも影響する。ただし、この時系列は2021年までの市場規模であり、サービス別の利用者数・継続率・収益性や2022年以降の同一定義の規模は未確認である。

## kind と stage の判定

**kind: tech-enabled とした。** インターネット配信と視聴・課金技術がなければ成立しない市場構造の変化であり、配信形態そのものが先行条件になるためである。

**stage: growing とした。** 2016年から2021年に市場規模が約2.6倍となり、文化庁の2023年審議でも配信市場は増加傾向として扱われている。ただし、配信事業者・作品・料金モデルごとの成熟度は異なる。

## 時間

同じ資料で比較できる2016年から `2016~` とした。終点は `..`（継続中）。

## チャネルと伝播

定額配信、都度課金、買い切り、広告型配信、動画共有プラットフォーム、スマートフォン、テレビ接続機器などを通じて広がる。資料は個別サービスが需要を発生させた因果を特定していない。

## 反証（これが偽なら何が観測されるか）

- 次回の同一定義の市場統計で配信市場規模が縮小し、利用者・視聴時間・売上の複数指標が同時に低下する
- 配信サービスが増えても、作品の視聴・課金・継続が増えず、既存市場の付け替えにとどまる
- クリエイターへの対価、視聴データ、ライセンス取引が配信拡大に伴って整備されない

## 未着手

- 2026年9月17日、ICT総研の2025年調査プレスリリースを実読して見出している未来を追記した。視聴者自身の継続利用意向を直接問う調査は今回探せていない
- SVOD、TVOD、EST、AVOD、UGCを分けた市場規模・利用者・継続率を確認する
- 作品ジャンル、年齢、デバイス、配信経路別に視聴・課金を比較する
- 2022年以降の同一定義の公的または独立調査で予測を答え合わせする
- ICT総研の2027年予測（4,120万人）に対する進捗を、次回以降の同種調査で確認する
