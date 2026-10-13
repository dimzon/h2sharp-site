# SUM

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#sum) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SUM( [ DISTINCT|ALL ] { [`numeric`](../grammar/numeric.md) | [`interval`](../grammar/interval.md) | { [`boolean`](../grammar/boolean.md) } } )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

The sum of all values. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

The data type of result is `BIGINT` for `BOOLEAN, TINYINT, SMALLINT`, and `INTEGER` arguments; `NUMERIC` with additional 10 decimal digits of precision for `BIGINT` and `NUMERIC` arguments; `DOUBLE PRECISION` for `REAL` arguments, `DECFLOAT` with additional 10 decimal digits of precision for `DOUBLE PRECISION` and `DECFLOAT` arguments; `INTERVAL` with maximum precision and the same interval qualifier and scale for `INTERVAL` arguments.

## Example

```sql
SUM(X)
```
