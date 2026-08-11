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
  - {field: time, source: "https://eur-lex.europa.eu/eli/reg/2016/679/oj", certainty: attested, retrieved: primary, as_of: "2018-05-25"}
  - {field: stage, source: "https://www.ppc.go.jp/personalinfo/legal/guidelines_thirdparty/", certainty: attested, retrieved: primary, as_of: "2023-12"}
predictions:
  - {claim: "2027年末までに、日本の主要広告主の間で計測の主軸がユーザー単位のトラッキングからMMM・インクリメンタリティ計測側へ寄る（業界団体・独立調査でその旨が確認できる）", by: "2027-12", resolved: null, outcome: null}
relations: []
sources:
  - https://developer.apple.com/app-store/user-privacy-and-data-use/
  - https://developer.apple.com/documentation/apptrackingtransparency
status: draft
updated: 2026-08-10
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

**未確認**: Safari ITPの段階的な制約と、Chromeのサードパーティクッキー方針・その転換は、この作業では
一次資料まで追えていない。したがって、ブラウザ側の制約がモバイル側と同じ強さ・速度で進んだとは断定しない。

## kind と stage の判定

**kind: regulation-driven とした。** 判定表の第1問「規制・制度の施行日・条文を指せるか」に対し、
ATT はプラットフォームの規約であって行政規制ではない——ここに迷いがある。だが事業者から見れば
「外部から強制された制度変更で、応答の選択肢がない」という構造は行政規制と同じ側にあり、
GDPR・個人情報保護法の第三者提供ルールという行政側の制約も同じ束に入るため、regulation-driven を採る。
tech-enabled（技術が可能にした変化）ではない——技術的には従来の手法のほうが「可能」で、
制度がそれを止めた。

**stage: peak とした。** 制約は撤回されず追加される方向で推移し、業界の標準的な前提として
一般化している。ただし peak の判定表が求める「数字の高原状態」を示す独立した定量（例: 許可率・
クッキー同期率の推移）は執筆環境から取れておらず、**この stage 判定は定性による**。
**未確認**: 定量の裏づけ。再検証時（2027-02まで）に許可率・対応済み広告主比率の独立調査を探す。

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
  Chrome のクッキー廃止撤回（未確認）がこの反証の部分的な成立である可能性があり、再検証時に
  「撤回された制約」と「残った制約」を仕分ける必要がある
- 制約が実務に効いていないなら、**広告主側の計測手法の構成が変わっていない**はず（MMM・
  コンバージョンAPI・クリーンルームへの移行が起きない）。移行が観測されれば効いている

## 未着手

- Safari ITP・Chromeのサードパーティクッキー方針と転換の一次確認（ブラウザ側の制約の整理）
- ATT 許可率の独立した実測を探す（ベンダー数字しか無い可能性が高い——その場合は vendor と明記して置く）
- 応答する practice の整理: MMM 回帰・リテールメディア（[practice/retail-media](../practices/retail-media.md)）・
  ファーストパーティデータ活用を responds_to で繋ぐ
