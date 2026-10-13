# SET QUERY_STATISTICS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_query_statistics) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET QUERY_STATISTICS { TRUE | FALSE }
```

🟢 includes non-standard H2 syntax

Disabled or enables query statistics gathering for the whole database. The statistics are reflected in the `INFORMATION_SCHEMA.QUERY_STATISTICS` meta-table.

This setting is not persistent. This command commits an open transaction in this connection. Admin rights are required to execute this command, as it affects all connections.

## Example

```sql
SET QUERY_STATISTICS FALSE
```
