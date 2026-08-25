---
id: practice/organic-post-boosting
uri: urn:mtn:practice/organic-post-boosting
type: practice
label_ja: 既存投稿のブースト配信
label_en: Organic post boosting
authority:
  wikidata: null
  none_reason: "wbsearchentities で Spark Ads（en）を検索して0件。運用の型そのものに項目は無く、プラットフォームの製品名にも項目が無い（2026-08-10 検索実施）"
time:
  start: null
  end: ".."
  display: null
saturation: spreading
evidence:
  - {field: time, source: "https://ads.tiktok.com/help/article/spark-ads", certainty: attested, retrieved: primary, as_of: "2026-06"}
channels:
  - {role: observed_on, target: channel/tiktok}
relations:
  - {type: responds_to, target: trend/short-video-mainstream, certainty: hypothesis, source: "https://ads.tiktok.com/help/article/spark-ads"}
sources:
  - https://ads.tiktok.com/help/article/spark-ads
status: draft
updated: 2026-08-10
---

# 既存投稿のブースト配信

## 何をするか

広告用に作った素材を配信するのではなく、**すでに投稿されているオーガニックの動画を、そのまま広告として
配信する**。対象事業者アカウントの投稿だけでなく、クリエイターの投稿を本人の許諾コードを介して広告に使える。

TikTok の Spark Ads がこの型の実装で、[公式ヘルプ](https://ads.tiktok.com/help/article/spark-ads)は
仕様をこう書いている（2026年6月最終更新・原文を取得して確認）。

- オーガニック投稿を使った広告配信で、**ブースト中に得た再生・コメント・シェア・いいね・フォローは
  元のオーガニック投稿に帰属する**
- 対象事業者アカウントの投稿と、**他のクリエイターの投稿（本人の許諾つき）**の両方を使える
- 許諾コードの有効期間を出稿側が設定できる

**未確認**: 開始時期。`time.start` は `null` のまま置いた。TikTok Newsroom の紹介記事とみられる URL
（`/en-us/introducing-spark-ads`）は 200 を返すが、中身は別記事のニュースルーム一覧に転送されており、
**launch を示す一次文書に到達できていない**。ヘルプの「Last updated: June 2026」は更新日であって開始日ではない。

**未確認**: 同型の運用が他プラットフォームにもあるか（Meta の広告としての投稿利用、YouTube Shorts の
同等機能）。TikTok 以外の一次文書に当たっていないので、`channels` は `observed_on: tiktok` の1本だけにした。

## どのトレンドへの応答か

[trend/short-video-mainstream](../trends/short-video-mainstream.md)（ショート動画視聴の主流化）への
応答とみる。レコメンドのフィードを流し見る視聴では、広告然とした素材はフィードの他の投稿と並んだ瞬間に
浮く。既存の投稿をそのまま配信すれば、素材はフィードの文脈で作られたものになる。

ただしこの因果は**私の仮説**（`certainty: hypothesis`）。**未確認**: 広告用素材と既存投稿の配信結果を
比較した独立した検証。プラットフォーム側の効果主張（上記ヘルプの Benefits 節）は、その主張で儲かる側の
記述なので根拠に使わない。

**この型が成立する条件そのものは仕様で確認できる**——エンゲージメントが元投稿に帰属する、という
帰属の設計があって初めて「広告出稿がオーガニックの資産を減らさない」が成り立つ。ここは
`certainty: attested`（当事者の一次言明・自分に不利でも成り立つ仕様の記述）として置いた。

## 成立条件・失敗条件

**効果未確認**:（外部資料で効果を確認できていない）。効いた・効かないを書ける段階にない。

仕様から言えることだけを書くと、この型は**すでに反応のある投稿が手元にあること**を前提にする。
投稿の蓄積が無い出稿者にとっては、先にオーガニックを回す工程が必要になる。
**未確認**: どの程度の蓄積から成立するか。

## 飽和度の判定

`saturation: spreading` とした。配信面の側が製品として提供し、許諾の仕組みまで用意している段階で、
**未確認**: 出稿者側の採用率。commoditized（参加が前提になり超過収益が消える）の判定には、
この形式の出稿が全出稿に占める比率か、同形式内での入札単価の推移が要る。どちらも独立した出典が無い。

## 利用上の注意

**効果未確認**: 手元にあるのは note と X の投稿で、これらに同型の仕組み（既存投稿をそのまま配信し、
反応が元投稿に帰属する）があるかを確認していない。転用を考えるなら、まず**反応のある投稿が
継続的に出ているか**が前提になる。試すとしたら何を測るかから設計が要る。

## 未着手

外部資料で効果を確認できていない論点は、比較可能な公開観測が得られるまで未着手として残す。
