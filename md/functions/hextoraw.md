# HEXTORAW

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#hextoraw) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
HEXTORAW([`string`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Converts a hex representation of a string to a string. 4 hex characters per string character are used.

## Example

```sql
HEXTORAW(DATA)
```
