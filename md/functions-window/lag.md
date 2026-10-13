# LAG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#lag) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LAG([`value`](../grammar/value.md) [, [`offsetInt`](../grammar/int.md) [, [`defaultValue`](../grammar/value.md)]]) [{RESPECT|IGNORE} NULLS]
OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Returns the value in a previous row with specified offset relative to the current row. Offset must be non-negative. If `IGNORE NULLS` is specified rows with null values in selected expression are skipped. If number of considered rows is less than specified relative number this function returns `NULL` or the specified default value, if any. If offset is 0 the value from the current row is returned unconditionally. This function requires window order clause. Window frame clause is not allowed for this function.

Window functions in H2 may require a lot of memory for large queries.

## Example

```sql
SELECT LAG(X) OVER (ORDER BY ID), * FROM TEST;
SELECT LAG(X, 2, 0) IGNORE NULLS OVER (
    PARTITION BY CATEGORY ORDER BY ID
), * FROM TEST;
```
