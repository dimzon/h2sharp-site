# ARRAY_GET

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#array_get) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY_GET([`arrayExpression`](../grammar/expression.md), [`indexExpression`](../grammar/expression.md))
```

🔴 compatibility-only syntax

Returns element at the specified 1-based index from an array.

This function is deprecated, use [array element reference](../grammar/array_element_reference.md) instead of it.

Returns `NULL` if array or index is `NULL`.

## Example

```sql
CALL ARRAY_GET(ARRAY['Hello', 'World'], 2)
```
