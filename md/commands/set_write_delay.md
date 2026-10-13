# SET WRITE_DELAY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_write_delay) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET WRITE_DELAY [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Set the maximum delay between a commit and flushing the log, in milliseconds. This setting is persistent. The default is 500 ms.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting can be appended to the database URL: `jdbc:h2:./test;WRITE_DELAY=0`

## Example

```sql
SET WRITE_DELAY 2000
```
