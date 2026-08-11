---
id: trend/gaming-digital-global-expansion
uri: urn:mtn:trend/gaming-digital-global-expansion
type: trend
kind: demand-shift
stage: growing
market: gaming
geo: global
label_ja: ゲーム市場のデジタル・グローバル化
label_en: Digital and global expansion of the game market
authority:
  wikidata: null
  none_reason: "Wikidataで「ゲーム市場のデジタル・グローバル化」「digital and global expansion of the game market」を確認したが、この市場構造の変化そのものの項目は確認できない"
time:
  start: "2020~"
  end: ".."
  display: "2020年代のゲーム市場拡大、デジタル販売・モバイル・PC・海外市場の比重上昇"
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: ゲーム市場のデジタル・グローバル化
  note: "消費者が自称する呼称ではなく、ゲーム産業の市場規模・プラットフォーム・地域データをこのKBでまとめた名称"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2026-11-11"
evidence:
  - {field: kind, source: "https://www.cesa.or.jp/action/industry-research/2024/", certainty: independent, retrieved: primary, as_of: "2024-12-20"}
  - {field: time, source: "https://www.cesa.or.jp/action/industry-research/2024/", certainty: independent, retrieved: primary, as_of: "2024-12-20"}
  - {field: stage, source: "https://www.cesa.or.jp/uploads/2025/release_game_industry_report2025.pdf", certainty: independent, retrieved: primary, as_of: "2025-12-15"}
channels: []
relations: []
sources:
  - https://www.cesa.or.jp/action/industry-research/2024/
  - https://www.cesa.or.jp/action/industry-research/2025/
  - https://www.cesa.or.jp/uploads/2025/release_game_industry_report2025.pdf
status: verified
updated: 2026-08-11
---

# ゲーム市場のデジタル・グローバル化

## 何が変わったか

CESAのゲーム産業レポート2025では、2024年のグローバルなゲームコンテンツ市場を31兆42億円、前年比5.0％増としている。プラットフォーム別では、
モバイルゲームが18兆4,334億円で前年比6.0％増、全体の6割近くを占める。PCゲームは過去4年間で59.7％増と各プラットフォームで最も拡大し、
全体シェアで家庭用ゲームを上回ったとされる。CESAの2024年レポートも、デジタル販売を含む国内外の売上と、Steamの台頭によるPCゲームの伸長を
扱っている。

一方、同じ2025年レポートの2024年国内ゲーム人口は5,475万人で、前年の5,553万人から微減した。モバイルゲーム人口は4,278万人で前年比1.8％減、
PCゲーム人口は1,452万人で0.5％増、家庭用ゲーム人口は2,951万人で0.7％減だった。したがって、ここで確認できる変化は「国内の利用者が一様に
増えた」ことではなく、世界市場の拡大、デジタル販売、モバイル・PCへの価値移動、地域をまたぐ販売機会が同時に進んでいることである。

この構造変化は、ゲームを単発のパッケージ販売だけでなく、デジタル配信、継続的なアップデート、プラットフォーム別のコミュニティ、海外向けの
ローカライズ・運用を含む事業として設計する前提を広げる。ただし、ゲームごとの収益性、継続率、広告・課金の因果はこの統計からは分からない。

## kind と stage の判定

**kind: demand-shift とした。** CESAの市場規模、プラットフォーム別の利用者数、地域別の市場データが、ゲームの消費・販売構造の変化を示している
ためである。個別企業が売り込む広告カテゴリではなく、業界団体の市場・ユーザー統計に基づく変化として扱う。

**stage: growing とした。** 2020年以降のグローバル市場拡大、2024年のモバイル市場増加、PCゲームの継続的な拡大、海外市場・法規制動向の分析拡充が
確認できる。一方、国内ゲーム人口は2024年に微減しており、プラットフォーム別の収益性や継続利用の比較も揃っていないため、peakやcommoditizedとは
判定しない。

## 時間

始点は、CESAが2020年にグローバルゲームコンテンツ市場が20兆円を突破し、その後も拡大傾向と整理している `2020~` とした。これはゲームの発明や
オンライン化の始まりではなく、今回確認した市場構造の拡大局面の観測時点である。終点は `..`（継続中）。

## チャネルと伝播

特定のSNSや広告媒体から発生した変化ではなく、モバイルアプリストア、PCゲームプラットフォーム、家庭用ゲーム機のオンラインストア、動画・配信、
海外販売・ローカライズを通じて伝わる市場構造の変化である。現在の資料だけでは、どのチャネルが需要を発生させたかを一つに特定できないため、
`channels` は張らない。**未確認**: プラットフォーム別の新規獲得、継続率、配信・動画視聴からの送客、海外地域別の購入経路。

## 反証（これが偽なら何が観測されるか）

- ゲーム市場のデジタル・グローバル化が続いていないなら、複数年の市場統計でグローバル市場、PC・モバイル、海外売上の拡大が同じ定義で確認できなくなるはず
- プラットフォームの価値移動が起きていないなら、PCゲームの市場・利用者シェアが家庭用ゲームを上回る状態やモバイルの大きな構成比が継続しないはず
- 利用者の需要まで一様に拡大しているなら、国内ゲーム人口が横ばい・減少する一方で市場規模だけが増える状態ではなく、国内の継続利用者数も同じ方向に増えるはず

## 未着手

- デジタル販売、パッケージ販売、基本無料・買い切り・継続課金などを同じ定義で分けた国内市場時系列を確認する
- モバイル、PC、家庭用、配信・動画経由の新規獲得・継続率・課金率を比較できる独立データを探す
- 日本発タイトルの地域別売上、ローカライズ、コミュニティ運用、広告・インフルエンサー施策の寄与を事例ごとに分解する
- このtrendに応答するpractice（デジタル配信・地域別展開・継続運用をつなぐゲーム事業設計）の採用率と実績を整理する
