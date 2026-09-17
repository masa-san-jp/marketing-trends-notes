---
id: trend/live-entertainment-experience-expansion
uri: urn:mtn:trend/live-entertainment-experience-expansion
type: trend
kind: demand-shift
stage: growing
market: entertainment-content
geo: japan
label_ja: ライブ・体験型エンタメ消費の拡大
label_en: Expansion of live and experience-based entertainment spending
authority:
  wikidata: null
  none_reason: "「ライブ・体験型エンタメ消費の拡大」「live experience entertainment spending Japan」で検索したが、この消費構造の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2020~"
  end: ".."
  display: "コロナ禍後の回復を超えて、ライブ・音楽興行・体験型消費が拡大する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: ライブ・エンタテインメント市場の拡大
  note: "「ライブ・体験型エンタメ消費の拡大」は、経済産業省が整理する第三次産業活動指数とライブ市場調査を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.meti.go.jp/statistics/toppage/report/minikaisetsu/hitokoto_kako/20251126hitokoto.html", certainty: independent, retrieved: primary, as_of: "2024", tense: completed}
  - {field: stage, source: "https://www.meti.go.jp/statistics/toppage/report/minikaisetsu/hitokoto_kako/20251126hitokoto.html", certainty: independent, retrieved: primary, as_of: "2020-2024", tense: completed}
  - {field: time, source: "https://www.meti.go.jp/statistics/toppage/report/minikaisetsu/hitokoto_kako/20251126hitokoto.html", certainty: independent, retrieved: primary, as_of: "2019-2024", tense: completed}
  - {field: current-status, source: "https://corporate.pia.jp/news/detail_live_enta_market20260617.html", certainty: vendor, retrieved: primary, as_of: "2026-06-17", tense: intended}
predictions:
  - {claim: "次回の同種のライブ市場調査で、2024年の総動員数約5,940万人を下回らない", by: "2028-12", resolved: null, outcome: null}
  - {claim: "ぴあ総研が発表する将来予測（2035年に市場規模が初の1兆円台）に向けて、2030年時点の同社発表値が2025年実績（8,564億円）を下回らない", by: "2031-06", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    会場、チケット販売、ファンクラブ、SNS・動画、物販、配信、観光・交通、海外アーティスト公演など複数の接点がある。どの接点が購入を発生させたかの因果は未確認である。
channels: []
relations: []
sources:
  - https://www.meti.go.jp/statistics/toppage/report/minikaisetsu/hitokoto_kako/20251126hitokoto.html
  - https://corporate.pia.jp/news/detail_live_enta_market20260617.html
status: verified
updated: 2026-09-17
---

# ライブ・体験型エンタメ消費の拡大

## 見出している未来（何に向かって動いているか）

ぴあ総研（ぴあ株式会社の調査機関）は、国内ライブ・エンタテインメント市場が2035年に初めて
1兆円台に達するとの見通しを示している（2026年6月17日発表「ライブ・エンタメ市場規模は、
過去最高の8千5百億円超え。2035年には1兆円台に」）。2025年の市場規模は8,564億円（前年比
12.6%増、3年連続の過去最高）で、動員1人あたりの単価が9,286円（同4.5%増）まで上昇して
おり、公演回数の増加よりも「興行規模の大型化」と「単価上昇」が市場成長の主因に移っている
と分析している。

これはぴあという興行チケット販売企業自身の調査・予測であり（`vendor`）、独立した第三者に
よる長期予測ではない。ぴあ総研は、今後は一人ひとりの観客が得る体験価値を高める「高付加価値化」
が市場成長の鍵になると位置づけている。

## 足元の根拠（完了した事実）

ライブ、演劇、音楽興行など、現地参加を伴う体験型エンターテインメントへの消費が拡大している。経済産業省の分析では、第三次産業活動指数の「音楽・芸術等興行」は2020年の36.0から2024年の196.6へ上昇し、「娯楽業」全体も2024年に122.7となってコロナ禍前と同水準になった。

ライブ市場調査では、2024年の総動員数は約5,940万人、総売上額は約6,122億円で、いずれも過去最多とされる。チケット単価、会場、出演者、海外公演、物販、配信などの内訳が混ざるため、動員数の増加を個々のファンの利用頻度や利益増と同一視しない。

## kind と stage の判定

**kind: demand-shift とした。** 観測対象は公演・ライブへの参加と支出であり、特定媒体の広告費や興行主の施策量ではない。

**stage: growing とした。** 2024年の指数・動員・売上がコロナ禍前を超える水準に達し、体験型消費の拡大が説明されている。価格上昇や会場供給の影響も含むため、すべての公演・地域・所得層で同じ成長とは判定しない。

## 時間

コロナ禍で落ち込んだ2020年から2024年までの回復・拡大が同じ資料で確認できるため `2020~` とした。終点は `..`（継続中）。

## チャネルと伝播

会場、チケット販売、ファンクラブ、SNS・動画、物販、配信、観光・交通、海外アーティスト公演など複数の接点がある。どの接点が購入を発生させたかの因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 次回以降の指数・動員数・売上の複数指標が同時に低下し、2024年の過去最多が一時的な反発となる
- チケット価格上昇だけで、実動員数・公演数・リピート参加が増えていないと分かる
- 特定ジャンル・大都市・一部アーティスト以外では体験型消費の拡大が再現されない

## 未着手

- 2026年9月17日、ぴあ総研のプレスリリースを実読して見出している未来を追記した。2035年予測の詳細な年平均成長率は本文取得の範囲では確認できなかった
- ジャンル、地域、会場規模、国内外、チケット単価、物販、配信を分けて比較する
- 「推し活」・体験型消費・ファンクラブ・再参加が売上に与える寄与を独立データで確認する
- 次回の市場調査で予測を答え合わせする
- 独立した調査機関による中長期のライブ市場予測を探し、ぴあ総研の予測と比較する
