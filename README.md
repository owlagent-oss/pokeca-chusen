# ポケカ・トレカ抽選ナビ

ポケカ（ポケモンカード）の抽選販売・予約・再販情報のまとめサイト。全国＋名古屋・東海を厚めに。

- 公開：https://pokeca-chusen-navi.pages.dev （Cloudflare Pages。site/ の中身。main に push すると自動で反映）
- 2026-11-18 から検索に出す設定（noindex と robots.txt の Disallow を外した）。sitemap.xml あり
- 必須ページ：about.html（運営者情報・お問い合わせ）、privacy.html、ad-policy.html（共通の見た目は pages.css）。お問い合わせのメールは about.html の CONTACT_MAIL に入れる
- PR枠は、index.html の prVideo に data-href（アフィリエイトのリンク）を入れるまで丸ごと非表示
- 広告（PR）は「PR」枠だけに出す。抽選情報の一覧には混ぜない

## 抽選データの更新
- 正本は買取ナビの `notes/lotteries.json`（見回りは1回で、両方のサイトに使う）
- `python3 tools/sync.py <買取ナビの notes/lotteries.json>` で `site/index.html` に埋め込む → main に push
- 抽選ナビだけに出す抽選は `data/extra.json`（全国分＋東海でまとめサイトから拾った分。同じ店・同じ商品は買取ナビ側を優先）
- 東海の拾い先：cardchusen.com/pokeka、nyuka-now.com/archives/2459、pokeca-navi.jp/prefectures/aichi/ ほか。拾ったら店の告知で確かめて verified を付ける
- 出どころ（src）は外に出さない。お店の告知で確かめたもの（verified）は「確認済み」、ほかは「要確認」と表示
