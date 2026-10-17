#!/usr/bin/env python3
"""Transform frozen raw/upstream snapshot -> sql/ref/ pages in own H2Sharp design.

Upstream format (h2database.com built pages): content lives between
`<td class="nav"><div class="content">` and the final `<!-- } -->` marker.
Left nav / search / chrome are dropped; upstream content classes
(railroad, ruleH2, ruleCompat, ...) are kept and styled by assets/h2ref.css.

Cross-page links (grammar.html#x) already point at sibling files in sql/ref/
and are left as-is. Stdlib only. Idempotent.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"

BANNER = """<div class="version-banner">H2 <code>2.5.252 (2026-09-23)</code> mirror + H2Sharp pin <code>{pin}</code> · Original: <a href="https://www.h2database.com/html/{name}.html">h2database.com ↗</a> · © H2 Group, MPL-2.0 / EPL-1.0 · Snapshot frozen: {stamp}</div>"""

LAYOUT = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} — H2Sharp SQL mirror</title><link rel="icon" type="image/svg+xml" href="../../assets/favicon.svg"><link rel="stylesheet" href="../../assets/site.css"><link rel="stylesheet" href="../../assets/h2ref.css"></head><body>
<header class="site-header"><div class="wrap"><a class="brand" href="../../" style="text-decoration:none"><img src="../../assets/logo.svg" alt="">H2Sharp <small>in progress</small></a><nav class="main"><a href="../../">Home</a><a href="../" class="active">SQL</a><a href="../../dotnet/">.NET API</a><a href="../../status/">Status</a></nav></div></header>
<main class="wrap wide"><section class="block">{banner}<article class="doc h2doc">{body}</article></section></main>
<footer><div class="wrap"><span>SQL content © H2 Group · <a href="https://www.h2database.com/html/license.html">original license</a></span><span style="margin-left:auto"><a href="../">← SQL section</a></span></div></footer><script src="../../assets/ref.js"></script></body></html>"""

TITLES = {
    "commands": "Commands",
    "functions": "Functions",
    "functions-aggregate": "Aggregate Functions",
    "functions-window": "Window Functions",
    "datatypes": "Data Types",
    "grammar": "SQL Grammar",
    "systemtables": "System Tables",
}


def extract(raw: str) -> str:
    start = raw.find('<div class="content">')
    if start < 0:
        raise ValueError("content div not found")
    start = raw.find(">", start) + 1
    end = raw.rfind("<!-- } -->")
    if end < 0 or end <= start:
        raise ValueError("end marker not found")
    return raw[start:end]


MIRRORED = ["commands", "functions", "functions-aggregate", "functions-window",
            "datatypes", "grammar", "systemtables"]


def clean(body: str) -> str:
    # Drop the generator's search-marker comments, keep syntax/railroad variants.
    body = re.sub(r"<!-- \[search\] \{ -->|<!-- \} -->", "", body)
    # Absolute upstream links to mirrored pages -> local siblings.
    body = re.sub(
        r'href="https://www\.h2database\.com/html/(' + "|".join(MIRRORED) + r')\.html((?:#[^"]*)?)"',
        r'href="\1.html\2"',
        body,
    )
    # Links to out-of-scope upstream pages (advanced, features, ...) -> absolute
    # original URLs instead of local 404s.
    body = re.sub(r'href="([a-zA-Z0-9_-]+\.html((?:#[^"]*)?))"',
                  lambda m: m.group(0) if m.group(1).split("#")[0].split(".")[0] in MIRRORED
                  else f'href="https://www.h2database.com/html/{m.group(1)}"',
                  body)
    # Normalize onload/scroll leftovers (none inside content, defensive).
    body = body.replace(' onload="', ' data-onload="').replace(' onscroll="', ' data-onscroll="')
    return body.strip()


def main() -> None:
    prov_path = RAW / "provenance.json"
    if not prov_path.exists():
        print("no raw/provenance.json — run tools/crawl-h2docs.py first")
        return
    prov = json.loads(prov_path.read_text(encoding="utf-8"))
    snap = RAW / "upstream" / prov["stamp"]
    out = ROOT / "sql" / "ref"
    out.mkdir(parents=True, exist_ok=True)
    pin = prov["h2sharpPin"][:7]
    for p in prov["pages"]:
        src = snap / f"{p['name']}.html"
        if not src.exists():
            print(f"skip {p['name']}: missing snapshot file")
            continue
        body = clean(extract(src.read_text(encoding="utf-8", errors="replace")))
        page = LAYOUT.format(
            title=TITLES.get(p["name"], p["name"]),
            banner=BANNER.format(pin=pin, name=p["name"], stamp=prov["stamp"]),
            body=body,
        )
        (out / f"{p['name']}.html").write_text(page, encoding="utf-8")
        print(f"built sql/ref/{p['name']}.html ({len(page) // 1024} KB)")
    print("done")


if __name__ == "__main__":
    main()
