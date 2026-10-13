# TO_CHAR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#to_char) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TO_CHAR([`value`](../grammar/value.md) [, [`formatString`](../grammar/string.md)[, [`nlsParamString`](../grammar/string.md)]])
```

🔴 compatibility-only syntax

Oracle-compatible `TO_CHAR` function that can format a timestamp, a number, or text.

## Example

```sql
CALL TO_CHAR(TIMESTAMP '2010-01-01 00:00:00', 'DD MON, YYYY')
```
