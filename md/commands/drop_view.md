# DROP VIEW

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_view) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP VIEW [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`viewName`](../grammar/name.md) [ RESTRICT | CASCADE ]
```

🟢 includes non-standard H2 syntax

Drops an existing view. Schema owner rights are required to execute this command. All dependent views are dropped as well if the `CASCADE` clause is used (the default). The command will fail if dependent views exist and the `RESTRICT` clause is used. This command commits an open transaction in this connection.

## Example

```sql
DROP VIEW TEST_VIEW
```
