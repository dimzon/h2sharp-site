# RAWTOHEX

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#rawtohex) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
RAWTOHEX({[`string`](../grammar/string.md)|[`bytes`](../grammar/bytes.md)})
```

🟢 includes non-standard H2 syntax

Converts a string or bytes to the hex representation. 4 hex characters per string character are used. This method returns a string.

## Example

```sql
RAWTOHEX(DATA)
```
