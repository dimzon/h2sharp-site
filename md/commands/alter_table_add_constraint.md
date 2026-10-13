# ALTER TABLE ADD CONSTRAINT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_table_add_constraint) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER TABLE [ IF EXISTS ] [`tableName`](../grammar/name.md) ADD [`tableConstraintDefinition`](../grammar/table_constraint_definition.md) [ CHECK | NOCHECK ]
```

🟢 includes non-standard H2 syntax

Adds a constraint to a table. If `NOCHECK` is specified, existing rows are not checked for consistency (the default is to check consistency for existing rows). The required indexes are automatically created if they don't exist yet. It is not possible to disable checking for unique constraints. This command commits an open transaction in this connection.

## Example

```sql
ALTER TABLE TEST ADD CONSTRAINT NAME_UNIQUE UNIQUE(NAME)
```
