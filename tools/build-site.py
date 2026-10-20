#!/usr/bin/env python3
"""Transform the frozen raw/upstream snapshot -> sql/ref/ pages in our own design.

The upstream pages are parsed into a tree (tools/htmldom.py) and the content
element is taken from it, rather than cutting the file at a comment marker:
cutting left the layout table's closing tags behind and unbalanced the markup.

What the tree lets us do that a string could not:
  - pick the content element by class, and take exactly its children;
  - rewrite every link by looking at the href attribute, not at a pattern;
  - drop the upstream's scripts and event handlers as elements.

The upstream content classes (railroad, ruleH2, ruleCompat, ...) are kept and
styled by assets/h2ref.css. Cross-page links (grammar.html#x) already point at
sibling files in sql/ref/ and are left as they are.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from htmldom import Node, parse_file, serialize  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"

MIRRORED = ["commands", "functions", "functions-aggregate", "functions-window",
            "datatypes", "grammar", "systemtables", "cheatSheet"]

TITLES = {
    "commands": "Commands",
    "functions": "Functions",
    "functions-aggregate": "Aggregate Functions",
    "functions-window": "Window Functions",
    "datatypes": "Data Types",
    "grammar": "SQL Grammar",
    "systemtables": "System Tables",
    "cheatSheet": "Cheat Sheet",
}

BANNER = """<div class="version-banner">H2 <code>2.5.252 (2026-09-23)</code> mirror + H2Sharp pin <code>{pin}</code> · Original: <a href="https://www.h2database.com/html/{name}.html">h2database.com ↗</a> · © H2 Group, MPL-2.0 / EPL-1.0 · Snapshot frozen: {stamp}</div>"""

LAYOUT = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} — H2Sharp SQL mirror</title><link rel="icon" type="image/svg+xml" href="../../assets/favicon.svg"><link rel="stylesheet" href="../../assets/site.css"><link rel="stylesheet" href="../../assets/h2ref.css"></head><body>
<header class="site-header"><div class="wrap"><a class="brand" href="../../" style="text-decoration:none"><img src="../../assets/logo.svg" alt="">H2Sharp <small>in progress</small></a><nav class="main"><a href="../../">Home</a><a href="../" class="active">SQL</a><a href="../../dotnet/">.NET API</a><a href="../../status/">Status</a></nav></div></header>
<main class="wrap wide"><section class="block">{banner}<article class="doc h2doc">{body}</article></section></main>
<footer><div class="wrap"><span>SQL content © H2 Group · <a href="https://www.h2database.com/html/license.html">original license</a></span><span style="margin-left:auto"><a href="../">← SQL section</a></span></div></footer><script src="../../assets/ref.js"></script></body></html>"""


def content_node(doc: Node) -> Node:
    """The element holding the page's content."""
    node = doc.find("div", cls="content")
    if node is not None:
        return node
    body = doc.find("body")
    if body is None:
        raise ValueError("no content div and no body")
    return body


def strip(node: Node) -> None:
    """Remove scripts and styles, and neutralise event handlers we do not implement.

    onclick is kept: assets/ref.js binds switchBnf(this) to it, and that is
    the toggle between the railroad diagram and the BNF text. The upstream's
    onload/onscroll handlers call functions this site does not have, so those
    are renamed rather than left to fire.
    """
    for child in list(node.children):
        if child.tag in ("script", "style", "#comment"):
            node.remove_child(child)
            continue
        for attr in [a for a in child.attrs if a.startswith("on") and a != "onclick"]:
            child.attrs[f"data-{attr}"] = child.attrs.pop(attr)
        strip(child)


def rewrite_links(node: Node) -> None:
    """Point links at the local mirror, or at the original for pages we do not carry."""
    for anchor in node.find_all("a"):
        href = anchor.attrs.get("href", "")
        if not href:
            continue
        if href.startswith("https://www.h2database.com/html/"):
            href = href[len("https://www.h2database.com/html/"):]
        page, _, anchor_part = href.partition("#")
        if page.endswith(".html"):
            name = page[:-5]
            if name in MIRRORED:
                anchor.attrs["href"] = f"{name}.html" + (f"#{anchor_part}" if anchor_part else "")
            else:
                anchor.attrs["href"] = f"https://www.h2database.com/html/{href}"
        elif not page and anchor_part:
            anchor.attrs["href"] = f"#{anchor_part}"


def build_body(path: Path) -> str:
    doc = parse_file(path)
    content = content_node(doc)
    strip(content)
    rewrite_links(content)
    return serialize(content).strip()


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
        body = build_body(src)
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
