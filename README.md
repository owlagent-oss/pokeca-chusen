# ポケカ・トレカ抽選ナビ

ポケカ（ポケモンカード）の抽選販売・予約・再販情報のまとめサイト。全国＋名古屋・東海を厚めに。

- 公開：https://pokeca-chusen-navi.pages.dev （Cloudflare Pages のプロジェクト名 pokeca-chusen-navi。site/ の中身）
- 公開のしくみ：main に push すると GitHub Actions（.github/workflows/deploy.yml）が `wrangler pages deploy site` で自動公開。GitHub の Settings → Secrets and variables → Actions に CLOUDFLARE_API_TOKEN と CLOUDFLARE_ACCOUNT_ID が必要（2026-11-18 追加。それまでは手でアップロードした11/17夜の試作版のまま止まっていた）
- 2026-11-18 から検索に出す設定（noindex と robots.txt の Disallow を外した）。sitemap.xml あり
- 必須ページ：about.html（運営者情報・お問い合わせ）、privacy.html、ad-policy.html（共通の見た目は pages.css）。お問い合わせのメールは about.html の CONTACT_MAIL に入れる
- PR枠は、index.html の prVideo に data-href（アフィリエイトのリンク）を入れるまで丸ごと非表示
- 広告（PR）は「PR」枠だけに出す。抽選情報の一覧には混ぜない

## 抽選データの更新
- 正本は買取ナビの `notes/lotteries.json`（見回りは1回で、両方のサイトに使う）
- `python3 tools/sync.py <買取ナビの notes/lotteries.json>` で `site/index.html` に埋め込む → main に push
- 抽選ナビだけに出す抽選は `data/extra.json`（全国分＋東海でまとめサイトから拾った分。同じ店・同じ商品は買取ナビ側を優先）
- まとめサイト巡回（予定タスク「抽選ナビ まとめサイト巡回」1日3回 8:40・12:40・16:40）の見る先：
  - cardchusen.com（/pokeka・/onepiece ほか。全トレカ・東海に強い）
  - toreka-chusen.com（/category/pokeka/ ほか）
  - pokeca-navi.jp（/prefectures/aichi/・gifu・mie と /lotteries/）
  - chusen-media.vercel.app
  - nyuka-now.com（抽選まとめ記事）
  - toreca-entry.com
- 東海（愛知・岐阜・三重）の抽選 → 買取ナビの notes/lotteries.json（正本）。全国は data/extra.json（オンライン抽選と全国チェーン一括のもの中心）
- まとめサイトから拾ったものは「要確認」。お店の告知で確かめられたら verified を付ける
- 出どころ（src）は外に出さない。お店の告知で確かめたもの（verified）は「確認済み」、ほかは「要確認」と表示
