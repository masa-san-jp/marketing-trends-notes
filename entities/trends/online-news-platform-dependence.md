---
id: trend/online-news-platform-dependence
uri: urn:mtn:trend/online-news-platform-dependence
type: trend
kind: demand-shift
stage: emerging
market: entertainment-content
geo: japan
label_ja: オンラインニュースプラットフォーム依存の可視化
label_en: Emerging dependence on online news platforms
authority:
  wikidata: null
  none_reason: "「オンラインニュースプラットフォーム依存の可視化」「online news platform dependence Japan」で検索したが、この利用経路の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2023~"
  end: ".."
  display: "紙媒体からニュースポータル・検索等のオンライン経路へ接点が移り、取引条件の実態調査が始まった段階"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: ニュースコンテンツのオンライン流通・利用増加
  note: "「オンラインニュースプラットフォーム依存の可視化」は、文化庁・公正取引委員会の実態調査の説明を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-09-11"
evidence:
  - {field: kind, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2023-03"}
  - {field: stage, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2023-03"}
  - {field: time, source: "https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/", certainty: independent, retrieved: primary, as_of: "2023-03"}
predictions:
  - {claim: "次回の公正取引委員会または文化庁の実態調査で、ニュースポータル・検索・媒体サイトの利用経路と取引条件が再整理される", by: "2028-12", resolved: null, outcome: null}
channels: []
relations: []
sources:
  - https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/kihonseisaku/r04_03/
status: verified
updated: 2026-08-11
---

# オンラインニュースプラットフォーム依存の可視化

## 何が変わったか

ニュースの接点が紙媒体だけでなく、ニュースポータル、検索結果、オンライン媒体などへ移り、ニュースメディアとプラットフォームの取引条件が競争・著作権政策の調査対象になっている。文化庁の2023年審議会では、新聞・雑誌など既存の紙媒体の利用が減る一方、インターネット上のニュースプラットフォーム利用が増えていると説明された。

公正取引委員会は、ニュースポータルや検索の表示・抜粋・リンク、ライセンス対価、表示順位、メディアへの送客などを実態調査の論点としている。利用が増えたことと、プラットフォームがニュース事業者の収益を改善することは別の命題であり、依存度・送客・対価・広告収入を分けて観測する必要がある。

## kind と stage の判定

**kind: demand-shift とした。** 変化の中心は消費者がニュースを読む経路であり、特定プラットフォームの機能ローンチや広告主の支出額ではない。

**stage: emerging とした。** オンライン利用増加は政策議論の前提になっているが、ニュースポータル、検索、媒体サイト、SNS、動画の利用割合を同じ定義で比較する統計と、取引条件の経年変化はまだ十分に揃っていない。

## 時間

文化庁・公正取引委員会の実態調査が公開された2023年を観測起点として `2023~` とした。終点は `..`（継続中）。

## チャネルと伝播

ニュースポータル、検索、媒体サイト、SNS、動画、メール・アプリ通知など複数の経路がある。検索・ポータルの抜粋閲覧で終わるのか、媒体サイトへ送客されるのか、広告・購読へ転換するのかは経路ごとに異なる。

## 反証（これが偽なら何が観測されるか）

- 紙媒体の利用減少とオンラインニュース利用増加が同じ定義の調査で再現されない
- ニュースポータル・検索の利用が増えても、メディアへの送客、購読、広告収入、適正な対価に変化がない
- 実態調査の後も取引条件・表示順位・対価の論点が縮小し、プラットフォーム経由の重要性が確認されない

## 未着手

- ニュースポータル、検索、媒体サイト、SNS、動画別の利用率・滞在・送客を比較する
- ライセンス、抜粋、表示順位、広告、購読、対価還元を媒体規模別に分解する
- 公正取引委員会の実態調査結果と、その後の取引条件の変化を確認する
