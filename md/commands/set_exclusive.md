# SET EXCLUSIVE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_exclusive) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET EXCLUSIVE { 0 | 1 | 2 }
```

🟢 includes non-standard H2 syntax

Switched the database to exclusive mode (1, 2) and back to normal mode (0).

In exclusive mode, new connections are rejected, and operations by other connections are paused until the exclusive mode is disabled. When using the value 1, existing connections stay open. When using the value 2, all existing connections are closed (and current transactions are rolled back) except the connection that executes `SET EXCLUSIVE`. Only the connection that set the exclusive mode can disable it. When the connection is closed, it is automatically disabled.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
SET EXCLUSIVE 1
```
