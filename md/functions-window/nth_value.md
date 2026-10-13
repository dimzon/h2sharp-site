# NTH_VALUE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#nth_value) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
NTH_VALUE([`value`](../grammar/value.md), [`nInt`](../grammar/int.md)) [FROM {FIRST|LAST}] [{RESPECT|IGNORE} NULLS]
OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Returns the value in a row with a specified relative number in a window. Relative row number must be positive. If `FROM LAST` is specified rows a counted backwards from the last row. If `IGNORE NULLS` is specified rows with null values in selected expression are skipped. If number of considered rows is less than specified relative number this function returns `NULL`. Note that the last row is actually a last row in the current group of rows if window order clause is specified and window frame clause is not specified.

Window functions in H2 may require a lot of memory for large queries.

## Example

```sql
SELECT NTH_VALUE(X) OVER (ORDER BY ID), * FROM TEST;
SELECT NTH_VALUE(X) IGNORE NULLS OVER (
    PARTITION BY CATEGORY ORDER BY ID
    RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
), * FROM TEST;
```
