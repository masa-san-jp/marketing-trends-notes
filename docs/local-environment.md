# ローカル環境の準備

X APIの認証情報はリポジトリに保存しない。共有するのは [`.env.example`](../.env.example) だけで、
実際の値はローカルの `.env` に置く。`.env` は `.gitignore` で除外している。

## 初回セットアップ

リポジトリの検証ツールは `requirements.txt` に記載したPython依存関係を使う。まず仮想環境を作り、
依存関係をインストールする。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

グラフと監査の検証を実行する。

```bash
python tools/build_graph.py --check
python tools/observe_social.py --check
python tools/audit.py
```

空気感観測に関係する検証を一括で確認する場合は、次のdry-runを使う。既定ではネットワークへ出ず、
Xトークンがない場合もスキップとして続行する。

```bash
python tools/run_atmosphere_pipeline.py --dry-run --skip-rss
```

Xトークンがない場合でも、公開検索関心の代理観測はGoogle Trends Japan RSSで実行できる。
これはSNS投稿や世論を取得するものではなく、HTTP取得時刻・キャッシュ指示・上位検索語と、
前回スナップショットとの差分を保存するための補助面である。

```bash
python tools/observe_google_trends.py --output /path/to/current.json --summary
python tools/observe_google_trends.py \
  --compare /path/to/current.json \
  --output /path/to/next.json --summary
```

検証とRSS取得を一度に行い、結果をDrive配下へ蓄積する場合は、保存先を明示して実行する。
`--collect-rss`を付けない限り、パイプラインはRSSへ接続しない。

```bash
python tools/run_atmosphere_pipeline.py --collect-rss \
  --output-dir "/Users/masa/マイドライブ/AI-Agent-Pipeline/Agentic-Art-Output/marketing-atmosphere/02_evidence" \
  --compare "/path/to/previous.json" --summary
```

このランナーが更新するのは、指定したRSSスナップショットと任意の実行レポートだけである。
Driveのevidence ledgerや観測判断は自動生成せず、RSSの内容を確認してから記録する。

`--compare` は同じRSS範囲の前回JSONを指定する。結果は「検索関心の時間帯別の回転」を見るために使い、
SNS上の会話量、感情の方向、社会全体の代表性へ変換しない。

その後、X APIを使う場合だけ `.env` を準備する。

```bash
cp .env.example .env
chmod 600 .env
$EDITOR .env
python tools/check_x_env.py
```

`.env` の `X_BEARER_TOKEN` に、X Developer Console の App の Keys and tokens で発行した
Bearer Tokenを設定する。公開データを読むX API v2のアプリ専用認証ではBearer Tokenを使う。
[X公式のBearer Token説明](https://docs.x.com/fundamentals/authentication/oauth-2-0/bearer-tokens)
と [v2認証の対応表](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
を参照。

トークンがない状態で `tools/check_x_env.py` を実行すると、エラーにせず
`SKIP: X_BEARER_TOKEN がないため、Xリサーチをスキップして続行します` と表示して終了する。
X以外の調査・検証を止めないための既定動作である。X APIを必須にする作業だけは
`python3 tools/check_x_env.py --require-token` を使う。

## 変数

| 変数 | 必須 | 用途 |
|---|---:|---|
| `X_BEARER_TOKEN` | 初回のAPI利用時 | 公開データを読むためのアプリ専用Bearer Token |
| `X_API_BASE_URL` | 任意 | APIのベースURL。既定値は `https://api.x.com` |
| `X_API_TIMEOUT_SECONDS` | 任意 | APIクライアントのタイムアウト秒。既定値は `30` |

`tools/check_x_env.py` はトークンの有無、URL、タイムアウト、`.env` の権限を確認するだけで、
トークンの値を表示したり、APIへリクエストしたりしない。シェルで環境変数を直接設定した場合は
`.env` よりそちらを優先する。

現在の観測ツールはJSONLを検証・集計する段階で、X APIの自動取得はまだ行わない。認証情報を
準備しても、それだけで現在のXトレンドを取得・保存することはない。
