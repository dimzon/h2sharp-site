# SET TRACE_LEVEL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_trace_level) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET { TRACE_LEVEL_FILE | TRACE_LEVEL_SYSTEM_OUT } [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the trace level for file the file or system out stream. Levels are: 0=off, 1=error, 2=info, 3=debug. The default level is 1 for file and 0 for system out. To use `SLF4J`, append `;TRACE_LEVEL_FILE=4` to the database URL when opening the database.

This setting is not persistent. Admin rights are required to execute this command, as it affects all connections. This command does not commit a transaction, and rollback does not affect it. This setting can be appended to the database URL: `jdbc:h2:./test;TRACE_LEVEL_SYSTEM_OUT=3`

## Example

```sql
SET TRACE_LEVEL_SYSTEM_OUT 3
```
