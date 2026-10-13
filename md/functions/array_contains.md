# ARRAY_CONTAINS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#array_contains) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY_CONTAINS([`arrayExpression`](../grammar/expression.md), [`value`](../grammar/value.md))
```

🟢 includes non-standard H2 syntax

Returns a boolean `TRUE` if the array contains the value or `FALSE` if it does not contain it. Returns `NULL` if the specified array is `NULL`.

## Example

```sql
CALL ARRAY_CONTAINS(ARRAY['Hello', 'World'], 'Hello')
```
