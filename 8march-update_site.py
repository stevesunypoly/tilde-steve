#!/usr/bin/env python3
"""
update_site.py — run from repo root
  python3 update_site.py

1. Converts any unconverted .md files in transcripts/ to .html
2. Regenerates transcripts/index.html
3. Copies ai-fye-v6.html (in repo root) to artifacts/
4. Updates artifacts/index.html: removes old faculty-invitation link, adds v6 entry
"""

import os, re, sys, shutil, subprocess
from pathlib import Path

REPO_ROOT      = Path("/Users/steve/tilde-steve")
TRANSCRIPTS    = REPO_ROOT / "transcripts"
ARTIFACTS      = REPO_ROOT / "artifacts"
CONVERT_SCRIPT = REPO_ROOT / "convert_transcript.py"
SOURCE_HTML    = REPO_ROOT / "ai-fye-v6.html"   # adjust if file is elsewhere
ARTIFACT_DEST  = ARTIFACTS / "ai-fye-v6.html"
PREV_URL       = "https://stevesunypoly.github.io/tilde-steve/artifacts/ai-fye-faculty-invitation.html"

def slugify(name):
    name = os.path.splitext(os.path.basename(name))[0]
    name = name.replace(' ', '-')
    return re.sub(r'[^a-zA-Z0-9\-_]', '', name).lower()

# ── 1. Convert new .md transcripts ───────────────────────────────────────────
print("\n── Converting transcripts ──")
for md in sorted(TRANSCRIPTS.glob("*.md")):
    html = TRANSCRIPTS / (slugify(md.name) + ".html")
    if html.exists():
        print(f"  skip (exists): {html.name}")
        continue
    r = subprocess.run(["python3", str(CONVERT_SCRIPT), str(md), str(TRANSCRIPTS)],
                       capture_output=True, text=True)
    if r.returncode == 0:
        print(f"  ok: {html.name}")
    else:
        print(f"  ERROR: {md.name}\n{r.stderr}")

# ── 2. Regenerate transcripts/index.html ─────────────────────────────────────
print("\n── Regenerating transcripts/index.html ──")
html_files = sorted([f for f in TRANSCRIPTS.glob("*.html") if f.name != "index.html"], reverse=True)
entries = []
for f in html_files:
    text = f.read_text(encoding="utf-8")
    m = re.search(r'<title>(.*?)</title>', text, re.I)
    title = m.group(1).strip() if m else f.stem
    entries.append(f'    <li><a href="{f.name}">{title}</a></li>')

index = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Transcripts — Steve Brizel</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
<div class="container">
  <nav>
    <a href="../index.html">Home</a> |
    <a href="../bio.html">Bio</a> |
    <a href="../teaching.html">Teaching</a> |
    <a href="../research.html">Research</a> |
    <a href="../artifacts/index.html">Artifacts</a> |
    <a href="index.html">Transcripts</a>
  </nav>
  <h1>Transcripts</h1>
  <p>Working session transcripts with Claude and ChatGPT — the provenance record for artifacts and research outputs.</p>
  <ul>
{chr(10).join(entries)}
  </ul>
</div>
</body>
</html>
"""
(TRANSCRIPTS / "index.html").write_text(index, encoding="utf-8")
print(f"  written ({len(html_files)} entries)")

# ── 3. Copy artifact ──────────────────────────────────────────────────────────
print("\n── Copying ai-fye-v6.html to artifacts/ ──")
if not SOURCE_HTML.exists():
    print(f"  ERROR: not found at {SOURCE_HTML}")
    print("  → adjust SOURCE_HTML at top of script")
    sys.exit(1)
shutil.copy2(SOURCE_HTML, ARTIFACT_DEST)
print(f"  ok: {ARTIFACT_DEST}")

# ── 4. Update artifacts/index.html ───────────────────────────────────────────
print("\n── Updating artifacts/index.html ──")
idx_path = ARTIFACTS / "index.html"
content  = idx_path.read_text(encoding="utf-8")

# Remove old link
old = re.compile(r'\s*<li>.*?ai-fye-faculty-invitation\.html.*?</li>', re.DOTALL | re.I)
if old.search(content):
    content = old.sub('', content)
    print("  removed: ai-fye-faculty-invitation entry")
else:
    print("  note: ai-fye-faculty-invitation entry not found — check manually")

# Add new entry at top of first list
new_entry = (
    f'\n    <li><strong>2026-03-08</strong> — '
    f'<a href="ai-fye-v6.html">AI-FYE: AI in the First Year Experience (v6)</a> '
    f'[<a href="{PREV_URL}">previous version</a>]</li>'
)
m = re.search(r'(<ul[^>]*>|<ol[^>]*>)', content, re.I)
if m:
    pos = m.end()
    content = content[:pos] + new_entry + content[pos:]
    print("  added: ai-fye-v6 entry")
else:
    print("  WARNING: no <ul>/<ol> found — add entry manually")

idx_path.write_text(content, encoding="utf-8")
print(f"  written: {idx_path}")

print("\n── Done ──")
print("Review, then:  git add -A && git commit -m 'Add ai-fye-v6 and new transcripts' && git push\n")
