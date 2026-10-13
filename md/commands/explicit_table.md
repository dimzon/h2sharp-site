# Explicit table

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#explicit_table) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TABLE [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md)
[ ORDER BY [`selectOrder`](../grammar/select_order.md) [,...] ]
[ OFFSET [`expression`](../grammar/expression.md) { ROW | ROWS } ]
[ FETCH { FIRST | NEXT } [ [`expression`](../grammar/expression.md) [ PERCENT ] ] { ROW | ROWS }
{ ONLY | WITH TIES } ]
```

Selects data from a table.

This command is an equivalent to `SELECT` * `FROM` tableName. See [SELECT](select.md) command for description of `ORDER BY, OFFSET`, and `FETCH`.

## Example

```sql
TABLE TEST;
TABLE TEST ORDER BY ID FETCH FIRST ROW ONLY;
```
