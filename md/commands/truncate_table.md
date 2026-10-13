# TRUNCATE TABLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#truncate_table) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TRUNCATE TABLE [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) [ [ CONTINUE | RESTART ] IDENTITY ]
```

Removes all rows from a table. Unlike `DELETE FROM` without where clause, this command can not be rolled back. This command is faster than `DELETE` without where clause. Only regular data tables without foreign key constraints can be truncated (except if referential integrity is disabled for this database or for this table). Linked tables can't be truncated. If `RESTART IDENTITY` is specified next values for identity columns are restarted.

This command commits an open transaction in this connection.

## Example

```sql
TRUNCATE TABLE TEST
```
