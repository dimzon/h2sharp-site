# FORMATDATETIME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#formatdatetime) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
FORMATDATETIME ( [`dateAndTime`](../grammar/date_and_time.md), [`formatString`](../grammar/string.md)
[ , [`localeString`](../grammar/string.md) [ , [`timeZoneString`](../grammar/string.md) ] ] )
```

🟢 includes non-standard H2 syntax

Formats a date, time or timestamp as a string. The most important format characters are: y year, M month, d day, H hour, m minute, s second. For details of the format, see `java.time.format.DateTimeFormatter`. Allowed format characters depend on data type of passed date/time value.

If timeZoneString is specified, it is used in formatted string if formatString has time zone. For `TIME` and `TIME WITH TIME ZONE` values the specified time zone must have a fixed offset.

If `TIME WITH TIME ZONE` is passed and timeZoneString is specified, the time is converted to the specified time zone offset and its `UTC` value is preserved. If `TIMESTAMP WITH TIME ZONE` is passed and timeZoneString is specified, the timestamp is converted to the specified time zone and its `UTC` value is preserved.

This method returns a string.

See also [cast specification](../grammar/cast_specification.md).

## Example

```sql
CALL FORMATDATETIME(TIMESTAMP '2001-02-03 04:05:06',
    'EEE, d MMM yyyy HH:mm:ss z', 'en', 'GMT')
```
