# RPAD

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#rpad) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
RPAD([`string`](../grammar/string.md), [`int`](../grammar/int.md)[, [`paddingString`](../grammar/string.md)])
```

Right pad the string to the specified length. If the length is shorter than the string, it will be truncated. If the padding string is not set, spaces will be used.

## Example

```sql
RPAD(TEXT, 10, '-')
```
