# ALTER TABLE DROP COLUMN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_table_drop_column) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER TABLE [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md)
DROP [ COLUMN ] [ IF EXISTS ]
{ ( [`columnName`](../grammar/name.md) [,...] ) } | [`columnName`](../grammar/name.md) [,...]
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Removes column(s) from a table. This command commits an open transaction in this connection.

## Example

```sql
ALTER TABLE TEST DROP COLUMN NAME
ALTER TABLE TEST DROP COLUMN (NAME1, NAME2)
```
