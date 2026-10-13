# ROW_NUMBER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#row_number) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ROW_NUMBER() OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

Returns the number of the current row starting with 1. Window frame clause is not allowed for this function.

Window functions in H2 may require a lot of memory for large queries.

## Example

```sql
SELECT ROW_NUMBER() OVER (), * FROM TEST;
SELECT ROW_NUMBER() OVER (ORDER BY ID), * FROM TEST;
SELECT ROW_NUMBER() OVER (PARTITION BY CATEGORY ORDER BY ID), * FROM TEST;
```
