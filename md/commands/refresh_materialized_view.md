# REFRESH MATERIALIZED VIEW

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#refresh_materialized_view) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REFRESH MATERIALIZED VIEW [[`schemaName`](../grammar/name.md).][`viewName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Recreates an existing materialized view. Schema owner rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
REFRESH MATERIALIZED VIEW TEST_VIEW
```
