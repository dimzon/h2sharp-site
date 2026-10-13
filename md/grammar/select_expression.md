# Select Expression

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#select_expression) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`wildcardExpression`](wildcard_expression.md) | [`expression`](expression.md) [ [ AS ] [`columnAlias`](alias.md) ]
```

An expression in a `SELECT` statement.

## Example

```sql
ID AS DOCUMENT_ID
```
