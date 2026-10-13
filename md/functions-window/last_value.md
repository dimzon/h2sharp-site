# LAST_VALUE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#last_value) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LAST_VALUE([`value`](../grammar/value.md)) [{RESPECT|IGNORE} NULLS]
OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Returns the last value in a window. If `IGNORE NULLS` is specified null values are skipped and the function returns last non-null value before them, if any; if there is no non-null value it returns `NULL`. Note that the last value is actually a value in the current group of rows if window order clause is specified and window frame clause is not specified.

Window functions in H2 may require a lot of memory for large queries.

## Example

```sql
SELECT LAST_VALUE(X) OVER (ORDER BY ID), * FROM TEST;
SELECT LAST_VALUE(X) IGNORE NULLS OVER (
    PARTITION BY CATEGORY ORDER BY ID
    RANGE BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
), * FROM TEST;
```
