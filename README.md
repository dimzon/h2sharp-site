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

## Docs pipeline

```sh
python tools/crawl-h2docs.py   # polite crawl of h2database.com/html → raw/
python tools/build-site.py      # raw/ → sql/ in own design
```

See `raw/provenance.json` after crawling. License: H2 content © H2 Group, MPL-2.0 / EPL-1.0.
