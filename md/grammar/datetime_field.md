# Datetime field

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#datetime_field) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`yearField`](year_field.md) | [`monthField`](month_field.md) | [`dayOfMonthField`](day_of_month_field.md)
| [`hourField`](hour_field.md) | [`minuteField`](minute_field.md) | [`secondField`](second_field.md)
| [`timezoneHourField`](timezone_hour_field.md) | [`timezoneMinuteField`](timezone_minute_field.md)
| { [`timezoneSecondField`](timezone_second_field.md)
| [`millenniumField`](millennium_field.md) | [`centuryField`](century_field.md) | [`decadeField`](decade_field.md)
| [`quarterField`](quarter_field.md)
| [`millisecondField`](millisecond_field.md) | [`microsecondField`](microsecond_field.md) | [`nanosecondField`](nanosecond_field.md)
| [`dayOfYearField`](day_of_year_field.md)
| [`isoDayOfWeekField`](iso_day_of_week_field.md) | [`isoWeekField`](iso_week_field.md) | [`isoWeekYearField`](iso_week_year_field.md)
| [`dayOfWeekField`](day_of_week_field.md) | [`weekField`](week_field.md) | [`weekYearField`](week_year_field.md)
| [`epochField`](epoch_field.md) }
```

🟢 includes non-standard H2 syntax

Fields for `EXTRACT, DATEADD, DATEDIFF`, and `DATE_TRUNC` functions.

## Example

```sql
YEAR
```
