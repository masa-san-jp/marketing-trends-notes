---
id: trend/online-medical-consultation-adoption
uri: urn:mtn:trend/online-medical-consultation-adoption
type: trend
kind: regulation-driven
stage: emerging
market: health-wellness
geo: japan
label_ja: オンライン診療の制度対応と利用拡大
label_en: Regulatory normalization and adoption of online medical consultation
authority:
  wikidata: null
  none_reason: "「オンライン診療の制度対応と利用拡大」「online medical consultation adoption」で検索したが、日本の制度・利用変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2024~"
  end: ".."
  display: "2024年度の利用実績と2026年の医療法・指針整備が並行する段階"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: オンライン診療の実施・制度整備
  note: "「オンライン診療の制度対応と利用拡大」は、厚生労働省の制度資料と調査結果をまとめるための記述的なラベル"
freshness:
  valid_as_of: "2026-08-12"
  recheck_by: "2026-09-12"
evidence:
  - {field: kind, source: "https://www.mhlw.go.jp/stf/index_0024_00004.html", certainty: attested, retrieved: primary, as_of: "2026-04-01"}
  - {field: stage, source: "https://www.mhlw.go.jp/stf/shingi2/0000190167_00062.html", certainty: independent, retrieved: primary, as_of: "2024年度"}
  - {field: time, source: "https://www.mhlw.go.jp/stf/shingi2/0000190167_00062.html", certainty: independent, retrieved: primary, as_of: "2024年度-2026-04"}
predictions:
  - {claim: "次回の厚生労働省調査または同等の公的調査で、患者のオンライン診療経験率と医療機関の実施割合が再計測される", by: "2028-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.mhlw.go.jp/stf/index_0024_00004.html
  - https://www.mhlw.go.jp/stf/shingi2/0000190167_00062.html
status: verified
updated: 2026-08-12
---

# オンライン診療の制度対応と利用拡大

## 何が変わったか

オンライン診療は、限定的な利用にとどまりながら、制度と提供体制の整備が続く段階にある。厚生労働省の検討会資料では、2024年度の調査でオンライン診療を受けた経験がある患者は3.5％だった。医療機関側では、外来診療の1割超をオンラインで行う施設が18.6％、5割超の施設が5.4％で、いずれも2年前より増えたと説明されている。

2026年4月1日にはオンライン診療に関する医療法上の規定が施行され、翌4月2日には指針改訂が示された。利用率はまだ小さく、対象となる診療科・患者・地域や調査方法の違いもあるため、医療全体がオンラインへ移行したとは言えない。

厚生労働省は2026年7月23日付で、自治体におけるオンライン診療・遠隔医療の導入事例集（令和8年3月版）を掲載した。制度施行後も自治体導入の事例整理が続いているが、
これは患者の利用率や医療機関の実施割合が増えたことを示す統計ではない。

## kind と stage の判定

**kind: regulation-driven とした。** 利用実績だけなら需要側の変化にも見えるが、2026年の医療法上の規定施行と診療指針の改訂という制度変更が提供条件を直接変えているため、判定表の上位ルールを採った。

**stage: emerging とした。** 患者経験率は3.5％で、医療機関の実施割合にも増加が見られるが、利用は限定的で、診療の適否・安全管理・地域差などの制度運用課題が残る。

## 時間

同じ定義で確認できる2024年度の利用実績と、2026年4月の制度施行を起点に `2024~` とした。終点は `..`（継続中）。

## チャネルと伝播

特定のアプリや広告媒体が発生チャネルだとは置かない。医療機関の予約・診療体制、患者の通院負担、対象疾患、本人確認、通信環境、診療報酬・法令・指針が組み合わさって利用に影響する。

## 反証（これが偽なら何が観測されるか）

- 次回の公的調査で患者の経験率と医療機関の実施割合が増えず、制度施行後も利用が縮小する
- オンライン診療を外来の一定割合で行う医療機関が増えず、制度整備が実務に波及していないと分かる
- 適用範囲や安全管理上の制約により、利用が一部の診療・地域に固定されたままになる

## 未着手

- 診療科、疾患、年齢、地域、医療機関規模ごとの利用差を確認する
- オンライン診療の継続率、対面への切替、患者負担、医療安全の指標を同じ定義で追う
- 2026年施行後の指針運用・監査・事例を一次資料で確認する
