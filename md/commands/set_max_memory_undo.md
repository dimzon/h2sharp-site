# SET MAX_MEMORY_UNDO

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_max_memory_undo) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET MAX_MEMORY_UNDO [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

The maximum number of undo records per a session that are kept in-memory. If a transaction is larger, the records are buffered to disk. The default value is 50000. Changes to tables without a primary key can not be buffered to disk. This setting is not supported when using multi-version concurrency.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. It has no effect for in-memory databases.

## Example

```sql
SET MAX_MEMORY_UNDO 1000
```
