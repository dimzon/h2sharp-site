# RATIO_TO_REPORT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-window.html#ratio_to_report) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
RATIO_TO_REPORT([`value`](../grammar/value.md))
OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)
```

🟢 includes non-standard H2 syntax

Returns the ratio of a value to the sum of all values. If argument is `NULL` or sum of all values is 0, then the value of function is `NULL`. Window ordering and window frame clauses are not allowed for this function.

Window functions in H2 may require a lot of memory for large queries.

## Example

```sql
SELECT X, RATIO_TO_REPORT(X) OVER (PARTITION BY CATEGORY), CATEGORY FROM TEST;
```
