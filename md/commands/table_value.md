# Table value

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#table_value) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
VALUES [`rowValueExpression`](../grammar/row_value_expression.md) [,...]
[ ORDER BY [`selectOrder`](../grammar/select_order.md) [,...] ]
[ OFFSET [`expression`](../grammar/expression.md) { ROW | ROWS } ]
[ FETCH { FIRST | NEXT } [ [`expression`](../grammar/expression.md) [ PERCENT ] ] { ROW | ROWS }
{ ONLY | WITH TIES } ]
```

A list of rows that can be used like a table. See See [SELECT](select.md) command for description of `ORDER BY, OFFSET`, and `FETCH`. The column list of the resulting table is C1, C2, and so on.

## Example

```sql
VALUES (1, 'Hello'), (2, 'World');
```
