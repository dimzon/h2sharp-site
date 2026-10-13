# PERCENT_RANK

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#percent_rank) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
PERCENT_RANK() OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Returns the relative rank of the current row. The relative rank is calculated as (`RANK` - 1) / (`NR` - 1), where `RANK` is a rank of the row and `NR` is a number of rows in window partition with this row. Note that result is always 0 if window order clause is not specified. Window frame clause is not allowed for this function.

Window functions in H2 may require a lot of memory for large queries.

See [PERCENT_RANK aggregate](../functions-aggregate/percent_rank_aggregate.md) for a hypothetical set function with the same name.

## Example

```sql
SELECT PERCENT_RANK() OVER (ORDER BY ID), * FROM TEST;
SELECT PERCENT_RANK() OVER (PARTITION BY CATEGORY ORDER BY ID), * FROM TEST;
```
