"""Copy only what the page needs into site/ (the folder that gets deployed).

Run from the project root:  python build-site.py
It reads index.html and styles.css, collects every local file they reference,
and recreates site/ from scratch. Edit the root files, then re-run this.
"""
import re, shutil
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "site"
DOMAIN = "https://blueskyfarm.site/"

html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")

refs = {"index.html"} | set(re.findall(r'(?:src|href|poster)="([^"#:]+)"', html))              # local src/href/poster
refs |= {u[len(DOMAIN):] for u in re.findall(r'content="([^"]+)"', html) if u.startswith(DOMAIN) and u != DOMAIN}
refs |= set(re.findall(r'url\(["\']?([^"\')#:]+)["\']?\)', css))               # url() in CSS

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
missing = []
for rel in sorted(refs):
    src = ROOT / rel
    if not src.is_file():
        missing.append(rel)
        continue
    dst = OUT / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

total = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
for f in sorted(OUT.rglob("*")):
    if f.is_file():
        print(f"{f.relative_to(OUT).as_posix():32s} {f.stat().st_size / 1024:8.1f} KB")
print(f"{'TOTAL':32s} {total / 1024:8.1f} KB ({total / 1048576:.2f} MB)")
if missing:
    raise SystemExit(f"Missing referenced files: {missing}")
