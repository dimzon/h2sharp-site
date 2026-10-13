# DROP TABLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_table) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP TABLE [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) [,...]
[ RESTRICT | CASCADE ]
```

🟢 includes non-standard H2 syntax

Drops an existing table, or a list of tables. The command will fail if dependent objects exist and the `RESTRICT` clause is used (the default). All dependent views and constraints are dropped as well if the `CASCADE` clause is used. This command commits an open transaction in this connection.

## Example

```sql
DROP TABLE TEST
```
