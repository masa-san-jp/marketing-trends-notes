# SNS上の空気感観測

この文書は、SNS上で人を強く惹きつける話題の熱、感情、言い回し、模倣、参加衝動を記録する
ための手順と形式を定める。

ここで記録するのは「社会全体で何％の人がそう思っているか」ではない。特定プラットフォーム、
特定の表示条件、特定のクラスターにおける高い引力を、偏り込みの観測対象として扱う。偏りを
代表性へ補正して消すのではなく、観測範囲とともに残す。

## トレンドとの違い

| 層 | 何を記録するか | 言ってよいこと | 言ってはいけないこと |
|---|---|---|---|
| `trend` | 外部資料や複数チャネルで裏付けられる需要・社会の変化 | 変化の存在、段階、伝播 | 1つの投稿や一時的な盛り上がりだけで社会変化と断定する |
| `atmosphere_signal` | 特定SNSで人を惹きつける高い注意、感情、文化的フック | その観測範囲で何が反復され、何への参加や反応を誘っているか | 社会全体の世論・普及率・代表的意見とみなす |

`atmosphere_signal` はトレンドの下位分類ではない。トレンドに昇格する場合は、独立した根拠、
時間の継続、別チャネルでの確認を追加して、通常のエンティティとして別途記録する。

## Xを観測するときの前提

X の Trends はフォロー、興味、位置情報などにより個人化され、位置を指定した表示もある。
X はトレンド判定に投稿本文、投稿者の情報や文脈、継続時間、トレンド化の見込みなど複数の
シグナルを使うと説明している。そのため、同じ日でも表示条件によって見える空気は変わる。
観測時には `geo`、`view`、`query_scope`、時刻を必ず残す。

参照: [X Trends FAQ](https://help.x.com/en/using-x/x-trending-faqs)、
[X Trends Recommendations](https://help.x.com/en/resources/recommender-systems/trends-recommendations)

## JSONL形式

1行を1観測とする。まだ実際のX観測を投入していない場合でも、空のログは有効である。この
仕組みの導入だけでは「現在のXトレンド」を主張しない。

必須フィールドは次のとおり。

```json
{
  "id": "x-2026-08-12-example",
  "platform": "x",
  "observed_window": {
    "start": "2026-08-12T09:00:00+09:00",
    "end": "2026-08-12T12:00:00+09:00"
  },
  "geo": "japan",
  "view": "trending_japan",
  "query_scope": "固定した検索語・ハッシュタグ・Explore位置",
  "sample": {
    "posts_observed": 1200,
    "unique_accounts": 430,
    "collection_method": "manual export / approved API",
    "method_version": "atmosphere-v1"
  },
  "signal": {
    "attention": "high",
    "affects": ["fascination", "anxiety"],
    "cultural_form": "反復される短い言い回しと模倣投稿",
    "hooks": ["参加したくなる", "怒りを共有したくなる"],
    "persistence": "burst",
    "spread": "within_cluster"
  },
  "interpretation": "X上で人を惹きつける空気の強まり",
  "scope": {
    "population_claim": false,
    "bias_notes": ["X上の公開投稿の観測であり、社会全体の比率ではない"]
  },
  "examples": [
    {
      "url": "https://x.com/example/status/123",
      "role": "hook",
      "note": "短い言い回しが反復される"
    }
  ],
  "sources": ["https://help.x.com/en/using-x/x-trending-faqs"],
  "observed_by": "masa"
}
```

上の値は形式を示す例であり、実際の観測結果ではない。実ログには実在するURLと、観測者が
確認した範囲だけを書く。

検証で固定する値は次のとおり。

- 現在の対応プラットフォームは `x`。追加時はスキーマと検証器を同時に更新する。
- `attention` は `low` / `medium` / `high`、`persistence` は `burst` / `short` /
  `persistent` / `unknown`、`spread` は `within_cluster` / `cross_cluster` /
  `cross_platform` / `unknown`。
- `affects` と `hooks` は空にしない。感情の極性だけでなく、魅力、不安、怒り、模倣、参加など
  何が人を引きつけるのかを記述する。
- `scope.population_claim` は必ず `false`。`bias_notes` も必須とする。
- `examples` は最大5件、URLは `https` のみ。本文の丸ごと転載はせず、URL、役割、短い観測メモ
  だけを残す。
- `posts_observed` は観測した投稿数、`unique_accounts` は重複を除いたアカウント数で、推定値
  なら `collection_method` に推定方法を書く。`unique_accounts` は投稿数を超えない。

## 観測ワークフロー

1. 先に観測範囲を固定する。Exploreの位置、検索語、ハッシュタグ、言語、期間を `query_scope`
   と `view` に書く。
2. 同じ範囲を複数時点で見る。単発の大きさではなく、反復、模倣、感情の束、参加しやすい型、
   クラスターを越える広がりを記録する。
3. `signal` に「何が強いか」を書く。肯定・否定のセンチメント1軸に潰さず、惹きつけるフック、
   不安や怒りなどの affect、文化的な形式を分ける。
4. `scope` に、公開投稿・検索結果・個人化表示などの限界と偏りを書く。
5. `python3 tools/observe_social.py --check` で検証する。必要なら `--summary` で複数観測を集計
   する。
6. 社会的なトレンドとして使うときは、独立ソースや別チャネルの観測を追加し、空気感ログだけ
   から一般化しない。

ログの既定位置は `data/social-observations.jsonl`。観測者は必要に応じて手動記録や承認済みの
APIエクスポートを取り込めるが、このリポジトリはXの取得認証やスクレイピングを自動化しない。
