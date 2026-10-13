# PERCENTILE_DISC

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#percentile_disc) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
PERCENTILE_DISC([`numeric`](../grammar/numeric.md)) WITHIN GROUP (ORDER BY [`sortSpecification`](../grammar/sort_specification.md))
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

Return percentile of values from the group. Interpolation is not performed. Argument must be between 0 and 1 inclusive. Argument must be the same for all rows in the same group. If argument is `NULL`, the result is `NULL`. `NULL` values are ignored in the calculation. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

## Example

```sql
PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY V)
```
