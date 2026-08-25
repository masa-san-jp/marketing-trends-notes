---
id: trend/sleep-rest-health-management
uri: urn:mtn:trend/sleep-rest-health-management
type: trend
kind: demand-shift
stage: growing
market: health-wellness
geo: japan
label_ja: 睡眠・休養の健康管理ニーズの可視化
label_en: Visibility of sleep and rest as health-management needs
authority:
  wikidata: null
  none_reason: "Wikidataで「睡眠・休養の健康管理ニーズ」「sleep and rest health-management needs」を確認したが、日本の生活者の睡眠状態、健康目標、支援策が連動する現象そのものの項目は確認できない"
time:
  start: "2024~"
  end: ".."
  display: "健康日本21（第三次）の開始と2024年国民健康・栄養調査のベースラインを通じ、睡眠・休養を健康管理の対象として測定・支援する局面"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: 睡眠で休養がとれている者の増加
  note: "「睡眠・休養の健康管理ニーズの可視化」は、厚生労働省の健康目標と国民調査を生活者側の課題として要約する記述的なラベル。生活者がこの複合語を自称するかは確認していない"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.mhlw.go.jp/content/10900000/001603146.pdf", certainty: independent, retrieved: primary, as_of: "2025-12-02"}
  - {field: stage, source: "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/suimin/index.html", certainty: attested, retrieved: primary, as_of: "2024-09-18"}
  - {field: time, source: "https://www.mhlw.go.jp/stf/newpage_66279.html", certainty: independent, retrieved: primary, as_of: "2025-12-02"}
predictions:
  - {claim: "次回の国民健康・栄養調査で、睡眠で休養がとれている者の年齢調整値が2024年の78.5%を大きく下回らない", by: "2027-12", resolved: null, outcome: null}
channel_scope:
  status: not-applicable
  note: >-
    健康診断・保健指導、職場の健康経営、自治体の普及啓発、医療・保健専門職、睡眠ガイド、ウェアラブル・アプリなどを通じて伝わる。どの接点が睡眠改善の
    実行、受診、商品購入に結び付くかは未確認のため、`channels` は張らない。
channels: []
relations: []
sources:
  - https://www.mhlw.go.jp/stf/newpage_66279.html
  - https://www.mhlw.go.jp/content/10900000/001603146.pdf
  - https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/suimin/index.html
  - https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/kenkounippon21_00006.html
  - https://www.mhlw.go.jp/web/t_doc?dataId=00012990&dataType=0&pageNo=1
status: verified
updated: 2026-08-11
---

# 睡眠・休養の健康管理ニーズの可視化

## 何が変わったか

睡眠や休養が、個人の生活習慣の助言だけでなく、健康づくりの指標、職域・自治体の支援、生活改善の対象として測定されるようになっている。
厚生労働省の令和6年国民健康・栄養調査では、20歳以上で「睡眠で休養がとれている」者は79.6％（年齢調整値78.5％）だった。20～59歳では73.0％で、
1日の平均睡眠時間が基準範囲にある者は56.0％（年齢調整値56.9％）だった。

健康日本21（第三次）は2024年度から2035年度までを計画期間とし、睡眠で休養がとれている者の割合80％、適切な睡眠時間を確保できている者の割合60％を
目標に置いている。厚生労働省は「健康づくりのための睡眠ガイド2023」や支援ツールも公開している。ただし、調査で睡眠不足・休養不足が確認されたことと、
睡眠関連商品・アプリ・サービスの購入が増えたこと、個々の介入で健康状態が改善したことは別の事実として扱う。

## kind と stage の判定

**kind: demand-shift とした。** 観測しているのは、生活者の睡眠による休養感・睡眠時間と、健康づくりの指標として睡眠を改善対象にする需要側の
課題である。睡眠アプリやウェアラブルなど特定の製品カテゴリの供給拡大を測るtrendや、厚生労働省の施策そのものを測るtrendとは区別する。

**stage: growing とした。** 2024年からの健康日本21（第三次）、2024年度調査によるベースライン、睡眠ガイド・支援ツール、職域や自治体向けの
普及啓発が接続している。一方、睡眠支援サービスの利用率、介入の継続率、睡眠改善と受診・生産性・生活満足度の関係は同じ定義で比較できないため、
市場全体で一般化したpeakとは判定しない。

## 時間

始点は健康日本21（第三次）が開始された `2024~` とした。これは睡眠の問題や睡眠産業の始まりではなく、睡眠による休養感と睡眠時間を国民健康づくりの
目標として継続測定・支援する枠組みが始まった時点である。終点は `..`（継続中）。

## チャネルと伝播

健康診断・保健指導、職場の健康経営、自治体の普及啓発、医療・保健専門職、睡眠ガイド、ウェアラブル・アプリなどを通じて伝わる。どの接点が睡眠改善の
実行、受診、商品購入に結び付くかは未確認のため、`channels` は張らない。

## 反証（これが偽なら何が観測されるか）

- 睡眠・休養が健康管理の継続課題でないなら、国民健康・栄養調査で休養感・睡眠時間の測定や健康日本21の目標・支援策が継続しないはず
- 睡眠状態の改善ニーズが生活者の実行に移るなら、睡眠時間、休養感、日中の眠気、生活習慣、相談・受診などが同じ対象で経時的に改善するはず
- 睡眠支援の提供が健康価値につながるなら、支援サービスの利用継続、睡眠指標、仕事・学習への影響、生活満足度を介入前後で比較できるはず

## 未着手

- 2024年調査の年齢・就業・地域別に、休養感、睡眠時間、日中の眠気、就寝・起床時刻を確認する
- 健康診断、職域、自治体、医療、アプリ・ウェアラブルの支援接点ごとに、利用率・継続率・改善指標を同じ定義で整理する
- 睡眠支援の利用と、受診、服薬、労働時間、事故、学習、生活満足度との因果関係を確認する
- 応答するpractice（睡眠状態の確認、生活・勤務環境の改善、必要時の相談・受診案内をつなぐ運用）の採用率と実績を確認する
