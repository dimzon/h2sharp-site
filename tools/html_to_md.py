#!/usr/bin/env python3
"""Frozen H2 HTML snapshot -> per-topic Markdown reference in md/.

The snapshot is parsed into a tree (tools/htmldom.py) and walked, rather than
scraped with regular expressions: the upstream pages are markup, and "which
elements carry this class", "what is the text of this cell" and "does this
cell span two columns" are questions about a tree.

Output:
  md/<page>/<id>.md   - one file per topic (command / function / type / rule / table)
  md/<page>.md        - index of a page (groups + topics)
  md/README.md        - root index with provenance
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from htmldom import Node, parse_file  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"

MIRRORED = ["commands", "functions", "functions-aggregate", "functions-window",
            "datatypes", "grammar", "systemtables", "cheatSheet"]
PAGE_TITLE = {
    "commands": "Commands", "functions": "Functions",
    "functions-aggregate": "Aggregate Functions", "functions-window": "Window Functions",
    "datatypes": "Data Types", "grammar": "SQL Grammar", "systemtables": "System Tables",
    "cheatSheet": "Cheat Sheet",
}

id2loc: dict[str, tuple[str, str]] = {}  # anchor -> (page, file-stem)


# --------------------------------------------------------------------------
# tree helpers
# --------------------------------------------------------------------------
def content_root(page: str) -> Node:
    """The element holding the page's content."""
    doc = parse_file(RAW / "upstream" / CURRENT_STAMP / f"{page}.html")
    node = doc.find("div", cls="content")
    if node is not None:
        return node
    body = doc.find("body")
    if body is None:
        raise ValueError(f"{page}: no content div and no body")
    return body


def children_of(node: Node) -> list[Node]:
    return [c for c in node.children if c.tag not in ("script", "style")]


def is_heading(node: Node) -> bool:
    return node.tag in ("h1", "h2", "h3", "h4")


def heading_id(node: Node) -> str:
    return node.attrs.get("id", "")


def is_railroad(node: Node) -> bool:
    return node.tag == "div" and node.attrs.get("name") == "railroad"


def is_bnf(node: Node) -> bool:
    return node.tag == "pre" and node.attrs.get("name") == "bnf"


# --------------------------------------------------------------------------
# inline rendering
# --------------------------------------------------------------------------
def link_url(href: str, cur_page: str) -> str | None:
    """The markdown URL for an href, or None when the link should stay as text."""
    if not href:
        return None
    if href.startswith(("http://", "https://", "mailto:")):
        prefix = "https://www.h2database.com/html/"
        if href.startswith(prefix):
            href = href[len(prefix):]
        else:
            return href
    m = re.match(r"(?:([a-z0-9-]+)\.html)?(?:#([A-Za-z0-9_]+))?$", href)
    if not m:
        return None
    page, anchor = m.group(1), m.group(2)
    if page is None and anchor is None:
        return None
    if page is not None and page not in MIRRORED:
        return f"https://www.h2database.com/html/{href}"
    page = page or cur_page
    if anchor and anchor in id2loc:
        pg, stem = id2loc[anchor]
        return f"{stem}.md" if pg == cur_page else f"../{pg}/{stem}.md"
    if anchor:
        return f"#{anchor}"
    return f"../{page}.md"


def is_local(url: str | None) -> bool:
    return bool(url) and not url.startswith("http")


def link_target(href: str, cur_page: str, text: str) -> str:
    url = link_url(href, cur_page)
    return f"[{text}]({url})" if url else text


def render_inline(node: Node, cur_page: str, flags: set[str] | None = None) -> str:
    """Render a node's content as markdown text."""
    out: list[str] = []
    for child in node.children:
        _render(child, cur_page, out, flags)
    return "".join(out)


def _render(node: Node, cur_page: str, out: list[str], flags: set[str] | None) -> None:
    if node.tag == "#text":
        out.append(node.text or "")
        return
    tag = node.tag
    if tag in ("script", "style"):
        return
    if tag == "br":
        out.append("\n")
        return
    if tag == "code":
        out.append(f"`{node.text_content().strip()}`")
        return
    if tag == "a":
        href = node.attrs.get("href", "")
        text = node.text_content().strip()
        # upstream's generator wrapped a markdown link back into HTML: the
        # label stayed as literal text "[label](", and the closing paren ended
        # up inside both the href and the anchor text. Rebuild the link.
        if text and text == href and href.endswith(")"):
            url = link_url(href[:-1], cur_page)
            if url and out:
                # the label sits in the text right before the anchor: "[label]("
                m = re.search(r"\[([^\[\]]*)\]\($", out[-1])
                if m:
                    label = m.group(1)
                    out[-1] = out[-1][:m.start()]
                    out.append(f"[{label}]({url})" if is_local(url) else f"[{label}]({href[:-1]})")
                    return
        out.append(link_target(href, cur_page, text))
        return
    if tag in ("strong", "b"):
        inner = render_inline(node, cur_page, flags).strip()
        out.append(f"**{inner}**")
        return
    if tag in ("em", "i"):
        inner = render_inline(node, cur_page, flags).strip()
        out.append(f"*{inner}*")
        return
    if tag == "span":
        classes = node.classes
        if flags is not None:
            if "ruleH2" in classes:
                flags.add("h2")
            if "ruleCompat" in classes:
                flags.add("compat")
        out.append(render_inline(node, cur_page, flags))
        return
    if tag == "div" and "ruleH2" in node.classes and flags is not None:
        flags.add("h2")
    if tag == "div" and "ruleCompat" in node.classes and flags is not None:
        flags.add("compat")
    out.append(render_inline(node, cur_page, flags))


def clean_text(text: str) -> str:
    lines = [re.sub(r"[ \t]+", " ", ln).rstrip() for ln in text.split("\n")]
    return "\n".join(lines).strip()


# --------------------------------------------------------------------------
# block rendering
# --------------------------------------------------------------------------
def bnf_block(node: Node, cur_page: str) -> tuple[str, set[str]]:
    """The syntax block, with grammar names linked to their own topics."""
    flags: set[str] = set()
    out: list[str] = []
    _bnf_render(node, cur_page, out, flags)
    return clean_text("".join(out)), flags


def _bnf_render(node: Node, cur_page: str, out: list[str], flags: set[str]) -> None:
    for child in node.children:
        if child.tag == "#text":
            out.append(child.text or "")
        elif child.tag == "a":
            name = child.text_content().strip()
            url = link_url(child.attrs.get("href", ""), cur_page)
            out.append(f"[`{name}`]({url})" if is_local(url) else f"`{name}`")
        elif child.tag == "span":
            classes = child.classes
            if "ruleH2" in classes:
                flags.add("h2")
            if "ruleCompat" in classes:
                flags.add("compat")
            _bnf_render(child, cur_page, out, flags)
        else:
            _bnf_render(child, cur_page, out, flags)


def is_name_type_pairs(rows: list[list[tuple[str, int]]]) -> bool:
    """True for the system-tables shape: a (name, type) row, then a description
    row spanning both columns - the rows come in pairs, not one after another."""
    if not rows or len(rows) % 2:
        return False
    i = 0
    while i < len(rows):
        if len(rows[i]) != 2:
            return False
        if len(rows[i + 1]) != 1 or rows[i + 1][0][1] < 2:
            return False
        i += 2
    return True


def table_block(node: Node, cur_page: str) -> str:
    """A table as markdown.

    The system-tables pages use two rows per column: the name and the type,
    then a spanning description. That shape is read from the colspan attribute
    instead of being guessed from the row lengths.
    """
    rows: list[list[tuple[str, int]]] = []
    for tr in node.find_all("tr"):
        cells: list[Node] = [c for c in tr.children if c.tag in ("td", "th")]
        if not cells:
            continue
        row: list[tuple[str, int]] = []
        for c in cells:
            span = int(c.attrs.get("colspan", "1") or 1)
            row.append((clean_text(render_inline(c, cur_page)).replace("\n", " "), span))
        rows.append(row)
    if not rows:
        return ""
    if is_name_type_pairs(rows):
        # (name, type) followed by a description spanning both columns
        merged: list[list[str]] = []
        i = 0
        while i < len(rows):
            merged.append([rows[i][0][0], rows[i][1][0], rows[i + 1][0][0]])
            i += 2
        out = ["| Column | Type | Description |", "| --- | --- | --- |"]
        out += [f"| {r[0]} | {r[1]} | {r[2]} |" for r in merged]
        return "\n".join(out)
    width = max(sum(span for _, span in r) for r in rows)
    flat: list[list[str]] = []
    for r in rows:
        padded: list[str] = []
        for text, span in r:
            padded.append(text)
            padded.extend([""] * (span - 1))
        flat.append(padded)
    out = [f"| {' | '.join(flat[0])} |", f"| {' | '.join(['---'] * width)} |"]
    out += [f"| {' | '.join(r)} |" for r in flat[1:]]
    return "\n".join(out)


def topic_blocks(nodes: list[Node], cur_page: str) -> list[tuple[str, str, set[str]]]:
    """Blocks of a topic as (kind, payload, flags)."""
    blocks: list[tuple[str, str, set[str]]] = []
    for node in nodes:
        if is_railroad(node):
            continue
        if is_bnf(node):
            text, flags = bnf_block(node, cur_page)
            if text:
                blocks.append(("bnf", text, flags))
            continue
        if node.tag == "table":
            md = table_block(node, cur_page)
            if md:
                blocks.append(("table", md, set()))
            continue
        if node.tag == "p":
            text = clean_text(render_inline(node, cur_page))
            if text:
                blocks.append(("para", text, set()))
            continue
        text = clean_text(render_inline(node, cur_page))
        if text:
            blocks.append(("para", text, set()))
    return blocks


# --------------------------------------------------------------------------
# topic splitting
# --------------------------------------------------------------------------
def topics_of(page: str, root: Node) -> list[dict]:
    """Split the content into topics, one per heading that carries an id."""
    kids = children_of(root)
    topics: list[dict] = []
    group = ""
    for i, node in enumerate(kids):
        if not is_heading(node):
            continue
        anchor = heading_id(node)
        title = clean_text(node.text_content())
        if not anchor or anchor.endswith("_index"):
            if title and "Index" not in title:
                group = title
            continue
        body: list[Node] = []
        for nxt in kids[i + 1:]:
            if is_heading(nxt):
                break
            body.append(nxt)
        topics.append({"id": anchor, "title": title, "group": group, "body": body})
    return topics


def topic_md(page: str, topic: dict, stamp: str, pin7: str) -> str:
    out = [f"# {topic['title']}", "",
           f"> H2 `{stamp}` + H2Sharp pin `{pin7}` · "
           f"[Original](https://www.h2database.com/html/{page}.html#{topic['id']}) · "
           "© H2 Group (MPL-2.0 / EPL-1.0)", ""]
    blocks = topic_blocks(topic["body"], page)
    expect_example = False
    for kind, payload, flags in blocks:
        if kind == "bnf":
            out += ["## Syntax", "", "```bnf", payload, "```", ""]
            notes = []
            if "h2" in flags:
                notes.append("🟢 includes non-standard H2 syntax")
            if "compat" in flags:
                notes.append("🔴 compatibility-only syntax")
            if notes:
                out += [" ".join(notes), ""]
            continue
        if kind == "table":
            out += [payload, ""]
            continue
        if payload.lower().rstrip(":") == "example":
            out += ["## Example", ""]
            expect_example = True
            continue
        if expect_example:
            out += ["```sql"] + payload.split("\n") + ["```", ""]
            expect_example = False
            continue
        out += [payload, ""]
    return keep_list_together("\n".join(out)).rstrip() + "\n"


def keep_list_together(text: str) -> str:
    """Keep '1.'/'2.' items adjacent - a blank line between them restarts the list."""
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        out.append(lines[i])
        if (re.match(r"^\d+\.\s", lines[i]) and i + 2 < len(lines)
                and lines[i + 1] == "" and re.match(r"^\d+\.\s", lines[i + 2])):
            i += 1
            continue
        i += 1
    return "\n".join(out)


# --------------------------------------------------------------------------
def main() -> int:
    prov_path = RAW / "provenance.json"
    if not prov_path.exists():
        print("no raw/provenance.json — run tools/crawl-h2docs.py first")
        return 1
    global CURRENT_STAMP
    prov = json.loads(prov_path.read_text(encoding="utf-8"))
    CURRENT_STAMP = prov["stamp"]
    pin7 = prov["h2sharpPin"][:7]
    stamp = "2.5.252"

    roots = {page: content_root(page) for page in MIRRORED}
    for page, root in roots.items():
        for topic in topics_of(page, root):
            id2loc.setdefault(topic["id"], (page, topic["id"]))

    if OUT.exists():
        for path in sorted(OUT.rglob("*")):
            if path.is_file():
                path.unlink()
    for page, root in roots.items():
        folder = OUT / page
        folder.mkdir(parents=True, exist_ok=True)
        topics = topics_of(page, root)
        for topic in topics:
            (folder / f"{topic['id']}.md").write_text(
                topic_md(page, topic, stamp, pin7), encoding="utf-8")
        index = [f"# {PAGE_TITLE[page]}", "",
                 f"> H2 `{stamp}` mirror + pin `{pin7}` · "
                 f"[Original](https://www.h2database.com/html/{page}.html) · © H2 Group", ""]
        current = None
        for topic in topics:
            if topic["group"] != current:
                current = topic["group"]
                if current:
                    index += [f"## {current}", ""]
            index.append(f"- [{topic['title']}]({page}/{topic['id']}.md)")
        index.append("")
        (OUT / f"{page}.md").write_text("\n".join(index), encoding="utf-8")
        print(f"{page}: {len(topics)} topics")

    root_index = ["# H2Sharp · SQL reference (Markdown)",
                  "",
                  f"> H2 `{stamp} (2026-09-23)` snapshot + H2Sharp pin `{pin7} (2026-10-06)` · "
                  "Source: `raw/upstream/` (one-time download, `raw/provenance.json`) · "
                  "Content © H2 Group, MPL-2.0 / EPL-1.0.", "",
                  "One file per topic: syntax (BNF), description, example.",
                  ""]
    for page in MIRRORED:
        count = len(list((OUT / page).glob("*.md")))
        root_index.append(f"- [{PAGE_TITLE[page]}]({page}.md) — {count} topics")
    root_index.append("")
    (OUT / "README.md").write_text("\n".join(root_index), encoding="utf-8")
    print("md/README.md done")
    return 0


OUT = ROOT / "md"
CURRENT_STAMP = ""

if __name__ == "__main__":
    sys.exit(main())
