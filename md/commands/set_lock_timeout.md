# SET LOCK_TIMEOUT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_lock_timeout) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET LOCK_TIMEOUT [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the lock timeout (in milliseconds) for the current session. The default value for this setting is 1000 (one second).

This command does not commit a transaction, and rollback does not affect it. This setting can be appended to the database URL: `jdbc:h2:./test;LOCK_TIMEOUT=10000`

## Example

```sql
SET LOCK_TIMEOUT 1000
```
