# GEOMETRY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#geometry) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
GEOMETRY { [`bytes`](bytes.md) | [`string`](string.md) }
```

🟢 includes non-standard H2 syntax

A binary string or character string with `GEOMETRY` object.

A binary string should contain Well-known Binary Representation (`WKB`) from `OGC` 06-103r4. Dimension system marks may be specified either in both `OGC WKB` or in Post`GIS EWKB` formats. Optional `SRID` from `EWKB` may be specified. `POINT EMPTY` stored with NaN values as specified in `OGC` 12-128r15 is supported.

A character string should contain Well-known Text Representation (`WKT`) from `OGC` 06-103r4 with optional `SRID` from Post`GIS EWKT` extension.

## Example

```sql
GEOMETRY 'GEOMETRYCOLLECTION (POINT (1 2))'
GEOMETRY X'00000000013ff00000000000003ff0000000000000'
```
