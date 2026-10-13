# Script Compression Encryption

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#script_compression_encryption) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[ COMPRESSION { DEFLATE | LZF | ZIP | GZIP } ]
[ CIPHER [`cipher`](cipher.md) PASSWORD [`string`](string.md) ]
```

🟢 includes non-standard H2 syntax

The compression and encryption algorithm to use for script files. When using encryption, only `DEFLATE` and `LZF` are supported. `LZF` is faster but uses more space.

## Example

```sql
COMPRESSION LZF
```
