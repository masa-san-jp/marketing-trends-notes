---
id: channel/tiktok
uri: urn:mtn:channel/tiktok
type: channel
label_ja: TikTok
label_en: TikTok
authority:
  wikidata: null
  none_reason: Wikidata に項目があることは確実だが、執筆環境からAPIに到達できず QID 未確認
time:
  start: "2017~"
  end: ".."
  display: 国際版の展開開始（2017年とされる・未確認）から
relations:
  - {type: operated_by, target: player/bytedance}
sources:
  - https://newsroom.tiktok.com/ja-jp
status: draft
updated: 2026-08-10
---

# TikTok

## 事実（運営・規模・課金）

ByteDance（[player/bytedance](../players/bytedance.md)）が運営する短尺動画プラットフォーム。
レコメンドフィード（For You）を視聴の基本単位とし、フォローグラフに依存しない分配を特徴とする。

**未確認**: 国内 MAU・年代構成・広告メニューの現行仕様。公式発表（[Newsroom](https://newsroom.tiktok.com/ja-jp)）
の数字は vendor として扱い、規模の断定には総務省調査系の独立数字を使う——どちらも執筆環境から
実読できておらず、このファイルの規模に関する記述はすべて再検証待ち。

## アルゴリズムと分配の変遷

**未確認**: 分配ロジックの公表資料・変更履歴。アルゴリズム変更は event として釘を打つ運用に
する（このKBでの channel は「変化が起きる場所」なので、場所自体の変化が時間軸の釘になる）。

## このKBでの位置

ショート動画形式の発生チャネル（[trend/short-video-mainstream](../trends/short-video-mainstream.md)
の `originated_on`）。伝播の追跡では「形式を模倣される側」の基準点になる。
