# RANK

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#rank) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
RANK() OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Returns the rank of the current row. The rank of a row is the number of rows that precede this row plus 1. If two or more rows have the same values in `ORDER BY` columns, these rows get the same rank from the first row with the same values. It means that gaps in ranks are possible. This function requires window order clause. Window frame clause is not allowed for this function.

Window functions in H2 may require a lot of memory for large queries.

See [RANK aggregate](../functions-aggregate/rank_aggregate.md) for a hypothetical set function with the same name.

## Example

```sql
SELECT RANK() OVER (ORDER BY ID), * FROM TEST;
SELECT RANK() OVER (PARTITION BY CATEGORY ORDER BY ID), * FROM TEST;
```
