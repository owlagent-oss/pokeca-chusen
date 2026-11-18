# ポケカ・トレカ抽選ナビ

ポケカ（ポケモンカード）の抽選販売・予約・再販情報のまとめサイト。全国＋名古屋・東海を厚めに。

- 公開：https://pokeca-chusen-navi.pages.dev （Cloudflare Pages。site/ の中身。main に push すると自動で反映）
- 準備中は `noindex` と robots.txt で検索に出さない。本公開のときに外す
- 広告（PR）は「PR」枠だけに出す。抽選情報の一覧には混ぜない

## 抽選データの更新
- 正本は買取ナビの `notes/lotteries.json`（見回りは1回で、両方のサイトに使う）
- `python3 tools/sync.py <買取ナビの notes/lotteries.json>` で `site/index.html` に埋め込む → main に push
- 抽選ナビだけに出す全国の抽選は `data/extra.json`（同じ店・同じ商品は買取ナビ側を優先）
- 出どころ（src）は外に出さない。お店の告知で確かめたもの（verified）は「確認済み」、ほかは「要確認」と表示
