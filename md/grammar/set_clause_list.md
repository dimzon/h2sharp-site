# Set clause list

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#set_clause_list) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ { [`updateTarget`](update_target.md) = { DEFAULT | [`expression`](expression.md) } }
| { ( [`updateTarget`](update_target.md) [,...] ) = { [`rowValueExpression`](row_value_expression.md) | ([`query`](query.md)) } } } [,...]
```

List of `SET` clauses.

Each column may be specified only once in update targets.

## Example

```sql
NAME = 'Test', PRICE = 2
(A, B) = (1, 2)
(A, B) = (1, 2), C = 3
(A, B) = (SELECT X, Y FROM OTHER T2 WHERE T1.ID = T2.ID)
```
