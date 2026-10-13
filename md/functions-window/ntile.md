# NTILE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#ntile) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
NTILE([`long`](../grammar/long.md)) OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Distributes the rows into a specified number of groups. Number of groups should be a positive long value. `NTILE` returns the 1-based number of the group to which the current row belongs. First groups will have more rows if number of rows is not divisible by number of groups. For example, if 5 rows are distributed into 2 groups this function returns 1 for the first 3 row and 2 for the last 2 rows. This function requires window order clause. Window frame clause is not allowed for this function.

Window functions in H2 may require a lot of memory for large queries.

## Example

```sql
SELECT NTILE(10) OVER (ORDER BY ID), * FROM TEST;
SELECT NTILE(5) OVER (PARTITION BY CATEGORY ORDER BY ID), * FROM TEST;
```
