# SET

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#set) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET([`@variableName`](../grammar/name.md), [`value`](../grammar/value.md))
```

🟢 includes non-standard H2 syntax

Updates a variable with the given value. The new value is returned. When used in a query, the value is updated in the order the rows are read. When used in a subquery, not all rows might be read depending on the query plan. This can be used to implement running totals / cumulative sums.

## Example

```sql
SELECT X, SET(@I, COALESCE(@I, 0)+X) RUNNING_TOTAL FROM SYSTEM_RANGE(1, 10)
```
