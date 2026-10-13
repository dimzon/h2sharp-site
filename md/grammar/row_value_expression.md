# Row value expression

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#row_value_expression) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ROW ([`expression`](expression.md), [,...])
| ( [ [`expression`](expression.md), [`expression`](expression.md) [,...] ] )
| [`expression`](expression.md)
```

A row value expression.

## Example

```sql
ROW (1)
(1, 2)
1
```
