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
  none_reason: "wbsearchentities で「ショート動画」（ja）と short-form video（en）を検索。現象そのものの項目は無く、該当は Q139548224 short video addiction と学術論文3件のみ。依存の概念は本 trend と別物なので採らない（2026-08-10 検索実施）"
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
  - {field: stage, source: "https://www.soumu.go.jp/main_content/001079136.pdf", certainty: independent, retrieved: primary, as_of: "2025-12"}
  - {field: stage, source: "https://www.soumu.go.jp/iicp/research/results/media_usage-time.html", certainty: independent, retrieved: primary, as_of: "2025-12"}
predictions:
  - {claim: "2027年末時点でも、国内若年層の動画視聴でショート形式が支配的であり続ける（総務省調査系の利用率が前年割れしない）", by: "2027-12", resolved: null, outcome: null}
  - {claim: "令和8年度調査（2026年12月実施・2027年6月公表見込み）で TikTok の10代利用率が67.9％を下回らない", by: "2027-07", resolved: null, outcome: null}
channel_scope:
  status: mapped
  note: null
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

規模は総務省の[令和7年度 情報通信メディアの利用時間と情報行動に関する調査](https://www.soumu.go.jp/iicp/research/results/media_usage-time.html)
（[調査結果概要 PDF](https://www.soumu.go.jp/main_content/001079136.pdf)）で確認した。13〜79歳の男女1,800人・
全国125地点のランダムロケーションクォータサンプリング・訪問留置、調査対象期間は2025年12月1日〜7日。

- インターネットの利用項目のうち、**全年代で平日・休日ともに「動画投稿・共有サービスを見る」の平均利用時間が最長**。
  平日の全年代は54.5分で、10代127.2分・20代107.1分と若年層で突出する
- オンデマンド型の動画共有サービスの利用率は全年代84.7％、**10代から50代では90％超**
- TikTok の利用率は全年代36.7％、10代67.9％・20代61.5％・30代44.7％・40代42.6％・50代32.2％・60代21.2％・70代11.1％。
  報告書自身が「『TikTok』の利用率は増加しており、10代で67.9％と最も高い利用率」と記述している
- YouTube の利用率は全年代81.5％で、10代から40代で90％超

**未確認**: この調査は**サービス単位（TikTok・YouTube）とサービス種別単位**で測っており、
**「ショート形式かどうか」を分けて測っていない**。したがって上記は「動画視聴がネット利用の最大項目である」
ことと「ショート動画を主戦場とするサービスの利用率が高い・伸びている」ことの裏づけであって、
**視聴時間に占めるショート形式の比率を直接に示すものではない**。形式別の内訳を持つ独立した出典は
2026-08時点で見つかっていない。

## kind と stage の判定

**kind: tech-enabled とした。** 判定表の第2問——TikTok 型のレコメンドフィード（機能のローンチ）が
先行し、それ無しでこの視聴形式は成立しない。需要側の変化（可処分時間の奪い合い）はあるが、
形式そのものは技術・プロダクトが規定した。

**stage: peak とした。** 「ショート動画」は一般紙・地上波が説明なしで使う語になっており、
判定表の peak の目安（主流化・説明不要）を満たす。加えて総務省調査で、動画視聴がネット利用項目の
最長であること・オンデマンド型動画共有の利用率が10代から50代で90％超であることを確認した（上記）。

**ただし peak と growing の線引きは、この出典だけでは決まらない。** 報告書は TikTok の利用率を
「増加しており」と記述しており、伸びているものを peak と呼ぶことになる。ここは**利用率（どれだけの人が
使ったか）と主流化（説明なしで通じるか）を別の軸として扱い、後者で peak を採った**という判断である。
利用率だけで判定するなら growing が正しい。declining でないことは、増加の記述から確実に言える。

**未確認**: 経年の数値（全年代 TikTok 利用率の年次推移）。PDF のグラフ部分は自動抽出では年次と数値の
対応が崩れるため、確実に読めた令和7年度の断面だけを採った。推移は同ページの集計表（xlsx）を開けば
取れるので、次の再検証タスクで埋める。

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
  → 2026-08-10 に総務省調査を実読して判定。10代の TikTok 利用率67.9％・オンデマンド型動画共有の
  10代から50代90％超で、**この反証は成立しなかった**（ただし形式別の内訳ではない点は上記のとおり）
- 「ショート動画」がプラットフォームの売り文句に過ぎない（kind: vendor-pushed が正しい）なら、
  **広告費・視聴時間の独立した統計に形式別の伸びが現れない**はず
- 既に declining なら、**利用時間の前年割れ**が観測されるはず（predictions に置いた）

## 未着手

- 形式別（ショート／ロング）の視聴時間内訳を持つ独立した出典。**この trend の名前が主張していることを
  直接に測った出典が、まだ1本も無い**
- 総務省調査の集計表（xlsx）から TikTok 利用率の経年推移を取り、stage を利用率の軸でも判定する
- 応答する practice（ショート動画運用・ショート広告）を responds_to で繋ぐ——現状この trend は
  打ち手に落ちていない（audit が指摘する状態のまま）
- channel/instagram（Reels）の追加と伝播の記録
- 「発見の主導権がレコメンドに移った」ことを独立に示す出典
