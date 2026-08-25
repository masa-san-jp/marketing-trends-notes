---
id: trend/building-renovation-market-expansion
uri: urn:mtn:trend/building-renovation-market-expansion
type: trend
kind: demand-shift
stage: growing
market: consumer-goods
geo: japan
label_ja: 建築物リフォーム・リニューアル需要の拡大
label_en: Expansion of building renovation and renewal demand
authority:
  wikidata: null
  none_reason: "「建築物リフォーム・リニューアル需要の拡大」「building renovation market expansion in Japan」で検索したが、日本の建築物リフォーム受注の変化そのもののWikidata項目は確認できない"
time:
  start: "2020~"
  end: ".."
  display: "新築だけでなく、建築物の改装・改修・維持・修理への受注が拡大する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 建築物リフォーム・リニューアル工事受注高の増加
  note: "「建築物リフォーム・リニューアル需要の拡大」は、国土交通省の受注高調査を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-11-12"
evidence:
  - {field: kind, source: "https://www.mlit.go.jp/report/press/joho04_hh_001375.html", certainty: independent, retrieved: primary, as_of: "2025年度"}
  - {field: stage, source: "https://www.mlit.go.jp/report/press/content/002005995.pdf", certainty: independent, retrieved: primary, as_of: "2024-2025年度"}
  - {field: time, source: "https://www.mlit.go.jp/report/press/joho04_hh_001375.html", certainty: independent, retrieved: primary, as_of: "2008-2025年度"}
predictions:
  - {claim: "次回公表される建築物リフォーム・リニューアル工事の合計受注高が2025年度の16兆4,104億円を下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    リフォーム会社、工務店、管理組合、住宅設備、ホームセンター、金融・補助制度、賃貸管理、建物管理を通じて、建築ストックと消費財・サービスへ伝わる。受注増が個人の可処分所得や住み替え意向をどう変えるかは未確認である。
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/report/press/joho04_hh_001375.html
  - https://www.mlit.go.jp/report/press/content/002005995.pdf
status: verified
updated: 2026-08-12
---

# 建築物リフォーム・リニューアル需要の拡大

## 何が変わったか

建築物への支出が新築だけでなく、改装・改修、維持・修理、設備更新へ広がっている。国土交通省の2025年度調査では、建築物リフォーム・リニューアル工事の合計受注高は16兆4,104億円で、前年度比18.7％増だった。住宅は4兆9,033億円、非住宅建築物は11兆5,071億円で、住宅の改装・改修工事は3兆8,164億円だった。

この調査は建設業許可業者5,000者を対象にした復元集計で、元請工事が中心である。受注高の増加は、建物所有者の満足度、居住性、賃料、エネルギー効率、工事利益が同時に改善したことを意味しない。

## kind と stage の判定

**kind: demand-shift とした。** 建物のストック更新、設備老朽化、用途変更などから改修需要が増える変化を観測しており、単一企業の技術導入ではないためである。

**stage: growing とした。** 2025年度の受注高が前年度を大きく上回り、住宅・非住宅の双方で改装・改修や維持・修理が観測されるためである。ただし、受注高だけでは持続的な市場成長や案件の採算は判断できない。

## 時間

国土交通省の調査が2008年度から実施されており、直近の比較可能な局面を追うため `2020~` を始点とした。終点は `..`（継続中）。

## チャネルと伝播

リフォーム会社、工務店、管理組合、住宅設備、ホームセンター、金融・補助制度、賃貸管理、建物管理を通じて、建築ストックと消費財・サービスへ伝わる。受注増が個人の可処分所得や住み替え意向をどう変えるかは未確認である。

## 反証（これが偽なら何が観測されるか）

- リフォーム需要の拡大が続くなら、受注高が複数年度連続して縮小することはないはず
- 受注高の増加が実需を表すなら、工事件数、設備更新、所有者・管理組合の発注にも同方向の変化が現れるはず
- 改修需要が事業機会になるなら、工事単価だけでなく、完工、再工事、顧客満足、エネルギー性能も改善するはず

## 未着手

- 住宅・非住宅、工事種類、発注者、用途、地域別に受注高を分解する
- 工事単価、工期、完工率、再工事、設備性能、補助制度の影響を接続する
- 次回の建築物リフォーム・リニューアル調査で予測を答え合わせする
