# REPEAT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#repeat) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REPEAT([`string`](../grammar/string.md), [`int`](../grammar/int.md))
```

🟢 includes non-standard H2 syntax

Returns a string repeated some number of times.

## Example

```sql
REPEAT(NAME || ' ', 10)
```
