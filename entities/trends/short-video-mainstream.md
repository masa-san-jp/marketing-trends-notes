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
  - {field: stage, source: "https://www.soumu.go.jp/menu_news/s-news/01iicp01_02000125.html", certainty: independent, as_of: "2024", retrieved: summary}
predictions:
  - {claim: "令和7年度以降の総務省調査で、TikTok の全年代利用率が33.2%を下回らない", by: "2027-12", resolved: null, outcome: null}
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

規模の目安として、総務省情報通信政策研究所「情報通信メディアの利用時間と情報行動に関する調査」の
令和6年度調査（2025年6月公表・[報道資料](https://www.soumu.go.jp/menu_news/s-news/01iicp01_02000125.html)）
では、動画共有系の利用率が YouTube 80.8%・TikTok 33.2%（全年代）。TikTok は10代 65.7%・20代 58.7%で、
全年代では前年から約5.4ポイント増とされる。同調査は令和6年度から対象を13〜69歳から13〜79歳に拡大している。

**原典未読**: 上の数字は WebSearch の要約経由で得たもので、報告書本体
（[PDF](https://www.soumu.go.jp/main_content/001017160.pdf)）を読んでいない
（`retrieved: summary`。この環境から総務省サイトに到達できない——[sources-directory](../../docs/sources-directory.md)）。
**未確認**: 調査の実施時期（`as_of` は年度で置いた。令和6年度調査の実査月は確認していない）、
n と抽出方法、「前年から5.4ポイント増」の前年値。要約は年度違いや丸めが混ざるので、
原典が読めるようになったら最初に突き合わせる。

**未確認**: そもそも「ショート動画の利用率」を直接測った統計を、この調査は持っていない可能性が高い。
上の数字は**プラットフォーム別の利用率**であって、形式（縦型短尺）別ではない。TikTok の利用率で
ショート動画の主流化を語るのは代理指標であり、YouTube 80.8% のうち Shorts が何割かは分からない。
形式別の統計を探すのが次の課題。

## kind と stage の判定

**kind: tech-enabled とした。** 判定表の第2問——TikTok 型のレコメンドフィード（機能のローンチ）が
先行し、それ無しでこの視聴形式は成立しない。需要側の変化（可処分時間の奪い合い）はあるが、
形式そのものは技術・プロダクトが規定した。

**stage: peak とした。** 判定表の peak の目安は「主流化・一般紙や地上波が説明なしで使う・数字は
高原状態」。前2つは満たす。3つ目については、TikTok 全年代33.2%が前年比+5.4ポイントで**まだ伸びて
いる**——これだけ見れば `growing` に見える。それでも peak を採るのは、代理指標である TikTok 単体の
利用率より、YouTube 80.8% を含む動画共有系全体の到達がすでに天井に近いためだが、
**この判断は形式別の統計が無いまま行っている**（上記）。
**未確認**: 形式別の視聴時間シェア。これが取れれば growing / peak は数字で決まる。

## 時間

始点は `2020~`（およそ）。TikTok の国内普及は2019年以前に始まっているが、「主流化」と呼べる規模に
なった時期としてコロナ禍の在宅時間拡大期を目安に置いた。**未確認**: この時期の特定を裏づける
時系列データ（総務省調査の年次推移が読めれば確定できる）。終点は `..`（継続中）。

## チャネルと伝播

発生チャネルは [channel/tiktok](../channels/tiktok.md)（`originated_on`）。同形式が
[channel/youtube](../channels/youtube.md)（Shorts）へ伝播した（`spread_to`）——プラットフォーム側が
形式を模倣して実装した型の伝播で、ユーザーが移動した型ではない点が美術の伝播と違う。
**未確認**: Instagram Reels への伝播も同型だが、channel/instagram をまだ置いていないので張っていない
（孤児 stub を作らないため。Reels を扱う調査が入る時に置く）。

## 反証（これが偽なら何が観測されるか）

- 「若年層で主流」が誇張なら、**10代のショート形式利用が過半に達していない**はず。
  令和6年度調査の TikTok 10代 65.7% はこの反証を（代理指標としては）くぐり抜けている
- 「ショート動画」がプラットフォームの売り文句に過ぎない（kind が `vendor-pushed` である）なら、
  **利用率が業界発表以外の独立した統計に現れない**はず。総務省調査に現れているので、
  この反証は成立していない——`tech-enabled` を採る根拠のひとつ
- **peak ではなく growing なら、次年度調査でも TikTok 利用率が数ポイント単位で伸び続ける**はず。
  前年比+5.4ポイントはむしろ growing 側の証拠で、stage を動かす可能性がある。
  これが predictions の判定対象でもある（33.2% を下回らないかどうか）
- 既に declining なら、**次年度調査で前年割れ**が観測されるはず

## 未着手

- **総務省報告書本体の実読**（`retrieved: summary` → `primary` への昇格）。数字の突き合わせと、
  実査時期・n・前年値の確定。この環境では総務省サイトに到達できないので、ネットワーク許可が要る
- **形式別（縦型短尺）の統計を探す**。いま使っているのはプラットフォーム別の代理指標で、
  stage 判定の弱点がここにある
- 応答する practice（ショート動画運用・ショート広告）を responds_to で繋ぐ——現状この trend は
  打ち手に落ちていない（audit が指摘する状態のまま）
- channel/instagram（Reels）の追加と伝播の記録
- 「発見の主導権がレコメンドに移った」ことを独立に示す出典
