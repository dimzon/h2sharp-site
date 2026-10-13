# ENVELOPE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#envelope) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ENVELOPE( [`value`](../grammar/value.md) )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Returns the minimum bounding box that encloses all specified `GEOMETRY` values. Only 2D coordinate plane is supported. `NULL` values are ignored in the calculation. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

## Example

```sql
ENVELOPE(X)
```
