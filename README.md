# H2Sharp Site

Documentation site for [H2Sharp](https://github.com/dimzon/h2sharp) — H2 Database ported to .NET.

- Landing: `index.html` (own design, dark developer aesthetic).
- SQL reference: `sql/` — mirror of H2 docs pinned to `reference/H2_COMMIT.txt` in `dimzon/h2sharp`
  (H2 `2.5.252` + pin `27c5170`, 2026-10-06). Original: https://www.h2database.com/html/main.html
- Future .NET API sections: `dotnet/` (`planned` stubs until the port stabilizes).
- All internal links are relative — moving from `dimzon.github.io/h2sharp-site` to
  `h2sharp.github.io` or a custom domain is a one-line change in `site.json`.

## Local preview

```sh
python -m http.server 8000
# open http://localhost:8000/
```

## Tools

```sh
python tools/check-updates.py    # what landed in the engine and the two provider repos
python tools/crawl-h2docs.py     # one-time crawl of h2database.com/html → raw/ (frozen afterwards)
python tools/build-site.py       # raw/ → sql/ref/ pages in our own design
python tools/html_to_md.py       # raw/ → md/ Markdown reference (one file per topic)
python tools/verify-snapshot.py  # our snapshot vs the manifest the main repo commits
```

The tools parse the snapshot into a tree (`tools/htmldom.py`) rather than scraping it with
regular expressions. lxml is used when it imports; otherwise the standard library's
`html.parser` is used, and the two produce the same output on this corpus. Force one with
`H2SHARP_DOM_BACKEND=stdlib|lxml`.

Note: lxml 6.1.3 shipped a wheel that does not import on Python 3.13 (its `parsertarget` uses
`inspect.getargspec`, removed in 3.11). `pip install --upgrade --force-reinstall lxml` fixes it;
without it the standard library backend takes over.

See `raw/provenance.json` after crawling. License: H2 content © H2 Group, MPL-2.0 / EPL-1.0.
