# SET LOCK_MODE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_lock_mode) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET LOCK_MODE [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the lock mode. The values 0, 1, 2, and 3 are supported. The default is 3. This setting affects all connections.

The value 0 means no locking (should only be used for testing). Please note that using `SET LOCK_MODE` 0 while at the same time using multiple connections may result in inconsistent transactions.

The value 3 means row-level locking for write operations.

The values 1 and 2 have the same effect as 3.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. This setting can be appended to the database URL: `jdbc:h2:./test;LOCK_MODE=0`

## Example

```sql
SET LOCK_MODE 0
```
