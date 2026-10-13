# SET MAX_LOG_SIZE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_max_log_size) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET MAX_LOG_SIZE [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the maximum size of the transaction log, in megabytes. If the log is larger, and if there is no open transaction, the transaction log is truncated. If there is an open transaction, the transaction log will continue to grow however. The default max size is 16 MB. This setting has no effect for in-memory databases.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent.

## Example

```sql
SET MAX_LOG_SIZE 2
```
