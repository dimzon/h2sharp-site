# ALTER SCHEMA RENAME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_schema_rename) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER SCHEMA [ IF EXISTS ] [`schemaName`](../grammar/name.md) RENAME TO [`newSchemaName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Renames a schema. Schema admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
ALTER SCHEMA TEST RENAME TO PRODUCTION
```
