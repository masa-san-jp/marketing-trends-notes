---
id: trend/foodservice-demand-recovery
uri: urn:mtn:trend/foodservice-demand-recovery
type: trend
kind: demand-shift
stage: growing
market: food-beverage
geo: japan
label_ja: 外食・飲食サービス需要の回復
label_en: Recovery of foodservice demand
authority:
  wikidata: null
  none_reason: "「外食・飲食サービス需要の回復」「foodservice demand recovery Japan」で検索したが、この日本の飲食サービス需要の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2022~"
  end: ".."
  display: "コロナ禍後に飲食店・飲食サービス業が上昇し、フード・ビジネス全体が3年連続で上昇した局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 飲食店・飲食サービス業の回復と単価上昇
  note: "「外食・飲食サービス需要の回復」は、経済産業省のフード・ビジネス指数分析を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.meti.go.jp/statistics/toppage/report/archive/kako/20250722_1.html", certainty: independent, retrieved: primary, as_of: "2024", tense: completed}
  - {field: stage, source: "https://www.meti.go.jp/statistics/toppage/report/archive/kako/20250722_1.html", certainty: independent, retrieved: primary, as_of: "2022-2024", tense: completed}
  - {field: time, source: "https://www.meti.go.jp/statistics/toppage/report/archive/kako/20250722_1.html", certainty: independent, retrieved: primary, as_of: "2022-2024", tense: completed}
  - {field: prediction, source: "https://www.meti.go.jp/statistics/toppage/report/archive/kako/20260527_1.html", certainty: independent, retrieved: primary, as_of: "2025", tense: completed}
  - {field: current-status, source: "https://www.fuji-keizai.co.jp/press/detail.html?cid=25077&la=ja&la=ja", certainty: vendor, retrieved: primary, as_of: "2025", tense: intended}
predictions:
  - {claim: "2025年のフード・ビジネス指数が2024年の96.3を下回らない", by: "2027-12", resolved: "2026-08-12", outcome: miss}
  - {claim: "富士経済の予測どおり、2026年の外食産業国内市場規模が2019年実績（26兆2,687億円）を上回る", by: "2027-06", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    店舗、テイクアウト、配達、予約、外食モール、インバウンド、ファーストフード、レストラン、居酒屋など複数の接点がある。業態別の来店・注文経路の因果は未確認である。
channels: []
relations: []
sources:
  - https://www.meti.go.jp/statistics/toppage/report/archive/kako/20250722_1.html
  - https://www.meti.go.jp/statistics/toppage/report/archive/kako/20260527_1.html
status: verified
updated: 2026-09-20
---

# 外食・飲食サービス需要の回復

## 見出している未来（何に向かって動いているか）

外食産業の市場規模は、コロナ禍前の水準を2026年に上回るとの見通しが示されている。富士経済
「外食産業マーケティング便覧2025 総市場分析編」（2025年2〜7月に13カテゴリー118業態を
調査）は、2025年の外食産業国内市場が35兆7,116億円の見込みで、コロナ禍前の2019年の規模
（26兆2,687億円、既存の足元の根拠参照）に近づき、「2026年には上回る」と予測している。
背景として、インバウンド需要の高さとアイドルタイム（客足の少ない時間帯）の需要開拓が挙げ
られている。

これは富士経済という市場調査会社自身の予測であり（`vendor`）、既存の足元の根拠にある
フード・ビジネス指数（FBI、経済産業省の独立集計）とは異なる調査・定義に基づく。FBIは
2025年に94.1へ低下（4年ぶりの低下、predictions参照）しており、富士経済の楽観的な予測と
経産省の実績指数の間には方向性の違いがある点に注意が必要である。

## 足元の根拠（完了した事実）

飲食店・飲食サービス業を含むフード・ビジネスが、コロナ禍の落ち込みから回復した後の高水準にある。経済産業省の2025年分析では、フード・ビジネス指数（FBI）は94.1で前年比2.3％低下し、4年ぶりの低下となった。2024年の96.3を下回ったため、「2025年も96.3以上」という予測はmissと判定した。一方、飲食店・飲食サービス業は上昇しており、食料品流通業・食料品工業の低下と動きが分かれている。

分析では、食堂・レストラン・専門店、パブ・居酒屋、ファーストフードなど業態による寄与が異なり、インバウンド需要や物価上昇も影響している。指数上昇を実質的な来店者数の増加や全業態の繁盛と同一視しない。

## kind と stage の判定

**kind: demand-shift とした。** 変化しているのは飲食サービスの活動指数と売上・需要の結果であり、特定店舗の広告施策ではない。

**stage: growing とした。** 2022年以降の回復を経て、2024年までFBIが3年連続で上昇したためである。ただし、価格上昇と客数の寄与、業態・地域差が残るため、実利用が一方向に増えたとは判定しない。

## 時間

同じ分析で回復と2024年の上昇が確認できる2022年以降を `2022~` とした。終点は `..`（継続中）。

## チャネルと伝播

店舗、テイクアウト、配達、予約、外食モール、インバウンド、ファーストフード、レストラン、居酒屋など複数の接点がある。業態別の来店・注文経路の因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 次回の同じ指数でFBIが低下し、飲食店・飲食サービス業も複数業態で下落する
- 指数上昇が物価・客単価だけで、来店者数、注文数、稼働店舗が増えていないと分かる
- インバウンドや一部業態を除くと、外食・飲食サービスの回復が再現されない

## 未着手

- 2026年9月20日、富士経済のプレスリリースを実読して見出している未来を追記した。FBI（経産省・独立集計）が2025年に低下した一方、富士経済（vendor・別定義）は2025年拡大・2026年コロナ前超えを予測しており、両者の乖離の理由（対象範囲・算出方法の違い）はまだ確認できていない
- 客数、客単価、店舗数、業態、地域、価格要因を分解する
- 店舗、テイクアウト、配達、予約、外食ECの利用経路を同じ期間で比較する
- 2025年の指数で予測を答え合わせし、94.1（96.3未満）のmissを記録した
