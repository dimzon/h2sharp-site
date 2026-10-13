# SET TIME ZONE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_time_zone) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET TIME ZONE { LOCAL | [`intervalHourToMinute`](../grammar/interval_hour_to_minute.md) | { [`intervalHourToSecond`](../grammar/interval_hour_to_second.md) | [`string`](../grammar/string.md) } }
```

🟢 includes non-standard H2 syntax

Sets the current time zone for the session.

This command does not commit a transaction, and rollback does not affect it. This setting can be appended to the database URL: `jdbc:h2:./test;TIME ZONE='1:00'`

Time zone offset used for [CURRENT_TIME](../functions/current_time.md), [CURRENT_TIMESTAMP](../functions/current_timestamp.md), [CURRENT_DATE](../functions/current_date.md), [LOCALTIME](../functions/localtime.md), and [LOCALTIMESTAMP](../functions/localtimestamp.md) is adjusted, so these functions will return new values based on the same `UTC` timestamp after execution of this command.

## Example

```sql
SET TIME ZONE LOCAL
SET TIME ZONE '-5:00'
SET TIME ZONE INTERVAL '1:00' HOUR TO MINUTE
SET TIME ZONE 'Europe/London'
```
