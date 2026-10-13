# LAST_DAY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#last_day) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LAST_DAY([`date`](../grammar/date.md) | [`timestamp`](../grammar/timestamp.md) | [`timestampWithTimeZone`](../grammar/timestamp_with_time_zone.md) | [`string`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Returns the last day of the month that contains the specified date-time value. This function returns a date.

## Example

```sql
LAST_DAY(DAY, DATE '2020-02-05');
```
