# CARDINALITY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#cardinality) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ CARDINALITY | { ARRAY_LENGTH } } ([`arrayExpression`](../grammar/expression.md))
```

🔴 compatibility-only syntax

Returns the length of an array or `JSON` array. Returns `NULL` if the specified array is `NULL`.

## Example

```sql
CALL CARDINALITY(ARRAY['Hello', 'World'])
CALL CARDINALITY(JSON '[1, 2, 3]')
```
