# GCD_AGG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#gcd_agg) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
GCD_AGG([`numeric`](../grammar/numeric.md))
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Returns the greatest common divisor of all values. Arguments must have `TINYINT, SMALLINT, INTEGER, BIGINT`, or `NUMERIC` data type with scale 0. This function returns result of `NUMERIC` data type with scale 0. `NULL` values are ignored in the calculation. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

For non-aggregate function see [GCD](../functions/gcd.md).

## Example

```sql
GCD_AGG(V)
```
