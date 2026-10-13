# SET SCHEMA

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_schema) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET SCHEMA { [`schemaString`](../grammar/string.md) | { [`schemaName`](../grammar/name.md) } }
```

🟢 includes non-standard H2 syntax

Changes the default schema of the current connection. The default schema is used in statements where no schema is set explicitly. The default schema for new connections is `PUBLIC`.

This command does not commit a transaction, and rollback does not affect it. This setting can be appended to the database URL: `jdbc:h2:./test;SCHEMA=ABC`

## Example

```sql
SET SCHEMA 'PUBLIC'
SET SCHEMA INFORMATION_SCHEMA
```
