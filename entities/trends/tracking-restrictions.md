---
id: trend/tracking-restrictions
uri: urn:mtn:trend/tracking-restrictions
type: trend
kind: regulation-driven
stage: peak
market: cross-category
geo: global
label_ja: 広告トラッキング制約の常態化
label_en: Normalization of ad-tracking restrictions
authority:
  wikidata: null
  none_reason: 現象そのものの項目は想定しにくい。執筆環境からWikidata APIに到達できず検索は未実施
time:
  start: "2018~"
  end: ".."
  display: GDPR適用（2018）前後から段階的に。ATT（2021）で モバイルに波及
naming:
  self_identified: true
  named_by: null
  named_when: null
  original_label: クッキーレス／ポストクッキー
  note: "業界内で自然発生的に定着した呼称で、当事者（広告主・媒体・代理店）自身が使う。初出の特定は未確認。「クッキーレス」はブラウザ側、ATT はアプリ側と、指す範囲が呼称ごとに微妙に違う点に注意"
freshness:
  valid_as_of: "2026-08-11"
  recheck_by: "2027-02-10"
evidence:
  - {field: kind, source: "https://developer.apple.com/app-store/user-privacy-and-data-use/", certainty: attested, retrieved: primary, as_of: "2026-08-10"}
  - {field: kind, source: "https://eur-lex.europa.eu/eli/reg/2016/679/oj", certainty: attested, retrieved: primary, as_of: "2018-05-25"}
  - {field: kind, source: "https://www.ppc.go.jp/personalinfo/legal/guidelines_thirdparty/", certainty: attested, retrieved: primary, as_of: "2023-12"}
  - {field: kind, source: "https://webkit.org/tracking-prevention/", certainty: attested, retrieved: primary, as_of: "2026-08-11"}
  - {field: kind, source: "https://privacysandbox.google.com/blog/privacy-sandbox-next-steps", certainty: attested, retrieved: primary, as_of: "2025-04-22"}
  - {field: time, source: "https://eur-lex.europa.eu/eli/reg/2016/679/oj", certainty: attested, retrieved: primary, as_of: "2018-05-25"}
  - {field: stage, source: "https://www.ppc.go.jp/personalinfo/legal/guidelines_thirdparty/", certainty: attested, retrieved: primary, as_of: "2023-12"}
  - {field: stage, source: "https://webkit.org/tracking-prevention/", certainty: attested, retrieved: primary, as_of: "2026-08-11"}
  - {field: stage, source: "https://privacysandbox.google.com/blog/privacy-sandbox-next-steps", certainty: attested, retrieved: primary, as_of: "2025-04-22"}
  - {field: stage, source: "https://www.ftc.gov/system/files/ftc_gov/pdf/3-Skiera-Economic-Impact-of-Opt-in-versus-Opt-out-Requirements-for-Personal-Data-Usage.pdf", certainty: independent, retrieved: primary, as_of: "2023-04"}
  - {field: stage, source: "https://www.usenix.org/system/files/usenixsecurity24-mohamed.pdf", certainty: independent, retrieved: primary, as_of: "2024-08-14"}
  - {field: stage, source: "https://www.adjust.com/ja/resources/ebooks/japan-app-trends-2024/", certainty: vendor, retrieved: primary, as_of: "2024-Q1"}
  - {field: stage, source: "https://marketing.itmedia.co.jp/mm/articles/2409/09/news063.html", certainty: vendor, retrieved: primary, as_of: "2024-Q1"}
predictions:
  - {claim: "2027年末までに、日本の主要広告主の間で計測の主軸がユーザー単位のトラッキングからMMM・インクリメンタリティ計測側へ寄る（業界団体・独立調査でその旨が確認できる）", by: "2027-12", resolved: null, outcome: null}
relations: []
sources:
  - https://developer.apple.com/app-store/user-privacy-and-data-use/
  - https://developer.apple.com/documentation/apptrackingtransparency
  - https://webkit.org/tracking-prevention/
  - https://webkit.org/blog/10247/new-webkit-features-in-safari-13-1/
  - https://privacysandbox.google.com/blog/privacy-sandbox-next-steps
  - https://privacysandbox.google.com/cookies/prepare/overview
  - https://www.ftc.gov/system/files/ftc_gov/pdf/3-Skiera-Economic-Impact-of-Opt-in-versus-Opt-out-Requirements-for-Personal-Data-Usage.pdf
  - https://www.usenix.org/system/files/usenixsecurity24-mohamed.pdf
  - https://www.adjust.com/ja/resources/ebooks/japan-app-trends-2024/
  - https://marketing.itmedia.co.jp/mm/articles/2409/09/news063.html
status: draft
updated: 2026-08-11
---

# 広告トラッキング制約の常態化

## 何が変わったか

ユーザー・端末を横断して行動を追跡し、精密なターゲティングと効果測定を行う——2010年代のデジタル
広告の前提だったこの手法が、規制とプラットフォームの制度変更で段階的に制約され、**制約がある状態が
例外ではなく常態**になった。

2018年5月25日に適用されたEU GDPRは、個人データ処理の適法根拠を定め、ダイレクトマーケティングに
関係するプロファイリングを含む処理への異議申立てを明文化している（[EUR-Lexの規則本文](https://eur-lex.europa.eu/eli/reg/2016/679/oj)、
2026-08-11 実読）。日本でも、個人情報保護委員会が個人データの第三者提供について、取得経緯の確認・
記録などの義務をガイドラインで具体化している（[第三者提供時の確認・記録義務編](https://www.ppc.go.jp/personalinfo/legal/guidelines_thirdparty/)、
2026-08-11 実読）。

さらに Apple の ATT（[event/apple-att](../events/apple-att.md)）では、iOS 14.5以降、他社データとの
紐づけ（トラッキング）とIDFAアクセスにユーザーの明示的許可が必要になった（[Apple 開発者文書](https://developer.apple.com/app-store/user-privacy-and-data-use/)、
2026-08-11 実読）。許可が無い場合のIDFA値、ハッシュ化メール等の代替識別子、第三者SDKにも適用範囲が及ぶことが明記されている。

Safari側では、WebKitが現在の出荷挙動として、ITPによる第三者Cookieのデフォルト全面ブロック、第三者
リファラのoriginへの縮小、リンク装飾に対するCookie有効期限の制限、スクリプト書き込み可能なストレージの
7日間上限などを説明している（[WebKit Tracking Prevention](https://webkit.org/tracking-prevention/)、
2026-08-11 実読）。Safari 13.1の公式リリース資料でも、第三者Cookieの全面ブロックと非CookieのWebサイト
データの期限を説明している（[WebKit Features in Safari 13.1](https://webkit.org/blog/10247/new-webkit-features-in-safari-13-1/)、
2026-08-11 実読）。

Chromeは、第三者Cookieを一律に廃止する方針へ一直線に進んだとはいえない。Googleは2025年4月、ユーザーが
第三者Cookieの扱いを選べる現在の方式を維持し、新しい単独プロンプトは導入しないと説明した。一方で、
シークレットモードでは第三者Cookieをデフォルトでブロックし、公式移行ガイドでは第三者Cookieが無い前提で
監査・破損テスト・Privacy Sandbox等への移行を案内している（[Chromeの方針更新](https://privacysandbox.google.com/blog/privacy-sandbox-next-steps)、
[第三者Cookie移行ガイド](https://privacysandbox.google.com/cookies/prepare/overview)、2026-08-11 実読）。
したがって、ブラウザ側の制約は常態化しているが、実装はブラウザごとに異なると記録する。

ATTの許可率に近い第三者測定として、Kraft・Skiera・Koschella（2023）は、19か国・数十億件規模の広告
インプレッションを使い、米国のApple向け追跡可能トラフィックがATT前の74%からATT後の17%へ下がったと報告した。
2023年4月の986アプリ・19か国の分析では、追跡率は18.26%〜38.71%、平均28.18%だった。これはユーザー個人の
単純な許可率ではなく、広告インプレッションで重み付けした「追跡可能トラフィック」の割合であり、データは
DSPの独自データを含むため、全iOSユーザー・全アプリの現在値には一般化しない（[研究論文PDF](https://www.ftc.gov/system/files/ftc_gov/pdf/3-Skiera-Economic-Impact-of-Opt-in-versus-Opt-out-Requirements-for-Personal-Data-Usage.pdf)、
2026-08-11 実読）。

2024年の独立研究は、許諾率そのものではなく、許諾を求める画面の設計が結果を左右しうることを示す。
USENIX Security Symposiumの研究は、App Storeの4,000件のiOSアプリを分析し、ATTの許諾アラートの59%に、
誤解を招く説明、追跡への誘因、分かりにくい用語、目的の欠落など、Appleの指針に反する4種類のダークパターンを
確認した。114人のユーザー調査でも、許可・拒否が何を意味するかの誤解が観測されている。したがって、
許諾率の時系列を比較するときは、国・カテゴリだけでなく、表示文言・事前説明・表示対象アプリの構成も交絡要因として
扱う（[USENIX論文PDF](https://www.usenix.org/system/files/usenixsecurity24-mohamed.pdf)、2026-08-11 実読）。

日本のカテゴリ別の近い指標としては、AdjustとSensor Towerの「モバイルアプリトレンド2024：日本版」がある。
同レポートを紹介した記事では、2024年第1四半期のATTオプトイン率について、ゲーム30%、フード＆ドリンク24%、
エンターテインメント23%とされ、フード＆ドリンクは前年同期の16%、エンターテインメントは20%から上昇したと報告されている。
ただし、これは計測ベンダーのデータであり、Kraftらの広告インプレッション加重の追跡可能トラフィックとも、
独立研究のユーザー許諾率とも同じ系列ではない。日本の独立したカテゴリ別時系列としては未確認である
（[Adjust/Sensor Towerの公式レポート](https://www.adjust.com/ja/resources/ebooks/japan-app-trends-2024/)、
[紹介記事](https://marketing.itmedia.co.jp/mm/articles/2409/09/news063.html)、2026-08-11 実読）。

## kind と stage の判定

**kind: regulation-driven とした。** 判定表の第1問「規制・制度の施行日・条文を指せるか」に対し、
ATT はプラットフォームの規約であって行政規制ではない——ここに迷いがある。だが事業者から見れば
「外部から強制された制度変更で、応答の選択肢がない」という構造は行政規制と同じ側にあり、
GDPR・個人情報保護法の第三者提供ルールという行政側の制約も同じ束に入るため、regulation-driven を採る。
tech-enabled（技術が可能にした変化）ではない——技術的には従来の手法のほうが「可能」で、
制度がそれを止めた。

**stage: peak とした。** 制約は撤回されず追加される方向で推移し、業界の標準的な前提として
一般化している。Safari/WebKitでは第三者Cookieのデフォルトブロックが出荷挙動として定着し、Chromeでは
一律廃止からユーザー選択へ方針が調整された。したがって「制約が無い状態に戻った」とは言えないが、
ブラウザ横断で同一の制約が適用されているわけでもない。独立した許可率・クッキー同期率の推移はなく、
ATTについては、追跡可能トラフィックの第三者研究が定量的な裏づけになる。ただし、広告インプレッション
ベースであり、国・アプリ・プロンプト表示条件による差があるため、**この stage 判定は定量と定性を
併用したもの**とする。Safari・Chromeを含むブラウザ横断の許可率・クッキー同期率は未確認である。

## 時間

始点は、GDPRが適用された `2018~` とした。GDPRの適用日（2018年5月25日）は規則本文で確認でき、
ATT（2021）でモバイルアプリ側に波及した。以降も第三者提供、アプリ識別子、SDK、ブラウザの扱いが
別々の制度・仕様で更新されているため、終点は `..`（継続中）とする。

## チャネルと伝播

この trend は特定チャネル発ではない（規制・制度の側から来ている）ので、`channels` は張っていない。
影響はチャネル横断に及ぶ——だから `market: cross-category`。

## 反証（これが偽なら何が観測されるか）

- これが「常態化」でなく一時的な振れなら、**主要プラットフォームのどれかが制約を実質的に
  巻き戻し**、ユーザー単位トラッキングの可用性が2018年以前の水準に戻る動きが観測されるはず。
  Chromeの2025年方針変更は一律廃止の反証側にあたるため、再検証時にも「撤回された制約」と
  「残った制約」を仕分ける必要がある
- 制約が実務に効いていないなら、**広告主側の計測手法の構成が変わっていない**はず（MMM・
  コンバージョンAPI・クリーンルームへの移行が起きない）。移行が観測されれば効いている

## 未着手

- Safari・Chromeのバージョン別挙動と、サイト側の対応状況を同じ定義で追跡する
- ATTの2024年以降の独立した許諾率測定と、日本のアプリ・カテゴリ別の独立時系列を探す。2024年の独立研究は
  許諾画面のダークパターンを測定し、日本のカテゴリ別数値は現時点ではベンダー資料のみである
- 応答する practice の整理: MMM 回帰・リテールメディア（[practice/retail-media](../practices/retail-media.md)）・
  ファーストパーティデータ活用を responds_to で繋ぐ
