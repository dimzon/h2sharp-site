# Join specification

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#join_specification) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ON [`expression`](expression.md) | USING ([`columnName`](name.md) [,...])
```

Specifies a join condition or column names.

## Example

```sql
ON B.ID = A.PARENT_ID
USING (ID)
```
