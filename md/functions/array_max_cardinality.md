# ARRAY_MAX_CARDINALITY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#array_max_cardinality) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY_MAX_CARDINALITY([`arrayExpression`](../grammar/expression.md))
```

Returns the maximum allowed array cardinality (length) of the declared data type of argument.

## Example

```sql
SELECT ARRAY_MAX_CARDINALITY(COL1) FROM TEST FETCH FIRST ROW ONLY;
```
