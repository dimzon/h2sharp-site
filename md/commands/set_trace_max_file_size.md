# SET TRACE_MAX_FILE_SIZE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_trace_max_file_size) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET TRACE_MAX_FILE_SIZE [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the maximum trace file size. If the file exceeds the limit, the file is renamed to .old and a new file is created. If another .old file exists, it is deleted. The default max size is 16 MB.

This setting is persistent. Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting can be appended to the database URL: `jdbc:h2:./test;TRACE_MAX_FILE_SIZE=3`

## Example

```sql
SET TRACE_MAX_FILE_SIZE 10
```
