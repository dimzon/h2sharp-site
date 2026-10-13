# DELETE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#delete) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DELETE FROM [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md)
[ WHERE [`expression`](../grammar/expression.md) ]
FETCH { FIRST | NEXT } [ [`expression`](../grammar/expression.md) ] { ROW | ROWS } ONLY
```

🟢 includes non-standard H2 syntax

Deletes rows form a table. If `FETCH` is specified, at most the specified number of rows are deleted (no limit if null or smaller than zero).

## Example

```sql
DELETE FROM TEST WHERE ID=2
```
