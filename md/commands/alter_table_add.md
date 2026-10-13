# ALTER TABLE ADD

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_table_add) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER TABLE [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) ADD [ COLUMN ]
{ [ IF NOT EXISTS ] [`columnName`](../grammar/name.md) [`columnDefinition`](../grammar/column_definition.md) [ USING [`initialValueExpression`](../grammar/expression.md) ]
| { ( { [`columnName`](../grammar/name.md) [`columnDefinition`](../grammar/column_definition.md) | [`tableConstraintDefinition`](../grammar/table_constraint_definition.md) } [,...] ) } }
[ { { BEFORE | AFTER } [`columnName`](../grammar/name.md) } | FIRST ]
```

🟢 includes non-standard H2 syntax

Adds a new column to a table. This command commits an open transaction in this connection.

If `USING` is specified the provided expression is used to generate initial value of the new column for each row. The expression may reference existing columns of the table. Otherwise the `DEFAULT` expression is used, if any. If neither `USING` nor `DEFAULT` are specified, the `NULL` is used.

## Example

```sql
ALTER TABLE TEST ADD CREATEDATE TIMESTAMP
```
