# ALTER TABLE RENAME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_table_rename) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER TABLE [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) RENAME TO [`newName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Renames a table. This command commits an open transaction in this connection.

## Example

```sql
ALTER TABLE TEST RENAME TO MY_DATA
```
