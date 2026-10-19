#!/usr/bin/env python3
"""Frozen H2 HTML snapshot -> per-topic Markdown reference in md/.

Reads raw/upstream/<stamp>/ (one-time crawl, see raw/README.md) and writes:
  md/<page>/<id>.md   — one file per topic (command / function / type / rule / table)
  md/<page>.md        — index of a page (groups + topics)
  md/README.md        — root index with provenance

Topic = heading (h2/h3) carrying an id. Hidden <pre name="bnf"> becomes the
Syntax block, <div name="railroad"> is skipped, <p>Example:</p> + following
notranslate paragraph becomes a ```sql fence, <table class="main"> becomes a
Markdown table. Stdlib only. Idempotent.
"""
import html as ihtml
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "md"

MIRRORED = ["commands", "functions", "functions-aggregate", "functions-window",
            "datatypes", "grammar", "systemtables", "cheatSheet"]
PAGE_TITLE = {
    "commands": "Commands", "functions": "Functions",
    "functions-aggregate": "Aggregate Functions", "functions-window": "Window Functions",
    "datatypes": "Data Types", "grammar": "SQL Grammar", "systemtables": "System Tables",
    "cheatSheet": "Cheat Sheet",
}
BOILERPLATE = ("Click on the header", "Non-standard syntax is marked")

id2loc: dict[str, tuple[str, str]] = {}  # anchor -> (page, file-stem)


def slug_page(page: str) -> str:
    return page


class BlockParser(HTMLParser):
    """Collect ordered blocks from topic HTML: bnf / para / example / table."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.blocks: list[tuple[str, str]] = []
        self._buf: list[str] = []
        self._mode: str | None = None
        self._skip = 0  # railroad subtree depth

    def _flush(self) -> None:
        if self._mode and self._buf:
            self.blocks.append((self._mode, "".join(self._buf)))
        self._mode, self._buf = None, []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if self._skip:
            self._skip += 1
            return
        if tag == "div" and a.get("name") == "railroad":
            self._flush()
            self._skip = 1
            return
        if tag == "pre" and a.get("name") == "bnf":
            self._flush()
            self._mode, self._buf = "bnf", []
            return
        if self._mode == "bnf":
            self._buf.append(self.get_starttag_text() or f"<{tag}>")
            return
        if tag == "p" and self._mode is None:
            self._mode, self._buf = "para", []
            return
        if tag == "table" and self._mode is None:
            self._mode, self._buf = "table", []
            self._buf.append(self.get_starttag_text() or "<table>")
            return
        if self._mode in ("para", "table"):
            self._buf.append(self.get_starttag_text() or f"<{tag}>")

    def handle_endtag(self, tag: str) -> None:
        if self._skip:
            self._skip -= 1
            return
        if self._mode == "bnf":
            if tag == "pre":
                self._flush()
            else:
                self._buf.append(f"</{tag}>")
            return
        if self._mode == "para" and tag == "p":
            self._flush()
            return
        if self._mode == "table" and tag == "table":
            self._buf.append("</table>")
            # table may nest? upstream main tables don't nest; flush on outer close
            if self._buf.count("<table") <= self._buf.count("</table>"):
                self._flush()
            return
        if self._mode in ("para", "table"):
            self._buf.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self._skip:
            return
        if self._mode in ("para", "bnf", "table"):
            self._buf.append(data)

    def handle_entityref(self, name: str) -> None:
        self.handle_data(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self.handle_data(f"&#{name};")

    def handle_comment(self, data: str) -> None:
        return


def inline_md(s: str, cur_page: str) -> str:
    """Convert inline HTML to Markdown: links, code, breaks."""
    # upstream artifact: a markdown link whose href absorbed the closing paren,
    # then got re-wrapped as HTML: [text](<a href="URL)">URL</a>. Rewrite it back
    # into a plain anchor so link() below resolves it to a local .md file.
    s = re.sub(r"\[([^\]]+)\]\(<a\s+href=\"([^\"]+?)\)\"[^>]*>[^<]*</a>",
               lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    def link(m: "re.Match[str]") -> str:
        href, text = m.group(1), ihtml.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        # absolute upstream URLs to mirrored pages behave like local ones
        if href.startswith("https://www.h2database.com/html/"):
            href = href[len("https://www.h2database.com/html/"):]
        mm = re.match(r"(?:([a-z0-9-]+)\.html)?(?:#([A-Za-z0-9_]+))?$", href)
        if mm and (mm.group(1) in MIRRORED or (mm.group(1) is None and mm.group(2))):
            page = mm.group(1) or cur_page
            anchor = mm.group(2)
            if anchor and anchor in id2loc:
                pg, stem = id2loc[anchor]
                rel = f"{stem}.md" if pg == cur_page else f"../{pg}/{stem}.md"
                return f"[{text}]({rel})"
            if anchor:
                return f"[{text}](#{anchor})"
            return f"[{text}](../{page}.md)"
        if href.startswith(("http://", "https://", "mailto:")):
            return f"[{text}]({href})"
        return text  # drop unresolvable relative links, keep text

    s = re.sub(r"<a\s+href=\"([^\"]+)\"[^>]*>(.*?)</a>", link, s, flags=re.S)
    s = re.sub(r"<code[^>]*>(.*?)</code>", lambda m: f"`{ihtml.unescape(m.group(1)).strip()}`", s, flags=re.S)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = ihtml.unescape(s)
    lines = [ln.rstrip() for ln in s.split("\n")]
    return "\n".join(lines).strip()


def bnf_md(s: str, cur_page: str) -> tuple[str, set[str]]:
    """BNF pre -> text with linked `names`; report ruleH2/ruleCompat flags."""
    flags: set[str] = set()
    if "ruleH2" in s:
        flags.add("h2")
    if "ruleCompat" in s:
        flags.add("compat")

    def span(m: "re.Match[str]") -> str:
        return m.group(1)  # keep inner, drop span wrapper (flags already recorded)

    s = re.sub(r"<span[^>]*>(.*?)</span>", span, s, flags=re.S)

    def ref(m: "re.Match[str]") -> str:
        name = ihtml.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        mm = re.match(r"(?:([a-z0-9-]+)\.html)?(?:#([A-Za-z0-9_]+))?$", m.group(1))
        if mm and (mm.group(1) in MIRRORED or (mm.group(1) is None and mm.group(2))):
            page = mm.group(1) or cur_page
            anchor = mm.group(2)
            if anchor and anchor in id2loc:
                pg, stem = id2loc[anchor]
                rel = f"{stem}.md" if pg == cur_page else f"../{pg}/{stem}.md"
                return f"[`{name}`]({rel})"
        return f"`{name}`"

    s = re.sub(r"<a\s+href=\"([^\"]+)\"[^>]*>(.*?)</a>", ref, s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = ihtml.unescape(s)
    lines = [ln.rstrip() for ln in s.strip("\n").split("\n")]
    return "\n".join(lines).strip("\n"), flags


def table_md(s: str, cur_page: str) -> str:
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", s, flags=re.S)
    grid: list[list[str]] = []
    for r in rows:
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, flags=re.S)
        grid.append([re.sub(r"\s+", " ", inline_md(c, cur_page).replace("\n", " ")).strip() for c in cells])
    if not grid:
        return ""
    # systemtables pattern: (name,type) + (colspan desc) pairs -> 3-col table
    if all(len(r) in (1, 2) for r in grid):
        merged: list[list[str]] = []
        i = 0
        while i < len(grid):
            if len(grid[i]) == 2 and i + 1 < len(grid) and len(grid[i + 1]) == 1:
                merged.append([grid[i][0], grid[i][1], grid[i + 1][0]])
                i += 2
            else:
                row = (grid[i] + ["", ""])[:3]
                merged.append(row)
                i += 1
        out = ["| Column | Type | Description |", "| --- | --- | --- |"]
        out += [f"| {r[0]} | {r[1]} | {r[2]} |" for r in merged]
        return "\n".join(out)
    width = max(len(r) for r in grid)
    grid = [(r + [""] * width)[:width] for r in grid]
    head = grid[0]
    out = [f"| {' | '.join(head)} |", f"| {' | '.join(['---'] * width)} |"]
    out += [f"| {' | '.join(r)} |" for r in grid[1:]]
    return "\n".join(out)


def topics_of(page: str, body: str) -> list[dict]:
    """Split content HTML into topics at headings carrying ids."""
    heads = list(re.finditer(r"<h([23])((?:[^>]*\sid=\"([^\"]+)\"[^>]*)?)>(.*?)</h\1>", body, flags=re.S))
    topics = []
    group = ""
    for idx, m in enumerate(heads):
        level, anchor = int(m.group(1)), m.group(3)
        title = ihtml.unescape(re.sub(r"<[^>]+>", "", m.group(4))).strip()
        start = m.end()
        end = heads[idx + 1].start() if idx + 1 < len(heads) else len(body)
        if not anchor or anchor.endswith("_index"):
            if level in (2, 3) and title and "Index" not in title:
                group = title
            continue
        topics.append({"id": anchor, "level": level, "title": title,
                       "group": group, "html": body[start:end]})
    return topics


def topic_md(page: str, t: dict, stamp: str, pin7: str) -> str:
    parser = BlockParser()
    parser.feed(t["html"])
    out = [f"# {t['title']}", "",
           f"> H2 `{stamp}` + H2Sharp pin `{pin7}` · "
           f"[Original](https://www.h2database.com/html/{page}.html#{t['id']}) · "
           "© H2 Group (MPL-2.0 / EPL-1.0)", ""]
    expect_example = False
    for kind, raw in parser.blocks:
        if kind == "bnf":
            text, flags = bnf_md(raw, page)
            if not text:
                continue
            out += ["## Syntax", "", "```bnf", text, "```", ""]
            if flags:
                notes = []
                if "h2" in flags:
                    notes.append("🟢 includes non-standard H2 syntax")
                if "compat" in flags:
                    notes.append("🔴 compatibility-only syntax")
                out += [" ".join(notes), ""]
        elif kind == "para":
            text = inline_md(raw, page)
            if not text:
                continue
            if any(b in text for b in BOILERPLATE):
                continue
            if text.strip().lower().rstrip(":") == "example":
                out += ["## Example", ""]
                expect_example = True
                continue
            if expect_example:
                out += ["```sql"] + text.split("\n") + ["```", ""]
                expect_example = False
                continue
            # multi-statement notranslate paragraph that isn't labeled -> code fence too
            out += [text, ""]
        elif kind == "table":
            md = table_md(raw, page)
            if md:
                out += [md, ""]
    # keep ordered lists contiguous (blank line between "1."/"2." restarts numbering)
    joined: list[str] = []
    i = 0
    while i < len(out):
        joined.append(out[i])
        if (re.match(r"^\d+\.\s", out[i]) and i + 2 < len(out)
                and out[i + 1] == "" and re.match(r"^\d+\.\s", out[i + 2])):
            i += 1  # skip the blank line, keep list together
            continue
        i += 1
    return "\n".join(joined).rstrip() + "\n"


def main() -> None:
    prov = json.loads((RAW / "provenance.json").read_text(encoding="utf-8"))
    snap = RAW / "upstream" / prov["stamp"]
    pin7 = prov["h2sharpPin"][:7]
    stamp = "2.5.252"

    # pass 1: anchor map
    bodies: dict[str, str] = {}
    for page in MIRRORED:
        raw = (snap / f"{page}.html").read_text(encoding="utf-8", errors="replace")
        start = raw.find('<div class="content">')
        start = raw.find(">", start) + 1
        end = raw.rfind("<!-- } -->")
        bodies[page] = raw[start:end]
    for page, body in bodies.items():
        for t in topics_of(page, body):
            id2loc.setdefault(t["id"], (page, t["id"]))

    # pass 2: write topics + indexes
    if OUT.exists():
        for p in sorted(OUT.rglob("*")):
            if p.is_file():
                p.unlink()
    for page, body in bodies.items():
        topics = topics_of(page, body)
        d = OUT / page
        d.mkdir(parents=True, exist_ok=True)
        for t in topics:
            (d / f"{t['id']}.md").write_text(topic_md(page, t, stamp, pin7), encoding="utf-8")
        # page index grouped
        idx = [f"# {PAGE_TITLE[page]}", "",
               f"> H2 `{stamp}` mirror + pin `{pin7}` · "
               f"[Original](https://www.h2database.com/html/{page}.html) · © H2 Group", ""]
        cur = None
        for t in topics:
            if t["group"] != cur:
                cur = t["group"]
                if cur:
                    idx += [f"## {cur}", ""]
            idx.append(f"- [{t['title']}]({page}/{t['id']}.md)")
        idx.append("")
        (OUT / f"{page}.md").write_text("\n".join(idx), encoding="utf-8")
        print(f"{page}: {len(topics)} topics")

    root = ["# H2Sharp · SQL reference (Markdown)",
            "",
            f"> H2 `{stamp} (2026-09-23)` snapshot + H2Sharp pin `{pin7} (2026-10-06)` · "
            "Source: `raw/upstream/` (one-time download, `raw/provenance.json`) · "
            "Content © H2 Group, MPL-2.0 / EPL-1.0.", "",
            "One file per topic: syntax (BNF), description, example.",
            ""]
    for page in MIRRORED:
        n = len(list((OUT / page).glob("*.md")))
        root.append(f"- [{PAGE_TITLE[page]}]({page}.md) — {n} topics")
    root.append("")
    (OUT / "README.md").write_text("\n".join(root), encoding="utf-8")
    print("md/README.md done")


if __name__ == "__main__":
    main()
