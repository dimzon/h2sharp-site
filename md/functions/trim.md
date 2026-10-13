# TRIM

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#trim) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TRIM ( [ [ LEADING | TRAILING | BOTH ] [ [`characterToTrimString`](../grammar/string.md) ] FROM ] [`string`](../grammar/string.md) )
```

Removes all leading spaces, trailing spaces, or spaces at both ends from a string. If character to trim is specified, these characters are removed instead of spaces, only one character can be specified. To trim multiple different characters use [LTRIM](ltrim.md), [RTRIM](rtrim.md), or [BTRIM](btrim.md).

If neither `LEADING, TRAILING`, nor `BOTH` are specified, `BOTH` is implicit.

## Example

```sql
TRIM(NAME)
TRIM(LEADING FROM NAME)
TRIM(BOTH '_' FROM NAME)
```
