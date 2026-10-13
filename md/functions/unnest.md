# UNNEST

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#unnest) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
UNNEST([`arrayExpression`](../grammar/expression.md), [,...]) [WITH ORDINALITY]
```

Returns the result set. Number of columns is equal to number of arguments, plus one additional column with row number if `WITH ORDINALITY` is specified. Number of rows is equal to length of longest specified array. If multiple arguments are specified and they have different length, cells with missing values will contain null values.

## Example

```sql
SELECT * FROM UNNEST(ARRAY['a', 'b', 'c']);
SELECT * FROM UNNEST(JSON '["a", "b", "c"]');
```
