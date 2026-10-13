# SET RETENTION_TIME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_retention_time) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET RETENTION_TIME [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

How long to retain old, persisted data, in milliseconds. The default is 45000 (45 seconds), 0 means overwrite data as early as possible. It is assumed that a file system and hard disk will flush all write buffers within this time. Using a lower value might be dangerous, unless the file system and hard disk flush the buffers earlier. To manually flush the buffers, use `CHECKPOINT SYNC`, however please note that according to various tests this does not always work as expected depending on the operating system and hardware.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. This setting can be appended to the database URL: `jdbc:h2:./test;RETENTION_TIME=0`

## Example

```sql
SET RETENTION_TIME 0
```
