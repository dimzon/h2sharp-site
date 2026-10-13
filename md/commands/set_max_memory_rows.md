# SET MAX_MEMORY_ROWS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_max_memory_rows) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET MAX_MEMORY_ROWS [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

The maximum number of rows in a result set that are kept in-memory. If more rows are read, then the rows are buffered to disk. The default is 40000 per GB of available `RAM`.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. It has no effect for in-memory databases.

## Example

```sql
SET MAX_MEMORY_ROWS 1000
```
