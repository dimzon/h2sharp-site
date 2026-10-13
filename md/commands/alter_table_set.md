# ALTER TABLE SET

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_table_set) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER TABLE [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md)
SET REFERENTIAL_INTEGRITY
{ FALSE | TRUE } [ CHECK | NOCHECK ]
```

🟢 includes non-standard H2 syntax

Disables or enables referential integrity checking for a table. This command can be used inside a transaction. Enabling referential integrity does not check existing data, except if `CHECK` is specified. Use `SET REFERENTIAL_INTEGRITY` to disable it for all tables; the global flag and the flag for each table are independent.

This command commits an open transaction in this connection.

## Example

```sql
ALTER TABLE TEST SET REFERENTIAL_INTEGRITY FALSE
```
