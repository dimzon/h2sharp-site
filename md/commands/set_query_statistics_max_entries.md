# SET QUERY_STATISTICS_MAX_ENTRIES

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_query_statistics_max_entries) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET QUERY_STATISTICS [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Set the maximum number of entries in query statistics meta-table. Default value is 100.

This setting is not persistent. This command commits an open transaction in this connection. Admin rights are required to execute this command, as it affects all connections.

## Example

```sql
SET QUERY_STATISTICS_MAX_ENTRIES 500
```
