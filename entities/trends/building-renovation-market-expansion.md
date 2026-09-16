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
  - {field: kind, source: "https://www.mlit.go.jp/report/press/joho04_hh_001375.html", certainty: independent, retrieved: primary, as_of: "2025年度", tense: completed}
  - {field: stage, source: "https://www.mlit.go.jp/report/press/content/002005995.pdf", certainty: independent, retrieved: primary, as_of: "2024-2025年度", tense: completed}
  - {field: time, source: "https://www.mlit.go.jp/report/press/joho04_hh_001375.html", certainty: independent, retrieved: primary, as_of: "2008-2025年度", tense: completed}
  - {field: current-status, source: "https://j-reform.com/publish/pdf/jitsurei-R7-c.pdf", certainty: independent, retrieved: primary, as_of: "2025", tense: intended}
predictions:
  - {claim: "次回公表される建築物リフォーム・リニューアル工事の合計受注高が2025年度の16兆4,104億円を下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "住宅リフォーム推進協議会の次回（第18回）検討者調査で、リフォーム予定時期を「1年以内」と回答する割合が今回調査の水準を大きく下回らない", by: "2027-03", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    リフォーム会社、工務店、管理組合、住宅設備、ホームセンター、金融・補助制度、賃貸管理、建物管理を通じて、建築ストックと消費財・サービスへ伝わる。受注増が個人の可処分所得や住み替え意向をどう変えるかは未確認である。
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/report/press/joho04_hh_001375.html
  - https://www.mlit.go.jp/report/press/content/002005995.pdf
  - https://j-reform.com/publish/pdf/jitsurei-R7-c.pdf
status: verified
updated: 2026-09-16
---

# 建築物リフォーム・リニューアル需要の拡大

## 見出している未来（何に向かって動いているか）

リフォームを検討している人（潜在需要者）は、実施をより早い時期に前倒しし、省エネ性能の向上を目的に据える方向へ動いている。住宅リフォーム推進協議会の「2025年度住宅リフォームに関する消費者（検討者・実施者）実態調査報告書」（2026年2月公表、検討者調査は直近3年以内にリフォームを計画しているユーザーが対象・第17回）では、検討者の「リフォーム予定時期」について、前年度と比較して「1年以内」と回答した割合が0.7ポイント上昇したと報告されている。また、「リフォームで実現したいこと」を尋ねた設問では、過去にリフォームを実施した人が最も多く挙げた「一部の部屋の全面改修」とは異なり、検討者（今後実施を考えている人）が最も多く挙げたのは「省エネ性能を高める」だった。

これは検討者の行動が変わったことを直接示すものではなく、意向段階での変化である。実際の受注高・工事内容にこの意向がどう反映されるかは、次回以降の実施者調査で確認する必要がある。

## 足元の根拠（完了した事実）

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

- 2026年9月16日、住宅リフォーム推進協議会「2025年度住宅リフォームに関する消費者（検討者・実施者）実態調査報告書」を実読して見出している未来を追記した。「リフォーム予定時期」のグラフ部分は列と数値の対応が崩れており、正確な内訳（3ヶ月以内〜3年以内の構成比）は読み取れなかったため、「1年以内が0.7ポイント上昇」という文章記載の事実のみを採用した
- 住宅・非住宅、工事種類、発注者、用途、地域別に受注高を分解する
- 工事単価、工期、完工率、再工事、設備性能、補助制度の影響を接続する
- 次回の建築物リフォーム・リニューアル調査で予測を答え合わせする
- 検討者の「省エネ性能を高めたい」という意向が、実際の工事内容（断熱改修・高効率設備導入等）にどう反映されるかを次回の実施者調査で確認する
