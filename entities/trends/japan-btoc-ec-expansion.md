---
id: trend/japan-btoc-ec-expansion
uri: urn:mtn:trend/japan-btoc-ec-expansion
type: trend
kind: demand-shift
stage: growing
market: retail-commerce
geo: japan
label_ja: 国内BtoC-ECの拡大
label_en: Expansion of domestic B2C e-commerce
authority:
  wikidata: null
  none_reason: "「日本 BtoC-EC 市場拡大」「国内電子商取引市場」で検索したが、この現象そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2022~"
  end: ".."
  display: 2022年以降に公表された経年値で拡大を確認できる局面
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: BtoC-EC市場の拡大
  note: "「国内BtoC-ECの拡大」は、経済産業省の市場規模・EC化率の統計を要約するための記述的なラベル。消費者がこの語を自称することは確認していない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.meti.go.jp/press/2025/08/20250826005/20250826005.html", certainty: independent, retrieved: primary, as_of: "2024", tense: completed}
  - {field: stage, source: "https://www.meti.go.jp/press/2025/08/20250826005/20250826005.html", certainty: independent, retrieved: primary, as_of: "2024", tense: completed}
  - {field: time, source: "https://www.meti.go.jp/press/2025/08/20250826005/20250826005.html", certainty: independent, retrieved: primary, as_of: "2024", tense: completed}
  - {field: current-status, source: "https://ecnomikata.com/ecnews/52119/", certainty: anecdotal, retrieved: summary, as_of: "2025", tense: completed}
predictions:
  - {claim: "2025年の国内BtoC-EC市場規模が2024年の26.1兆円を下回らない", by: "2026-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    特定のプラットフォームや媒体が発生チャネルだとは置かない。ここで観測しているのは、商取引全体に占める電子取引の構成変化である。
    モール、ブランド直販、SNS経由などの内訳は、報告書を実読してから分ける。
channels: []
relations: []
sources:
  - https://www.meti.go.jp/press/2025/08/20250826005/20250826005.html
  - https://www.meti.go.jp/policy/it_policy/statistics/outlook/250826_kohyoshiryo.pdf
  - https://ecnomikata.com/ecnews/52119/
status: verified
updated: 2026-11-17
---

# 国内BtoC-ECの拡大

## 見出している未来（何に向かって動いているか）

**未確認**: 生活者が「今後ネット通販の利用・支出を増やしたいか」を直接問う独立調査に到達できていない（総務省「家計消費状況調査」は実績のみ、PwC「日本の消費者調査」は分析者自身の見通しで消費者本人の意向調査ではない）。

## 足元の根拠（完了した事実）

日本国内の消費者向け商取引で、電子商取引の金額と比率が拡大している。

経済産業省「令和6年度電子商取引に関する市場調査」の公式発表本文では、2024年の国内BtoC-EC市場規模は
26.1兆円（2023年24.8兆円、2022年22.7兆円）で、前年比5.1％増。BtoC-EC化率は9.8％で、前年比0.4ポイント増とされている。

ここで言えるのは、消費者向け商取引のうち電子的に行われた金額の比率が上がったことまでである。
消費者の購買動機や、特定のECモール・SNSが成長を生んだ因果までは、この数値からは言えない。

上記の数値は経済産業省の公式発表本文を直接取得して確認した。報告書PDFの図表内訳や調査方法の細部は未読のため、
物販・サービス・デジタルの内訳を使った主張はまだ置かない。

## kind と stage の判定

**kind: demand-shift とした。** 観測しているのは、供給側の施策ではなく、消費者向け商取引に占める電子取引の規模・比率の変化である。
ただし、EC化率は商取引の構成を示す指標であり、消費者がなぜECを選んだかを直接測るものではない。

**stage: growing とした。** 公式発表本文で、2022年から2024年にかけて市場規模が22.7兆円から26.1兆円へ、
EC化率が上昇したことを確認した。調査方法・分母の変更は報告書PDFで追加確認する。

## 時間

始点は、このファイルで直接使う経年値が確認できる2022年以降の拡大局面として `2022~` と置いた。
ECそのものの始まりを2022年と主張しているわけではない。終点は `..`（継続中）。

## チャネルと伝播

特定のプラットフォームや媒体が発生チャネルだとは置かない。ここで観測しているのは、商取引全体に占める電子取引の構成変化である。
モール、ブランド直販、SNS経由などの内訳は、報告書を実読してから分ける。

## 追記（2026-11-17・二次情報・一次未確認）

ECのミカタの記事（https://ecnomikata.com/ecnews/52119/、2026-11-17に取得）によると、経済産業省が2026年10月21日に「令和7年度電子商取引に関する市場調査」を公表し、2025年の国内BtoC-EC市場規模は27.6兆円（記事の記載で前年比5.5％増）、BtoC-EC化率は9.80％（前年比0.02ポイント増）とされる。記事は前年を26.1兆円と記しており、27.6兆円と26.1兆円から計算した増加率は約5.7％で記事の5.5％と一致しない（2024年値の改定の有無は未確認）。
上の2024年の値（26.1兆円・9.8％）は上書きせず残す。経産省の公表ページ（https://www.meti.go.jp/press/2026/10/20261021001.html）は2026-11-17にHTTP 403で、Web Archiveにも保存が無く、一次情報は未確認。このため予測「2025年が26.1兆円を下回らない」の答え合わせは一次確認までresolvedにしない。

## 反証（これが偽なら何が観測されるか）

- 2025年の次回公表値で国内BtoC-EC市場規模が2024年の26.1兆円を下回り、EC化率も低下する
- 経年値の分母・調査方法が変わっており、見かけの増加が同じ定義での成長ではないと判明する
- 物販・サービス・デジタルの内訳の一部だけが増え、BtoC-EC全体の拡大というまとめが過大だったと分かる

## 未着手

- 2026年11月17日、https://www.meti.go.jp/press/2025/08/20250826005/20250826005.html は直接取得が403（またはbot遮断の空応答）で、Web Archiveの保存版（2026-05-15取得分）を取得して、2024年の26.1兆円（前年24.8兆円、前々年22.7兆円、前年比5.1％増）とBtoC-EC化率9.8％（前年比0.4ポイント増）を再確認した。報告書PDF（250826_kohyoshiryo.pdf）は403で未確認。公式ページを直接開けていないため valid_as_of は更新していない
- 経産省の2026-10-21公表ページ（令和7年度調査）を一次で取得し、27.6兆円・9.80％と2024年値の改定有無を確認する

- 2026年9月17日、生活者の「今後ネット通販を増やしたいか」という意向を測る独立調査を探したが見つからなかった（**未確認**の理由）。EC拡大を裏づける消費者意向調査（総務省・消費者庁・業界団体等）を継続して探す
- 経済産業省の報告書PDFを取得して、分野別内訳・調査方法・分母の変更を実読確認する
- 物販系・サービス系・デジタル系の内訳と、各分野のEC化率を確認する
- 2025年公表予定の次回調査で予測を答え合わせする
- EC拡大に応答するpracticeを、広告施策の主張と混同せずに整理する
