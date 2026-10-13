# DENSE_RANK aggregate

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#dense_rank_aggregate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DENSE_RANK([`value`](../grammar/value.md) [,...])
[`withinGroupSpecification`](../grammar/within_group_specification.md)
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Returns the dense rank of the hypothetical row in specified collection of rows. The rank of a row is the number of groups of rows with the same values in `ORDER BY` columns that precede group with this row plus 1. If two or more rows have the same values in `ORDER BY` columns, these rows get the same rank. Gaps in ranks are not possible.

See [DENSE_RANK](../functions-window/dense_rank.md) for a window function with the same name.

## Example

```sql
SELECT DENSE_RANK(5) WITHIN GROUP (ORDER BY V) FROM TEST;
```
