# TRUNC

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#trunc) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ TRUNC | TRUNCATE } ( { {[`numeric`](../grammar/numeric.md) [, [`digitsInt`](../grammar/int.md)] }
| { [`timestamp`](../grammar/timestamp.md) | [`timestampWithTimeZone`](../grammar/timestamp_with_time_zone.md) | [`date`](../grammar/date.md) | [`timestampString`](../grammar/string.md) } } )
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

When a numeric argument is specified, truncates it to a number of digits (to the next value closer to 0) and returns value of the same type as argument, but with adjusted precision and scale, if applicable.

This function with datetime or string argument is deprecated, use [DATE_TRUNC](date_trunc.md) instead. When used with a timestamp, truncates the timestamp to a date (day) value and returns a timestamp with or without time zone depending on type of the argument. When used with a date, returns a timestamp at start of this date. When used with a timestamp as string, truncates the timestamp to a date (day) value and returns a timestamp without time zone.

## Example

```sql
TRUNCATE(N, 2)
```
