# ARRAY_SLICE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#array_slice) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY_SLICE([`arrayExpression`](../grammar/expression.md), [`lowerBoundInt`](../grammar/int.md), [`upperBoundInt`](../grammar/int.md))
```

🟢 includes non-standard H2 syntax

Returns elements from the array as specified by the lower and upper bound parameters. Both parameters are inclusive and the first element has index 1, i.e. `ARRAY_SLICE`(a, 2, 2) has only the second element. Returns `NULL` if any parameter is `NULL` or if an index is out of bounds.

## Example

```sql
CALL ARRAY_SLICE(ARRAY[1, 2, 3, 4], 1, 3)
```
