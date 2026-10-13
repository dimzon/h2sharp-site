# Array value constructor by query

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#array_value_constructor_by_query) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY ([`query`](query.md))
```

Collects values from the subquery into array.

The subquery should have exactly one column. Number of elements in the returned array is the number of rows in the subquery. `NULL` values are included into array.

## Example

```sql
ARRAY(SELECT * FROM SYSTEM_RANGE(1, 10));
```
