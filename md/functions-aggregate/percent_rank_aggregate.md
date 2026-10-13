# PERCENT_RANK aggregate

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#percent_rank_aggregate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
PERCENT_RANK([`value`](../grammar/value.md) [,...])
[`withinGroupSpecification`](../grammar/within_group_specification.md)
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Returns the relative rank of the hypothetical row in specified collection of rows. The relative rank is calculated as (`RANK` - 1) / (`NR` - 1), where `RANK` is a rank of the row and `NR` is a total number of rows in the collection including hypothetical row.

See [PERCENT_RANK](../functions-window/percent_rank.md) for a window function with the same name.

## Example

```sql
SELECT PERCENT_RANK(5) WITHIN GROUP (ORDER BY V) FROM TEST;
```
