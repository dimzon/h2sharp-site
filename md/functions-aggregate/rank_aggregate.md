# RANK aggregate

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#rank_aggregate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
RANK([`value`](../grammar/value.md) [,...])
[`withinGroupSpecification`](../grammar/within_group_specification.md)
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Returns the rank of the hypothetical row in specified collection of rows. The rank of a row is the number of rows that precede this row plus 1. If two or more rows have the same values in `ORDER BY` columns, these rows get the same rank from the first row with the same values. It means that gaps in ranks are possible.

See [RANK](../functions-window/rank.md) for a window function with the same name.

## Example

```sql
SELECT RANK(5) WITHIN GROUP (ORDER BY V) FROM TEST;
```
