# DROP ALIAS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_alias) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP ALIAS [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`aliasName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Drops an existing function alias. Schema owner rights are required to execute this command.

This command commits an open transaction in this connection.

## Example

```sql
DROP ALIAS MY_SQRT
```
