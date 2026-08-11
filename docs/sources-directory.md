# 出典カタログ — どの層から当たるか

調査は**上の層から順に**当たる（[investigation-task.md](investigation-task.md) 手順3）。
層がそのまま `certainty` に対応する。**発行元ではなく「その記述で誰が得をするか」で層を決める**——
同じ発行元でも、事実の言明（`attested`）と利害のある主張（`vendor`）は別。

**確認状況について**: このカタログには、URLに実際に到達して中身を確かめたものだけを「確認済み」と
書く。**未確認のものは未確認と明記する**（このKBの根本規律）。初版の執筆環境はネットワーク制限で
大半の外部サイトに到達できなかったため、未確認が多い。`python3 tools/linkcheck.py` を制限のない
環境で回し、確認できたものからこの表を昇格させる。

## 層1: 官公庁統計・公的調査（`independent`）

利害がなく、n と取り方が公開されている。日本のトレンドの規模の主張はまずここで裏を取る。

| 情報源 | 何が取れるか | URL | 確認状況 |
|---|---|---|---|
| 総務省 情報通信メディアの利用時間と情報行動に関する調査 | メディア別・年代別の利用時間・利用率（年次） | https://www.soumu.go.jp/iicp/research/results/media_usage-time.html | **未確認**（2026-08-10 執筆環境から到達できず） |
| 総務省 通信利用動向調査 | 世帯・企業のネット利用（年次） | https://www.soumu.go.jp/johotsusintokei/statistics/statistics05.html | **未確認**（同上） |
| 経産省 電子商取引に関する市場調査 | EC市場規模・EC化率（年次） | https://www.meti.go.jp/policy/it_policy/statistics/outlook/ie_outlook.html | **未確認**（同上） |
| e-Stat（政府統計の総合窓口） | 家計調査ほか政府統計の横断検索 | https://www.e-stat.go.jp/ | **未確認**（同上） |
| 消費者庁 ステルスマーケティング規制 | 景表法のステマ告示・運用基準 | https://www.caa.go.jp/policies/policy/representation/fair_labeling/stealth_marketing/ | **未確認**（同上） |

## 層2: 当事者の一次言明（`attested`）

仕様・規約・決算開示。**自分に不利でも成り立つ事実の言明**。市場規模や効果の主張はここに入れない。

| 情報源 | 何が取れるか | URL | 確認状況 |
|---|---|---|---|
| Apple Developer — User Privacy and Data Use | ATT の仕様（トラッキングの定義・許可の要件） | https://developer.apple.com/app-store/user-privacy-and-data-use/ | **確認済み**（2026-08-10 実読） |
| Apple Developer — AppTrackingTransparency | ATT フレームワークの技術文書 | https://developer.apple.com/documentation/apptrackingtransparency | **確認済み**（2026-08-10 到達確認） |
| EUR-Lex — Regulation (EU) 2016/679（GDPR） | 個人データ処理の適法根拠、同意、ダイレクトマーケティングへの異議申立て、適用日 | https://eur-lex.europa.eu/eli/reg/2016/679/oj | **確認済み**（2026-08-11 実読） |
| 個人情報保護委員会 — 第三者提供時の確認・記録義務編 | 個人データの第三者提供における取得経緯の確認・記録義務 | https://www.ppc.go.jp/personalinfo/legal/guidelines_thirdparty/ | **確認済み**（2026-08-11 実読） |
| 各社の決算・IR（EDINET／各社IRページ） | 事業セグメントの数字。トレンドの規模の傍証 | https://disclosure2.edinet-fsa.go.jp/ | **未確認**（執筆環境から到達できず） |

## 層3: 業界団体・学術（`independent`）

| 情報源 | 何が取れるか | URL | 確認状況 |
|---|---|---|---|
| JIAA（日本インタラクティブ広告協会） | ネット広告のガイドライン・実態調査 | https://www.jiaa.org/ | **未確認**（同上） |
| Ehrenberg-Bass Institute | マーケティングサイエンスの実証研究（CEP・ダブルジョパディ） | https://marketingscience.info/ | **未確認**（同上） |
| Kraft・Skiera・Koschella — Economic Impact of Opt-in versus Opt-out Requirements for Personal Data Usage | 19か国の広告インプレッションを用いたATT後の追跡可能トラフィック。DSP独自データを含むためユーザー全体の許可率とは区別する | https://www.ftc.gov/system/files/ftc_gov/pdf/3-Skiera-Economic-Impact-of-Opt-in-versus-Opt-out-Requirements-for-Personal-Data-Usage.pdf | **確認済み**（2026-08-11 実読） |
| Mohamed et al. — ATTention Please! An Investigation of the App Tracking Transparency Permission | 4,000件のiOSアプリと114人のユーザー調査。ATT許諾アラートのダークパターンと理解への影響 | https://www.usenix.org/system/files/usenixsecurity24-mohamed.pdf | **確認済み**（2026-08-11 実読） |

## 層4: プラットフォーム・ベンダーの公式発表（`vendor`）

**使ってよい。ただし必ず vendor と明記し、断定に使わない。** ここの数字はその主張で儲かる側の
数字であり、「調査レポート」の顔で来る。裏が取れたら層1〜2の出典に差し替える。

| 情報源 | 注意 | URL | 確認状況 |
|---|---|---|---|
| 電通「日本の広告費」 | 業界の標準指標だが、発行元は広告を売る側。市場の定義変更で系列が切れることがある | https://www.dentsu.co.jp/knowledge/ad_cost/ | **未確認**（同上） |
| TikTok Newsroom | 機能ローンチ日は attested、利用者数・効果の主張は vendor | https://newsroom.tiktok.com/ja-jp | **未確認**（同上） |
| Google / YouTube 公式ブログ・ヘルプ | 同上の使い分け | https://support.google.com/youtube/ | **未確認**（同上） |
| WebKit — Tracking Prevention in WebKit | Safari/WebKitの第三者Cookie、リファラ、ストレージ、ITPの出荷挙動 | https://webkit.org/tracking-prevention/ | **確認済み**（2026-08-11 実読） |
| WebKit — WebKit Features in Safari 13.1 | Safari 13.1の第三者Cookie全面ブロック・Webサイトデータ期限 | https://webkit.org/blog/10247/new-webkit-features-in-safari-13-1/ | **確認済み**（2026-08-11 実読） |
| Google Privacy Sandbox — Next steps for tracking protections in Chrome | Chromeの第三者Cookieに関するユーザー選択方針（2025-04-22） | https://privacysandbox.google.com/blog/privacy-sandbox-next-steps | **確認済み**（2026-08-11 実読） |
| Google Privacy Sandbox — Third-party cookie restrictions | 第三者Cookieなしを前提にした監査・テスト・移行ガイド | https://privacysandbox.google.com/cookies/prepare/overview | **確認済み**（2026-08-11 実読） |
| Adjust・Sensor Tower — モバイルアプリトレンド2024：日本版 | 日本のATTオプトイン率・ゲーム等カテゴリ別指標。計測ベンダー由来のため独立統計とは区別する | https://www.adjust.com/ja/resources/ebooks/japan-app-trends-2024/ | **確認済み**（2026-08-11 実読） |
| 各種ツールベンダーの「◯◯トレンドレポート」 | kind: vendor-pushed の一次資料としては優秀（命名の証拠）。規模の典拠にはしない | （個別に記録） | — |

## 層5: 個別の投稿・記事・事例（`anecdotal`）

存在の証拠にはなる。規模の証拠にはならない。「バズっている」を規模の出典にしない。

| ITmedia マーケティング — 日本のモバイルアプリ市場のATTオプトイン率紹介 | Adjust・Sensor Towerのベンダー資料に基づく日本のカテゴリ別数値の紹介。独立調査とは扱わない | https://marketing.itmedia.co.jp/mm/articles/2409/09/news063.html | **確認済み**（2026-08-11 実読） |

## このカタログの育て方

- 新しい情報源を使ったら、この表に**層と確認状況つきで**追記する（1調査1行の追記でよい）
- 発行元がベンダーに買収された・事業を始めた等で利害が変わったら、層を下げて日付と理由を書く
- 定点で使う調査（総務省・経産省の年次）は、`source` エンティティに昇格させて
  `## 数字の取り方`（n・調査方法・系列の断絶）を記録する
