# Select order

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#select_order) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ [`expression`](expression.md) | { [`int`](int.md) } } [ ASC | DESC ] [ NULLS { FIRST | LAST } ]
```

🔴 compatibility-only syntax

Sorts the result by the given column number, or by an expression. If the expression is a single parameter, then the value is interpreted as a column number. Negative column numbers reverse the sort order.

## Example

```sql
NAME DESC NULLS LAST
```
