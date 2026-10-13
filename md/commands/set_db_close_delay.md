# SET DB_CLOSE_DELAY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_db_close_delay) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET DB_CLOSE_DELAY [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the delay for closing a database if all connections are closed. The value -1 means the database is never closed until the close delay is set to some other value or `SHUTDOWN` is called. The value 0 means no delay (default; the database is closed if the last connection to it is closed). Values 1 and larger mean the number of seconds the database is left open after closing the last connection.

If the application exits normally or System.exit is called, the database is closed immediately, even if a delay is set.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. This setting can be appended to the database URL: `jdbc:h2:./test;DB_CLOSE_DELAY=-1`

## Example

```sql
SET DB_CLOSE_DELAY -1
```
