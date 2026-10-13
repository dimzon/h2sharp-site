# AVG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#avg) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
AVG ( [ DISTINCT|ALL ] { [`numeric`](../grammar/numeric.md) | [`interval`](../grammar/interval.md) } )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

The average (mean) value. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

The data type of result is `DOUBLE PRECISION` for `TINYINT, SMALLINT, INTEGER`, and `REAL` arguments, `NUMERIC` with additional 10 decimal digits of precision and scale for `BIGINT` and `NUMERIC` arguments; `DECFLOAT` with additional 10 decimal digits of precision for `DOUBLE PRECISION` and `DECFLOAT` arguments; `INTERVAL` with the same leading field precision, all additional smaller datetime units in interval qualifier, and the maximum scale for `INTERVAL` arguments.

## Example

```sql
AVG(X)
```
