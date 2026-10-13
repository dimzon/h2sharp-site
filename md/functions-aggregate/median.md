# MEDIAN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#median) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
MEDIAN( [ DISTINCT|ALL ] [`value`](../grammar/value.md) )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

The value separating the higher half of a values from the lower half. Returns the middle value or an interpolated value between two middle values if number of values is even. Interpolation is only supported for numeric, date-time, and interval data types. `NULL` values are ignored in the calculation. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

## Example

```sql
MEDIAN(X)
```
