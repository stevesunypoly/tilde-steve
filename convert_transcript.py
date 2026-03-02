#!/usr/bin/env python3
"""
convert_transcript.py
Converts a Claude/ChatGPT export .md transcript to a styled HTML page.
- Metadata displayed at top
- Prompt/response pairs reversed (newest first)
- Each pair in <details><summary> with prompt as label
- Sanitized filename (spaces -> hyphens)

Usage: python3 convert_transcript.py input.md [output_dir]
Folder Action: pass dropped file as $1
"""

import sys
import re
import os
from html import escape

try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False

def slugify(name):
    name = os.path.splitext(os.path.basename(name))[0]
    name = name.replace(' ', '-')
    name = re.sub(r'[^a-zA-Z0-9\-_]', '', name)
    return name.lower()

def parse_transcript(text):
    metadata = {}
    pairs = []

    # Extract metadata
    for match in re.finditer(r'\*\*(Created|Updated|Exported|Link):\*\*\s*(.+?)(?:\n|$)', text):
        key, val = match.group(1), match.group(2).strip()
        link_match = re.match(r'\[.*?\]\((.*?)\)', val)
        if link_match:
            val = link_match.group(1)
        metadata[key] = val

    # Title
    title_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    metadata['Title'] = title_match.group(1).strip() if title_match else 'Transcript'

    # Split on prompt/response headers
    blocks = re.split(r'\n## (Prompt|Response):\n', text)

    i = 1
    current_prompt = None
    while i < len(blocks) - 1:
        block_type = blocks[i]
        block_content = blocks[i+1].strip()
        # Strip leading timestamp
        block_content = re.sub(r'^\d{1,2}/\d{1,2}/\d{4},.*\n\n?', '', block_content)

        if block_type == 'Prompt':
            current_prompt = block_content
        elif block_type == 'Response' and current_prompt is not None:
            pairs.append((current_prompt, block_content))
            current_prompt = None
        i += 2

    return metadata, pairs

def md_to_html(text):
    if HAS_MARKDOWN:
        return markdown.markdown(text, extensions=['fenced_code', 'tables'])
    # Basic fallback
    paras = text.split('\n\n')
    return '\n'.join(f'<p>{escape(p.strip())}</p>' for p in paras if p.strip())

def render_html(metadata, pairs):
    title = escape(metadata.get('Title', 'Transcript'))
    created = escape(metadata.get('Created', ''))
    updated = escape(metadata.get('Updated', ''))
    link = metadata.get('Link', '')
    link_html = f'<a href="{escape(link)}">{escape(link)}</a>' if link else ''

    pairs_html = []
    for prompt, response in reversed(pairs):
        summary = prompt.split('\n')[0].strip()
        if len(summary) > 120:
            summary = summary[:117] + '...'
        pairs_html.append(f"""
    <details>
      <summary>{escape(summary)}</summary>
      <div class="response">{md_to_html(response)}</div>
    </details>""")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
  <style>
    details {{ border:1px solid #ddd; border-radius:4px; margin:.75em 0; }}
    summary {{ font-weight:bold; padding:.6em 1em; cursor:pointer; background:#f9f9f9; border-radius:4px; text-align:left; }}
    summary:hover {{ background:#f0eded; }}
    details[open] summary {{ border-bottom:1px solid #ddd; border-radius:4px 4px 0 0; }}
    .response {{ padding:1em 1.2em; line-height:1.6; }}
    .meta {{ font-size:.85em; color:#666; margin-bottom:1.5em; border-bottom:1px solid #eee; padding-bottom:.75em; }}
    .meta a {{ color:#8C1515; }}
  </style>
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
  <h1>{title}</h1>
  <div class="meta">
    <strong>Created:</strong> {created} &nbsp;|&nbsp; <strong>Updated:</strong> {updated}<br>
    {f'<strong>Source:</strong> {link_html}' if link_html else ''}
  </div>
  <p><em>Exchanges shown newest first. Click a prompt to expand the response.</em></p>
{''.join(pairs_html)}
</div>
</body>
</html>"""

def convert(input_path, output_dir=None):
    if not input_path.endswith('.md'):
        print(f"Skipping non-.md file: {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    metadata, pairs = parse_transcript(text)
    if not pairs:
        print(f"Warning: no pairs found in {input_path}")

    slug = slugify(input_path)
    out_dir = output_dir or os.path.dirname(input_path)
    out_path = os.path.join(out_dir, slug + '.html')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(render_html(metadata, pairs))

    print(f"Written: {out_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 convert_transcript.py input.md [output_dir]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
