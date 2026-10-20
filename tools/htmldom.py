#!/usr/bin/env python3
"""A small DOM over the standard library, or over lxml when it is available.

Why a tree at all: the upstream H2 pages are markup, and questions like "what
is the text of this cell" or "which elements carry this class" are questions
about a tree, not about a string.

Two backends:
  * lxml, when it imports - a real, forgiving HTML parser that also knows
    about rowspan/colspan and rebuilds the document the way a browser does;
  * the standard library's html.parser, built into a tree here, so the tooling
    works on a machine where lxml is missing or broken.

Both backends expose the same interface, so the tools do not care which one
runs. The lxml path is preferred; the fallback keeps the site buildable
anywhere, with no install step.
"""
from __future__ import annotations

import os
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterator, Optional

try:  # pragma: no cover - depends on the machine
    from lxml import etree
    from lxml import html as lxml_html

    HAVE_LXML = True
except Exception:  # noqa: BLE001 - any import failure means "no lxml"
    etree = None
    lxml_html = None
    HAVE_LXML = False

# H2SHARP_DOM_BACKEND=stdlib forces the standard library backend, which is how
# the fallback is tested on a machine where lxml happens to work.
_FORCE = os.environ.get("H2SHARP_DOM_BACKEND", "").lower()
if _FORCE == "stdlib":
    HAVE_LXML = False
elif _FORCE == "lxml" and not HAVE_LXML:
    raise SystemExit("H2SHARP_DOM_BACKEND=lxml requested, but lxml does not import here")


# ---------------------------------------------------------------------------
# shared interface
# ---------------------------------------------------------------------------
class Node:
    """One element, in whichever backend produced it."""

    __slots__ = ("_el", "_tag", "_attrs", "_children", "_text", "parent")

    def __init__(self, backend: str, el=None, tag: str = "", attrs: Optional[dict] = None,
                 text: Optional[str] = None, children: Optional[list["Node"]] = None):
        self.parent: Optional[Node] = None
        if backend == "lxml":
            self._el = el
            self._tag = tag
            self._attrs = attrs or {}
            self._children = children or []
            self._text = text
        else:
            self._el = None
            self._tag = tag
            self._attrs = attrs or {}
            self._children = children or []
            self._text = text

    # -- navigation -------------------------------------------------------
    def iter(self) -> Iterator["Node"]:
        yield self
        for child in self.children:
            yield from child.iter()

    def find_all(self, tag: Optional[str] = None, cls: Optional[str] = None) -> list["Node"]:
        out: list[Node] = []
        for node in self.iter():
            if node.tag.startswith("#"):
                continue
            if tag is not None and node.tag != tag:
                continue
            if cls is not None and cls not in node.classes:
                continue
            out.append(node)
        return out

    def find(self, tag: Optional[str] = None, cls: Optional[str] = None) -> Optional["Node"]:
        found = self.find_all(tag, cls)
        return found[0] if found else None

    # -- content ----------------------------------------------------------
    @property
    def tag(self) -> str:
        return self._tag

    @property
    def attrs(self) -> dict[str, str]:
        return self._attrs

    @property
    def children(self) -> list["Node"]:
        return self._children

    @property
    def classes(self) -> list[str]:
        return self._attrs.get("class", "").split()

    @property
    def text(self) -> str:
        return self._text or ""

    def text_content(self) -> str:
        if self._el is not None:  # lxml
            return self._el.text_content()
        if self._tag == "#text":
            return self._text or ""
        return "".join(c.text_content() for c in self._children)

    def own_text(self) -> str:
        """Text directly inside this node, before any child element."""
        if self._el is not None:  # lxml
            return self._el.text or ""
        parts: list[str] = []
        for child in self._children:
            if child.tag == "#text":
                parts.append(child.text)
            else:
                break
        return "".join(parts)

    def remove_child(self, child: "Node") -> None:
        """Detach a child from this node, in whichever backend produced it."""
        if child in self._children:
            self._children.remove(child)
        if self._el is not None and child._el is not None:
            try:
                self._el.remove(child._el)
            except ValueError:
                pass

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        if self.tag == "#text":
            return f"Text({self.text!r})"
        return f"<{self.tag} {self.attrs}>"


# ---------------------------------------------------------------------------
# lxml backend
# ---------------------------------------------------------------------------
def _lxml_children(el) -> list[Node]:
    """The children of an lxml element: its text, then each element with its tail.

    Text is kept as nodes so that the inline renderer can walk the tree in
    document order, the same way it walks the standard library tree.
    """
    out: list[Node] = []
    if el.text:
        out.append(Node("lxml", tag="#text", text=el.text))
    for child in el:
        tag = child.tag if isinstance(child.tag, str) else "#comment"
        node = Node("lxml", el=child, tag=tag, attrs={k: v for k, v in child.attrib.items()})
        node._children = _lxml_children(child)
        out.append(node)
        if child.tail:
            out.append(Node("lxml", tag="#text", text=child.tail))
    return out


def _lxml_wrap(el) -> Node:
    node = Node("lxml", el=el, tag=el.tag if isinstance(el.tag, str) else "#document",
                attrs={k: v for k, v in el.attrib.items()})
    node._children = _lxml_children(el)
    for child in node._children:
        child.parent = node
    return node


def _parse_lxml(text: str) -> Node:
    # lxml's HTML parser is forgiving: it fixes unclosed tags the way a browser
    # does, and it keeps the document structure rather than guessing.
    doc = lxml_html.document_fromstring(text)
    return _lxml_wrap(doc)


# ---------------------------------------------------------------------------
# standard library backend
# ---------------------------------------------------------------------------
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

IMPLIED_END = {
    "p": {"p"},
    "li": {"li"},
    "dt": {"dt", "dd"},
    "dd": {"dt", "dd"},
    "tr": {"tr", "td", "th"},
    "td": {"td", "th"},
    "th": {"td", "th"},
    "tbody": {"tr", "td", "th"},
    "thead": {"tr", "td", "th"},
    "tfoot": {"tr", "td", "th"},
    "option": {"option"},
}


class DomBuilder(HTMLParser):
    """Builds a Node tree, applying HTML's implied end tags."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("stdlib", tag="#document")
        self._stack: list[Node] = [self.root]

    def _current(self) -> Node:
        return self._stack[-1]

    def _close_implied(self, tag: str) -> None:
        implied = IMPLIED_END.get(tag)
        if not implied:
            return
        while len(self._stack) > 1:
            if self._stack[-1].tag in implied:
                self._stack.pop()
            else:
                break

    def _close_tag(self, tag: str) -> None:
        for i in range(len(self._stack) - 1, 0, -1):
            if self._stack[i].tag == tag:
                del self._stack[i:]
                return

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self._close_implied(tag)
        node = Node("stdlib", tag=tag, attrs={k.lower(): (v or "") for k, v in attrs})
        self._current()._children.append(node)
        node.parent = self._current()
        if tag not in VOID:
            self._stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self._close_implied(tag)
        node = Node("stdlib", tag=tag, attrs={k.lower(): (v or "") for k, v in attrs})
        self._current()._children.append(node)
        node.parent = self._current()

    def handle_endtag(self, tag: str) -> None:
        self._close_tag(tag.lower())

    def handle_data(self, data: str) -> None:
        if not data:
            return
        node = Node("stdlib", tag="#text", text=data)
        self._current()._children.append(node)
        node.parent = self._current()


def _parse_stdlib(text: str) -> Node:
    builder = DomBuilder()
    builder.feed(text)
    builder.close()
    return builder.root


# ---------------------------------------------------------------------------
# public API
# ---------------------------------------------------------------------------
def parse(text: str) -> Node:
    """Parse HTML text into a Node tree."""
    if HAVE_LXML:
        return _parse_lxml(text)
    return _parse_stdlib(text)


def parse_file(path) -> Node:
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return parse(fh.read())


def escape_text(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def escape_attr(text: str) -> str:
    return escape_text(text).replace('"', "&quot;")


def serialize(node: Node) -> str:
    """Serialise a node's children back to HTML.

    The children list is the single source of truth for both backends: a child
    removed from it is gone from the output, whether it was detached from the
    lxml tree or never added to the standard library tree.
    """
    out: list[str] = []
    for child in node.children:
        _ser(child, out)
    return "".join(out)


def _ser(node: Node, out: list[str]) -> None:
    if node.tag == "#text":
        out.append(escape_text(node.text))
        return
    if node.tag == "#comment":
        return
    if node._el is not None:  # lxml element: serialise it whole
        out.append(etree.tostring(node._el, encoding="unicode", method="html", with_tail=False))
        return
    attrs = "".join(f' {k}="{escape_attr(v)}"' for k, v in node.attrs.items())
    out.append(f"<{node.tag}{attrs}>")
    if node.tag in VOID:
        return
    for child in node.children:
        _ser(child, out)
    out.append(f"</{node.tag}>")


def backend() -> str:
    return "lxml" if HAVE_LXML else "stdlib"
