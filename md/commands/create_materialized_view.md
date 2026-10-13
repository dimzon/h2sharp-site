# CREATE MATERIALIZED VIEW

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_materialized_view) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE [ OR REPLACE ]
MATERIALIZED VIEW [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`viewName`](../grammar/name.md)
[ ( [`columnName`](../grammar/name.md) [,...] ) ] AS [`query`](../grammar/query.md)
```

🟢 includes non-standard H2 syntax

Creates a new materialized view. Schema owner rights are required to execute this command.

If the `OR REPLACE` clause is used an existing view will be replaced.

Views are not updatable except using `REFRESH MATERIALIZED VIEW`.

This command commits an open transaction in this connection.

## Example

```sql
CREATE MATERIALIZED VIEW TEST_VIEW AS SELECT * FROM TEST WHERE ID < 100
```
