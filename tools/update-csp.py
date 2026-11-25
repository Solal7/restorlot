"""Recompute the CSP hashes in vercel.json from the inline <script> and <style> in index.html.
Run after any edit to index.html: python3 tools/update-csp.py"""
import re, hashlib, base64, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()
def hashes(tag):
    return " ".join("'sha256-%s'" % base64.b64encode(hashlib.sha256(m.encode()).digest()).decode()
                    for m in re.findall(r"<%s>(.*?)</%s>" % (tag, tag), html, re.S))
vj = root / "vercel.json"
cfg = json.loads(vj.read_text())
for h in cfg["headers"][0]["headers"]:
    if h["key"] == "Content-Security-Policy":
        v = re.sub(r"script-src [^;]*", "script-src 'self' " + hashes("script"), h["value"])
        h["value"] = re.sub(r"style-src [^;]*", "style-src 'self' " + hashes("style"), v)
vj.write_text(json.dumps(cfg, indent=2) + "\n")
print("CSP hashes updated")
