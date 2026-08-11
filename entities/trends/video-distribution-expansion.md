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
  - {field: kind, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2021"}
  - {field: stage, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2016-2021"}
  - {field: time, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2016-2021"}
predictions:
  - {claim: "次回の公的なコンテンツ市場調査で、映像配信市場規模が2021年の約4,230億円を下回らない", by: "2028-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/
status: verified
updated: 2026-08-11
---

# 映像配信市場の拡大

## 何が変わったか

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

- SVOD、TVOD、EST、AVOD、UGCを分けた市場規模・利用者・継続率を確認する
- 作品ジャンル、年齢、デバイス、配信経路別に視聴・課金を比較する
- 2022年以降の同一定義の公的または独立調査で予測を答え合わせする
