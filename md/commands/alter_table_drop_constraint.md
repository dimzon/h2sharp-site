# ALTER TABLE DROP CONSTRAINT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_table_drop_constraint) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER TABLE [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) DROP
CONSTRAINT [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`constraintName`](../grammar/name.md) [ RESTRICT | CASCADE ] | { PRIMARY KEY }
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Removes a constraint or a primary key from a table. If `CASCADE` is specified, unique or primary key constraint is dropped together with all referential constraints that reference the specified constraint. This command commits an open transaction in this connection.

## Example

```sql
ALTER TABLE TEST DROP CONSTRAINT UNIQUE_NAME RESTRICT
```
