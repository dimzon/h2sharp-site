# INTERVAL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#interval_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`intervalYearType`](interval_year_type.md) | [`intervalMonthType`](interval_month_type.md) | [`intervalDayType`](interval_day_type.md)
| [`intervalHourType`](interval_hour_type.md)| [`intervalMinuteType`](interval_minute_type.md) | [`intervalSecondType`](interval_second_type.md)
| [`intervalYearToMonthType`](interval_year_to_month_type.md) | [`intervalDayToHourType`](interval_day_to_hour_type.md)
| [`intervalDayToMinuteType`](interval_day_to_minute_type.md) | [`intervalDayToSecondType`](interval_day_to_second_type.md)
| [`intervalHourToMinuteType`](interval_hour_to_minute_type.md) | [`intervalHourToSecondType`](interval_hour_to_second_type.md)
| [`intervalMinuteToSecondType`](interval_minute_to_second_type.md)
```

Interval data type. There are two classes of intervals. Year-month intervals can store years and months. Day-time intervals can store days, hours, minutes, and seconds. Year-month intervals are comparable only with another year-month intervals. Day-time intervals are comparable only with another day-time intervals.

Mapped to `org.h2.api.Interval`.

## Example

```sql
INTERVAL DAY TO SECOND
```
