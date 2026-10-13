# ARRAY_CAT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#array_cat) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY_CAT([`arrayExpression`](../grammar/expression.md), [`arrayExpression`](../grammar/expression.md))
```

🔴 compatibility-only syntax

Returns the concatenation of two arrays.

This function is deprecated, use `||` instead of it.

Returns `NULL` if any parameter is `NULL`.

## Example

```sql
CALL ARRAY_CAT(ARRAY[1, 2], ARRAY[3, 4])
```
