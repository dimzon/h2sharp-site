# EXPAND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#expand) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
EXPAND([`bytes`](../grammar/bytes.md))
```

🟢 includes non-standard H2 syntax

Expands data that was compressed using the `COMPRESS` function. This method returns bytes.

## Example

```sql
UTF8TOSTRING(EXPAND(COMPRESS(STRINGTOUTF8('Test'))))
```
