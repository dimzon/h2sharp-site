# SET DEFAULT_LOCK_TIMEOUT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_default_lock_timeout) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET DEFAULT_LOCK_TIMEOUT [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the default lock timeout (in milliseconds) in this database that is used for the new sessions. The default value for this setting is 1000 (one second).

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent.

## Example

```sql
SET DEFAULT_LOCK_TIMEOUT 5000
```
