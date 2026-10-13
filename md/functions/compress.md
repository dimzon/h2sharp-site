# COMPRESS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#compress) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
COMPRESS([`dataBytes`](../grammar/bytes.md) [, [`algorithmString`](../grammar/string.md)])
```

🟢 includes non-standard H2 syntax

Compresses the data using the specified compression algorithm. Supported algorithms are: `LZF` (faster but lower compression; default), and `DEFLATE` (higher compression). Compression does not always reduce size. Very small objects and objects with little redundancy may get larger. This method returns bytes.

## Example

```sql
COMPRESS(STRINGTOUTF8('Test'))
```
