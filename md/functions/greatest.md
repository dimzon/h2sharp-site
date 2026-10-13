# GREATEST

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#greatest) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
GREATEST([`aValue`](../grammar/value.md), [`bValue`](../grammar/value.md) [,...]) [{RESPECT|IGNORE} NULLS]
```

🟢 includes non-standard H2 syntax

Returns the largest value or `NULL` if any value is `NULL` or the largest value cannot be determined. For example, `ROW` (`NULL`, 1) is neither equal to nor smaller than nor larger than `ROW` (1, 1). If `IGNORE NULLS` is specified, `NULL` values are ignored.

## Example

```sql
CALL GREATEST(1, 2, 3);
```
