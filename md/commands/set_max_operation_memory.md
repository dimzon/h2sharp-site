# SET MAX_OPERATION_MEMORY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_max_operation_memory) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET MAX_OPERATION_MEMORY [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the maximum memory used for large operations (delete and insert), in bytes. Operations that use more memory are buffered to disk, slowing down the operation. The default max size is 100000. 0 means no limit.

This setting is not persistent. Admin rights are required to execute this command, as it affects all connections. It has no effect for in-memory databases. This setting can be appended to the database URL: `jdbc:h2:./test;MAX_OPERATION_MEMORY=10000`

## Example

```sql
SET MAX_OPERATION_MEMORY 0
```
