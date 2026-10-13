# DROP SCHEMA

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_schema) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP SCHEMA [ IF EXISTS ] [`schemaName`](../grammar/name.md) [ RESTRICT | CASCADE ]
```

🟢 includes non-standard H2 syntax

Drops a schema. Schema owner rights are required to execute this command. The command will fail if objects in this schema exist and the `RESTRICT` clause is used (the default). All objects in this schema are dropped as well if the `CASCADE` clause is used. This command commits an open transaction in this connection.

## Example

```sql
DROP SCHEMA TEST_SCHEMA
```
