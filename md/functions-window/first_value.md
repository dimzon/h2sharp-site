# FIRST_VALUE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#first_value) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
FIRST_VALUE([`value`](../grammar/value.md)) [{RESPECT|IGNORE} NULLS]
OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Returns the first value in a window. If `IGNORE NULLS` is specified null values are skipped and the function returns first non-null value, if any.

Window functions in H2 may require a lot of memory for large queries.

## Example

```sql
SELECT FIRST_VALUE(X) OVER (ORDER BY ID), * FROM TEST;
SELECT FIRST_VALUE(X) IGNORE NULLS OVER (PARTITION BY CATEGORY ORDER BY ID), * FROM TEST;
```
