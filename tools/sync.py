"""抽選データを site/index.html に埋め込む。
使い方: python3 tools/sync.py <買取ナビの notes/lotteries.json のパス>
- 正本は買取ナビの notes/lotteries.json（見回りは1回、データは共通）
- 外に出さない項目（src：どこから拾ったか）は落とす
"""
import json, re, sys, os
src = sys.argv[1]
d = json.load(open(src, encoding="utf-8"))
keep = ["pref","shop","item","game","method","deadline","time","result","buy","condition","url","verified"]
items = [{k: x[k] for k in keep if x.get(k)} for x in d["items"]]
out = {"checked": d.get("checked",""), "items": items}
p = os.path.join(os.path.dirname(__file__), "..", "site", "index.html")
s = open(p, encoding="utf-8").read()
js = "const DATA=" + json.dumps(out, ensure_ascii=False, separators=(",",":")).replace("</","<\\/") + ";"
s2 = re.sub(r"/\*DATA-START\*/.*?/\*DATA-END\*/", lambda m: "/*DATA-START*/"+js+"/*DATA-END*/", s, flags=re.S)
assert s2 != s or js in s, "埋め込み場所が見つからない"
open(p, "w", encoding="utf-8").write(s2)
print(f"{len(items)}件を埋め込み（最終確認 {out['checked']}）")
