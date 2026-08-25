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
  - https://newsroom.tiktok.com/dong-hua-komiyuniteiapuritiktokga2017app-ape-awardde-forbes-japanshang-woshou-shang?lang=ja-JP
  - https://newsroom.tiktok.com/how-tiktok-recommends-videos-for-you
  - https://newsroom.tiktok.com/tiktok-new-for-you-feed/?lang=ja-JP
  - https://support.tiktok.com/ja/business-and-creator/tiktok-creator-fund-us
  - https://newsroom.tiktok.com/creativity-program-beta?lang=ja-JP
status: draft
updated: 2026-08-25
---

# TikTok

## 事実（運営・規模・課金）

ByteDance（[player/bytedance](../players/bytedance.md)）が運営する短尺動画プラットフォーム。
日本市場では2017年夏にサービスを開始したと公式ニュースルームが説明している。
[日本でのサービス開始に関する公式記事](https://newsroom.tiktok.com/dong-hua-komiyuniteiapuritiktokga2017app-ape-awardde-forbes-japanshang-woshou-shang?lang=ja-JP)

レコメンドフィード（For You）を視聴・発見の基本面とする。クリエイターのフォロワー数や過去の高成績が
推薦の直接要因ではないとTikTokは説明しているが、ユーザーの操作、動画情報、アカウント・端末設定などを
組み合わせる仕組みであり、「フォローに依存しない」と単純化しない。
[推薦システムの説明](https://newsroom.tiktok.com/how-tiktok-recommends-videos-for-you)

収益化にはクリエイター向け報酬プログラムやLIVEサブスクリプションなどがある。Creator Fund は終了し、
Creator Rewards Program が後継となっている。対象動画の条件や提供地域は制度・地域によって異なるため、
日本のクリエイター全体の収益や広告市場規模へ一般化しない。
[公式サポート](https://support.tiktok.com/ja/business-and-creator/tiktok-creator-fund-us)

**未確認**: 国内 MAU・年代構成・広告メニューの現行仕様。公式発表の数字は vendor として扱い、規模の
断定には総務省調査系などの独立数字を使う。このチャネル本文では国内規模を断定しない。

## アルゴリズムと分配の変遷

For You はユーザーの視聴・いいね・共有・コメント・フォロー、動画のキャプション・サウンド・ハッシュタグ
などを手がかりに個人化される。視聴完了のような反応を強いシグナルとして扱い、既視聴・重複・スパムを避け、
関心外の動画も混ぜて発見の多様性を保つと説明されている。
[TikTok公式の推薦説明](https://newsroom.tiktok.com/how-tiktok-recommends-videos-for-you)

2025年には、日本向けにもトピック管理、スマートフィルター、推薦理由の理解を助ける教育ガイドなど、
ユーザーが「おすすめ」フィードを調整する機能が案内された。
[日本向け公式発表](https://newsroom.tiktok.com/tiktok-new-for-you-feed/?lang=ja-JP)

**未確認**: 分配ロジックの全履歴と、機能変更が国内の視聴時間・発見・購買へ与えた因果。アルゴリズム変更は
event として釘を打つ運用にする（このKBでの channel は「変化が起きる場所」なので、場所自体の変化が時間軸の
釘になる）。

## このKBでの位置

ショート動画形式の発生チャネル（[trend/short-video-mainstream](../trends/short-video-mainstream.md)
の `originated_on`）。伝播の追跡では「形式を模倣される側」の基準点になる。
