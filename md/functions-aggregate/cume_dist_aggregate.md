# CUME_DIST aggregate

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#cume_dist_aggregate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CUME_DIST([`value`](../grammar/value.md) [,...])
[`withinGroupSpecification`](../grammar/within_group_specification.md)
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Returns the relative rank of the hypothetical row in specified collection of rows. The relative rank is calculated as `NP` / `NR` where `NP` is a number of rows that precede the current row or have the same values in `ORDER BY` columns and `NR` is a total number of rows in the collection including hypothetical row.

See [CUME_DIST](../functions-window/cume_dist.md) for a window function with the same name.

## Example

```sql
SELECT CUME_DIST(5) WITHIN GROUP (ORDER BY V) FROM TEST;
```
