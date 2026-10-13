# ARRAY_APPEND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#array_append) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY_APPEND([`arrayExpression`](../grammar/expression.md), [`value`](../grammar/value.md))
```

🔴 compatibility-only syntax

Append an element to the end of an array.

This function is deprecated, use `||` instead of it.

Returns `NULL` if any parameter is `NULL`.

## Example

```sql
CALL ARRAY_APPEND(ARRAY[1, 2], 3)
```
