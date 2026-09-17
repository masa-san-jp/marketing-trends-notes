---
id: trend/parcel-delivery-volume-expansion
uri: urn:mtn:trend/parcel-delivery-volume-expansion
type: trend
kind: demand-shift
stage: growing
market: retail-commerce
geo: japan
label_ja: 宅配便取扱量の拡大
label_en: Expansion of parcel-delivery volume
authority:
  wikidata: null
  none_reason: "「宅配便取扱量の拡大」「parcel delivery volume expansion Japan」で検索したが、日本の宅配便取扱個数の変化そのもののWikidata項目は確認できない（2026-08-11検索実施）"
time:
  start: "2020~"
  end: ".."
  display: "EC・生活様式の変化を背景に、宅配便取扱個数が年間50億個規模へ拡大する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 宅配便取扱個数の増加
  note: "「宅配便取扱量の拡大」は、国土交通省の宅配便・メール便取扱実績を要約する記述的なラベル"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mlit.go.jp/report/press/jidosha04_hh_000341.html", certainty: independent, retrieved: primary, as_of: "2024年度", tense: completed}
  - {field: stage, source: "https://www.mlit.go.jp/report/press/jidosha04_hh_000341.html", certainty: independent, retrieved: primary, as_of: "2023-2024年度", tense: completed}
  - {field: time, source: "https://www.mlit.go.jp/report/press/jidosha04_hh_000341.html", certainty: independent, retrieved: primary, as_of: "2020-2024年度", tense: completed}
  - {field: current-status, source: "https://www.jcer.or.jp/research-report/20201117-2.html", certainty: independent, retrieved: primary, as_of: "2020-11", tense: intended}
predictions:
  - {claim: "2025年度の宅配便取扱個数が2024年度の50億3,147万個を下回らない", by: "2027-12", resolved: null, outcome: null}
  - {claim: "国土交通省の宅配便取扱実績が、日本経済研究センターの予測（2035年度に88億個）と整合する経路で増加を続け、2030年度時点で60億個を下回らない", by: "2031-03", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    EC、店舗受取、宅配ボックス、置き配、日時指定、食品宅配、返品、配送追跡、ラストマイルを通じて購買体験へ伝わる。取扱個数を生む注文経路の因果は未確認である。
channels: []
relations: []
sources:
  - https://www.mlit.go.jp/report/press/jidosha04_hh_000341.html
  - https://www.mlit.go.jp/report/press/tokatsu01_hh_000908.html
  - https://www.jcer.or.jp/research-report/20201117-2.html
status: verified
updated: 2026-09-17
---

# 宅配便取扱量の拡大

## 見出している未来（何に向かって動いているか）

公益社団法人日本経済研究センター（JCER、1963年設立の非営利民間研究機関）は、EC化の進展を
背景に、宅配便取扱個数が2019年度の43億個から2035年度には88億個へ倍増すると予測している
（2020年11月17日公表）。同センターは、物販系EC化率が2019年度の7％弱から2035年度には約
30％に高まると見込んでおり、これがネット通販利用増加を通じて宅配便個数を押し上げる主因だと
説明している。

この予測は2020年時点のもので、その後のコロナ禍の需要変動や2024年問題（トラックドライバーの
労働時間規制）を踏まえた更新版かどうかは、今回の調査では確認できていない。ただし、既存の
足元の根拠（下記）にある2024年度の実績（50億3,147万個）は、この予測の経路上にある水準である。

## 足元の根拠（完了した事実）

宅配便の取扱量が年間50億個規模となり、EC、在宅時間、贈答、食品・日用品配送などの購買後接点が大きくなっている。国土交通省によると、2024年度の宅配便取扱個数は50億3,147万個で、前年度から0.5％増加した。一方、メール便は7.3％減少しており、配送形態ごとに動きが異なる。

取扱個数の増加はEC購入者数や購買頻度、宅配事業者の利益を直接表さない。再配達、荷姿、地域、配送時間、置き配・宅配ボックス、ドライバー不足などの制約を同時に見る必要がある。

## kind と stage の判定

**kind: demand-shift とした。** 観測しているのは荷物の取扱個数という購買後需要の結果であり、特定の物流会社の営業施策ではない。

**stage: growing とした。** 2024年度も取扱個数が前年度を上回り、EC拡大とともに50億個規模で継続しているためである。ただし、取扱量の増加率は小さく、配送効率・再配達・地域差があるため、無制限の成長とは判定しない。

## 時間

EC・宅配の長期推移と2024年度実績を追うため `2020~` とした。終点は `..`（継続中）。

## チャネルと伝播

EC、店舗受取、宅配ボックス、置き配、日時指定、食品宅配、返品、配送追跡、ラストマイルを通じて購買体験へ伝わる。取扱個数を生む注文経路の因果は未確認である。

## 反証（これが偽なら何が観測されるか）

- 次回の取扱実績で宅配便個数が複数年連続して減少する
- 個数が増えても注文数・購入者数が増えず、大口・高単価・返品の影響だけと分かる
- 再配達、配送遅延、供給制約が悪化し、消費者が配送を選ばなくなる

## 未着手

- 2026年9月17日、日本経済研究センターの2020年11月レポートを実読して見出している未来を追記した。2020年時点の予測であり、より新しい更新版があるかは未確認
- EC注文数、宅配個数、購入者、頻度、単価、返品、再配達を接続する
- 地域、配送業者、荷姿、受取方法、時間帯別の構成を比較する
- 2025年度の取扱実績で予測を答え合わせする
- JCERの2035年度88億個予測に対する経路上の水準を、2030年度時点の実績で確認する（predictions参照）
