---
id: player/bytedance
uri: urn:mtn:player/bytedance
type: player
label_ja: ByteDance（字節跳動）
label_en: ByteDance
authority:
  wikidata: null
  none_reason: Wikidata に項目があることは確実だが、執筆環境からAPIに到達できず QID 未確認
time:
  start: "2012"
  end: ".."
  display: ByteDance の創立（2012年）から
relations: []
sources:
  - https://www.bytedance.com/
  - https://www.bytedance.com/en/products/
  - https://newsroom.tiktok.com/regarding-tiktoks-data-governance?from_seo_redirect=1&lang=ja-JP
status: draft
updated: 2026-08-25
---

# ByteDance（字節跳動）

## 事実（沿革・事業）

ByteDance は2012年に創立され、同年8月に Toutiao を立ち上げたと自社の沿革で説明している。
その後、2016年9月に中国向け短尺動画サービス Douyin、約1年後に中国国外向けの短尺動画サービス TikTok を
開始し、2017年11月に Musical.ly を買収、2018年に TikTok と統合した。
[ByteDance公式の沿革](https://www.bytedance.com/)

現在の公式プロダクト一覧には TikTok、CapCut、TikTok Shop、Lark、Pico などのサービスが並ぶ。
ただし、このファイルでは個別サービスの市場規模や業績を ByteDance 全体の数字へ一般化しない。
[ByteDance公式プロダクト一覧](https://www.bytedance.com/en/products/)

## TikTokとの関係

[channel/tiktok](../channels/tiktok.md) の `operated_by` の対象として、TikTokをByteDanceのグローバルな
プロダクト群に含める関係を記録する。日本国内のサービス提供主体については、TikTokの説明では
シンガポール法人 TikTok Pte. Ltd. が運営主体で、日本法人 Bytedance株式会社（TikTok Japan）が実務的な提供・
運用を支援するとされている。したがって、この関係はブランド・企業グループ上の運営者を示すものであり、
日本国内の個別契約主体を同一視するものではない。
[TikTokのデータガバナンス説明](https://newsroom.tiktok.com/regarding-tiktoks-data-governance?from_seo_redirect=1&lang=ja-JP)

## このKBでの位置

この entity は、TikTokという発生チャネルの同一性と運営主体を辿るためのプレイヤー記録である。
ByteDance の自社説明は `vendor` として扱い、TikTokの利用規模、広告効果、トレンドの実在を裏づける
独立根拠には使わない。

**未確認**: 国・地域ごとの法人・契約・データ処理の全体構造、出資・所有関係の最新の詳細、ByteDance全体の
利用者数・売上・評価額。これらはこのKBのチャネル同定には不要なため、別途一次資料と独立資料を揃えるまで
追記しない。
