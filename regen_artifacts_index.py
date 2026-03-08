#!/usr/bin/env python3
"""
regen_artifacts_index.py
Regenerates artifacts/index.html from all .html files in artifacts/ (except index.html).
Preserves existing order by using a manual sort list; unknown files appended at end.
Run from repo root: python3 regen_artifacts_index.py
"""

from pathlib import Path
import re

ARTIFACTS = Path("/Users/steve/tilde-steve/artifacts")

# Desired display order — newest first
ORDER = [
    "ai-fye-v6.html",
    "ai-literacy-learners-permit.html",
    "ai-literacy-commercial-license.html",
    "ai-literacy-wednesday-sessions.html",
    "ai-literacy-artifacts.html",
    "AIX-Architecture-Overview.html",
    "herkimer-county-27feb.html",
    "Africa_Trip_Overview.html",
]

def get_title(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r'<title>(.*?)</title>', text, re.I)
    return m.group(1).strip() if m else path.stem

# Collect all html files except index
all_files = {f.name: f for f in ARTIFACTS.glob("*.html") if f.name != "index.html"}

# Build ordered list: ORDER first, then anything not in ORDER
ordered = [f for f in ORDER if f in all_files]
remainder = sorted(f for f in all_files if f not in ORDER)
final = ordered + remainder

entries = []
for fname in final:
    title = get_title(all_files[fname])
    entries.append(f'    <li><a href="{fname}">{title}</a></li>')

# Read existing index to preserve nav/header — just replace the <ul>...</ul> block
idx_path = ARTIFACTS / "index.html"
content = idx_path.read_text(encoding="utf-8")

new_list = "<ul>\n" + "\n".join(entries) + "\n  </ul>"
replaced = re.sub(r'<ul>.*?</ul>', new_list, content, count=1, flags=re.DOTALL)

if replaced == content:
    print("WARNING: no <ul>...</ul> found to replace — check artifacts/index.html structure")
else:
    idx_path.write_text(replaced, encoding="utf-8")
    print(f"Done: {len(final)} artifacts listed")
    for f in final:
        print(f"  {f}")
