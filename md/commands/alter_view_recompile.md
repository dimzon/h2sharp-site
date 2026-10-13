# ALTER VIEW RECOMPILE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_view_recompile) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER VIEW [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`viewName`](../grammar/name.md) RECOMPILE
```

🟢 includes non-standard H2 syntax

Recompiles a view after the underlying tables have been changed or created. Schema owner rights are required to execute this command. This command is used for views created using `CREATE FORCE VIEW`. This command commits an open transaction in this connection.

## Example

```sql
ALTER VIEW ADDRESS_VIEW RECOMPILE
```
