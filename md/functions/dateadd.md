# DATEADD

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#dateadd) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ DATEADD| TIMESTAMPADD } ([`datetimeField`](../grammar/datetime_field.md), [`addIntLong`](../grammar/long.md), [`dateAndTime`](../grammar/date_and_time.md))
```

🟢 includes non-standard H2 syntax

Adds units to a date-time value. The datetimeField indicates the unit. Use negative values to subtract units. addIntLong may be a long value when manipulating milliseconds, microseconds, or nanoseconds otherwise its range is restricted to int. This method returns a value with the same type as specified value if unit is compatible with this value. If specified field is a `HOUR, MINUTE, SECOND, MILLISECOND`, etc and value is a `DATE` value `DATEADD` returns combined `TIMESTAMP`. Fields `DAY, MONTH, YEAR, WEEK`, etc are not allowed for `TIME` values. Fields `TIMEZONE_HOUR, TIMEZONE_MINUTE`, and `TIMEZONE_SECOND` are only allowed for `TIMESTAMP WITH TIME ZONE` values.

## Example

```sql
DATEADD(MONTH, 1, DATE '2001-01-31')
```
