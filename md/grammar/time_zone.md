# Time zone

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#time_zone) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
AT { TIME ZONE { [`intervalHourToMinute`](interval_hour_to_minute.md) | [`intervalHourToSecond`](interval_hour_to_second.md) | { [`string`](string.md) } } | LOCAL }
```

🟢 includes non-standard H2 syntax

A time zone. Converts the timestamp with or without time zone into timestamp with time zone at specified time zone. If a day-time interval is specified as a time zone, it may not have fractional seconds and must be between -18 to 18 hours inclusive.

## Example

```sql
AT LOCAL
AT TIME ZONE '2'
AT TIME ZONE '-6:00'
AT TIME ZONE INTERVAL '10:00' HOUR TO MINUTE
AT TIME ZONE INTERVAL '10:00:00' HOUR TO SECOND
AT TIME ZONE 'UTC'
AT TIME ZONE 'Europe/London'
```
