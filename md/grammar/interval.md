# Interval

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`intervalYear`](interval_year.md) | [`intervalMonth`](interval_month.md) | [`intervalDay`](interval_day.md) | [`intervalHour`](interval_hour.md) | [`intervalMinute`](interval_minute.md)
| [`intervalSecond`](interval_second.md) | [`intervalYearToMonth`](interval_year_to_month.md) | [`intervalDayToHour`](interval_day_to_hour.md)
| [`intervalDayToMinute`](interval_day_to_minute.md) | [`intervalDayToSecond`](interval_day_to_second.md) | [`intervalHourToMinute`](interval_hour_to_minute.md)
| [`intervalHourToSecond`](interval_hour_to_second.md) | [`intervalMinuteToSecond`](interval_minute_to_second.md)
```

An interval literal.

## Example

```sql
INTERVAL '1-2' YEAR TO MONTH
```
