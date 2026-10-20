#!/usr/bin/env python3
"""A minimal DOM over the standard library's html.parser.

Why this exists instead of regexes: the upstream H2 pages are markup, and
questions like "what is the text of this cell" or "which elements carry this
class" are questions about a tree, not about a string. A third-party DOM was
not an option here - lxml 6.1.3 fails to import on Python 3.13 (its
parsertarget uses inspect.getargspec, removed in 3.11) - so the tree is built
here on html.parser, which is in the standard library.

The parser is deliberately forgiving, like a browser: it applies the implicit
end tags HTML allows (a <p> ends the previous <p>, a <td> ends the previous
<td>), and it keeps unknown tags as containers rather than dropping them.
"""
from __future__ import annotations

from html.parser import HTMLParser
from typing import Iterator, Optional

# Elements that never have content and never get a closing tag.
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

# A start tag closes an open element of the same kind when the tag is one of
# these and the open element is in the implied-end set.
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


class Node:
    """One element or text node."""

    __slots__ = ("tag", "attrs", "children", "parent", "text")

    def __init__(self, tag: str, attrs: Optional[dict[str, str]] = None,
                 text: Optional[str] = None, parent: Optional["Node"] = None):
        self.tag = tag
        self.attrs: dict[str, str] = attrs or {}
        self.children: list["Node"] = []
        self.parent = parent
        self.text = text

    # -- navigation -------------------------------------------------------
    def iter(self) -> Iterator["Node"]:
        """Depth-first over this node and its descendants."""
        yield self
        for child in self.children:
            yield from child.iter()

    def find_all(self, tag: Optional[str] = None, cls: Optional[str] = None) -> list["Node"]:
        out = []
        for node in self.iter():
            if node.tag in (None, "#text"):
                continue
            if tag is not None and node.tag != tag:
                continue
            if cls is not None and cls not in node.attrs.get("class", "").split():
                continue
            out.append(node)
        return out

    def find(self, tag: Optional[str] = None, cls: Optional[str] = None) -> Optional["Node"]:
        found = self.find_all(tag, cls)
        return found[0] if found else None

    # -- content ----------------------------------------------------------
    @property
    def classes(self) -> list[str]:
        return self.attrs.get("class", "").split()

    def text_content(self) -> str:
        """All text under this node, in document order."""
        if self.tag == "#text":
            return self.text or ""
        return "".join(c.text_content() for c in self.children)

    def own_text(self) -> str:
        """Text directly inside this node, before any child element."""
        parts: list[str] = []
        for child in self.children:
            if child.tag == "#text":
                parts.append(child.text or "")
            else:
                break
        return "".join(parts)

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        if self.tag == "#text":
            return f"Text({self.text!r})"
        return f"<{self.tag} {self.attrs}>"


class DomBuilder(HTMLParser):
    """Builds a Node tree, applying HTML's implied end tags."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("#document")
        self._stack: list[Node] = [self.root]

    # -- helpers ----------------------------------------------------------
    def _current(self) -> Node:
        return self._stack[-1]

    def _close_implied(self, tag: str) -> None:
        implied = IMPLIED_END.get(tag)
        if not implied:
            return
        while len(self._stack) > 1:
            top = self._stack[-1]
            if top.tag in implied:
                self._stack.pop()
            else:
                break

    def _close_tag(self, tag: str) -> None:
        for i in range(len(self._stack) - 1, 0, -1):
            if self._stack[i].tag == tag:
                del self._stack[i:]
                return
        # No matching open element: ignore the stray close tag, as a browser does.

    # -- HTMLParser hooks -------------------------------------------------
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self._close_implied(tag)
        node = Node(tag, {k.lower(): (v or "") for k, v in attrs}, parent=self._current())
        self._current().children.append(node)
        if tag not in VOID:
            self._stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self._close_implied(tag)
        node = Node(tag, {k.lower(): (v or "") for k, v in attrs}, parent=self._current())
        self._current().children.append(node)

    def handle_endtag(self, tag: str) -> None:
        self._close_tag(tag.lower())

    def handle_data(self, data: str) -> None:
        if not data:
            return
        node = Node("#text", text=data, parent=self._current())
        self._current().children.append(node)

    def handle_comment(self, data: str) -> None:
        # Comments carry no content for our purposes; the upstream marks its
        # generated blocks with them and we look at the elements instead.
        return

    def handle_entityref(self, name: str) -> None:  # pragma: no cover - convert_charrefs=True
        self.handle_data(f"&{name};")

    def handle_charref(self, name: str) -> None:  # pragma: no cover - convert_charrefs=True
        self.handle_data(f"&#{name};")


def parse(text: str) -> Node:
    """Parse HTML text into a Node tree."""
    builder = DomBuilder()
    builder.feed(text)
    builder.close()
    return builder.root


def parse_file(path) -> Node:
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return parse(fh.read())


# -- serialisation -------------------------------------------------------
def escape_text(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def escape_attr(text: str) -> str:
    return escape_text(text).replace('"', "&quot;")


def serialize(node: Node) -> str:
    """Serialise a node's children back to HTML (entities kept as text)."""
    out: list[str] = []
    for child in node.children:
        _ser(child, out)
    return "".join(out)


def _ser(node: Node, out: list[str]) -> None:
    if node.tag == "#text":
        out.append(escape_text(node.text or ""))
        return
    attrs = "".join(f' {k}="{escape_attr(v)}"' for k, v in node.attrs.items())
    out.append(f"<{node.tag}{attrs}>")
    if node.tag in VOID:
        return
    for child in node.children:
        _ser(child, out)
    out.append(f"</{node.tag}>")
