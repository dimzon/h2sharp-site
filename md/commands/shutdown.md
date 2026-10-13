# SHUTDOWN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#shutdown) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SHUTDOWN [ IMMEDIATELY | COMPACT | DEFRAG ]
```

🟢 includes non-standard H2 syntax

This statement closes all open connections to the database and closes the database. This command is usually not required, as the database is closed automatically when the last connection to it is closed.

If no option is used, then the database is closed normally. All connections are closed, open transactions are rolled back.

`SHUTDOWN COMPACT` fully compacts the database (re-creating the database may further reduce the database size). If the database is closed normally (using `SHUTDOWN` or by closing all connections), then the database is also compacted, but only for at most the time defined by the database setting `h2.maxCompactTime` in milliseconds (see there).

`SHUTDOWN IMMEDIATELY` closes the database files without any cleanup and without compacting.

`SHUTDOWN DEFRAG` is currently equivalent to `COMPACT`.

Admin rights are required to execute this command.

## Example

```sql
SHUTDOWN COMPACT
```
