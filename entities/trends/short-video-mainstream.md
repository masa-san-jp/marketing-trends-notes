---
id: trend/short-video-mainstream
uri: urn:mtn:trend/short-video-mainstream
type: trend
kind: tech-enabled
stage: peak
market: entertainment-content
geo: japan
label_ja: ショート動画視聴の主流化
label_en: Short-form video mainstreaming
authority:
  wikidata: null
  none_reason: 現象そのものの項目は想定しにくい。執筆環境からWikidata APIに到達できず検索は未実施
time:
  start: "2020~"
  end: ".."
  display: コロナ禍の在宅時間拡大期から
naming:
  self_identified: false
  named_by: null
  named_when: null
  original_label: ショート動画
  note: "業界・媒体側の呼称が一般化した型。視聴者側の自称は「TikTok見てる」のように媒体名で、形式名では呼ばない。named_by は特定できない（未確認）"
freshness:
  valid_as_of: "2026-08-10"
  recheck_by: "2027-02-10"
evidence:
  - {field: stage, source: "https://www.soumu.go.jp/iicp/research/results/media_usage-time.html", certainty: independent, as_of: "2025"}
predictions:
  - {claim: "2027年末時点でも、国内若年層の動画視聴でショート形式が支配的であり続ける（総務省調査系の利用率が前年割れしない）", by: "2027-12", resolved: null, outcome: null}
channels:
  - {role: originated_on, target: channel/tiktok}
  - {role: spread_to, target: channel/youtube}
relations: []
sources:
  - https://www.soumu.go.jp/iicp/research/results/media_usage-time.html
  - https://newsroom.tiktok.com/ja-jp
status: draft
updated: 2026-08-10
---

# ショート動画視聴の主流化

## 何が変わったか

60秒前後の縦型動画を、フォローではなくレコメンドで連続視聴する形式が、若年層を起点に動画視聴の
主要な形式になった。視聴の単位が「番組・作品を選んで見る」から「フィードを流し見る」に変わり、
発見（新しいものに出会う場所）の主導権が検索・フォローからレコメンドアルゴリズムに移った。

**未確認**: 規模の定量。総務省「情報通信メディアの利用時間と情報行動に関する調査」が年代別の
ソーシャルメディア・動画系サービスの利用率を持つはずで、evidence にはその URL を置いたが、
執筆環境のネットワーク制限で最新版の数字を実読できていない。**この trend の規模の主張はすべて
再検証（数字の実読）待ち**である。

## kind と stage の判定

**kind: tech-enabled とした。** 判定表の第2問——TikTok 型のレコメンドフィード（機能のローンチ）が
先行し、それ無しでこの視聴形式は成立しない。需要側の変化（可処分時間の奪い合い）はあるが、
形式そのものは技術・プロダクトが規定した。

**stage: peak とした。** 「ショート動画」は一般紙・地上波が説明なしで使う語になっており、
判定表の peak の目安（主流化・説明不要）を満たす。ただし**数字の高原状態は未確認**（上記）。
emerging / growing でないことは確実だが、peak と declining の区別は数字を見るまで確定しない。

## 時間

始点は `2020~`（およそ）。TikTok の国内普及は2019年以前に始まっているが、「主流化」と呼べる規模に
なった時期としてコロナ禍の在宅時間拡大期を目安に置いた。**未確認**: この時期の特定を裏づける
時系列データ。終点は `..`（継続中）。

## チャネルと伝播

発生チャネルは [channel/tiktok](../channels/tiktok.md)（`originated_on`）。同形式が
[channel/youtube](../channels/youtube.md)（Shorts）へ伝播した（`spread_to`）——プラットフォーム側が
形式を模倣して実装した型の伝播で、ユーザーが移動した型ではない点が美術の伝播と違う。
**未確認**: Instagram Reels への伝播も同型だが、channel/instagram をまだ置いていないので張っていない
（孤児 stub を作らないため。Reels を扱う調査が入る時に置く）。

## 反証（これが偽なら何が観測されるか）

- 「主流化」が誇張なら、**年代別利用率で若年層のショート形式利用が過半に達していない**はず
  （総務省調査の実読で判定できる。再検証タスクの第一項）
- 「ショート動画」がプラットフォームの売り文句に過ぎない（kind: vendor-pushed が正しい）なら、
  **広告費・視聴時間の独立した統計に形式別の伸びが現れない**はず
- 既に declining なら、**利用時間の前年割れ**が観測されるはず（predictions に置いた）

## 未着手

- 総務省調査の実読と、stage 判定の定量化（このファイルの最優先タスク）
- 応答する practice（ショート動画運用・ショート広告）を responds_to で繋ぐ——現状この trend は
  打ち手に落ちていない（audit が指摘する状態のまま）
- channel/instagram（Reels）の追加と伝播の記録
- 「発見の主導権がレコメンドに移った」ことを独立に示す出典
