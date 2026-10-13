# CUME_DIST

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#cume_dist) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CUME_DIST() OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Returns the relative rank of the current row. The relative rank is calculated as `NP` / `NR` where `NP` is a number of rows that precede the current row or have the same values in `ORDER BY` columns and `NR` is a number of rows in window partition with this row. Note that result is always 1 if window order clause is not specified. Window frame clause is not allowed for this function.

Window functions in H2 may require a lot of memory for large queries.

See [CUME_DIST aggregate](../functions-aggregate/cume_dist_aggregate.md) for a hypothetical set function with the same name.

## Example

```sql
SELECT CUME_DIST() OVER (ORDER BY ID), * FROM TEST;
SELECT CUME_DIST() OVER (PARTITION BY CATEGORY ORDER BY ID), * FROM TEST;
```
