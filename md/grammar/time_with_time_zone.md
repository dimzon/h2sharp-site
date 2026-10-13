# Time with time zone

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#time_with_time_zone) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TIME WITH TIME ZONE 'hh:mm:ss[.nnnnnnnnn]{ { Z } | { - | + } [`timeZoneOffsetString`](string.md)}'
```

🟢 includes non-standard H2 syntax

A time with time zone literal. A value is between 0:00:00 and 23:59:59.999999999 and has nanosecond resolution.

## Example

```sql
TIME WITH TIME ZONE '23:59:59+01'
TIME WITH TIME ZONE '10:15:30.334-03:30'
TIME WITH TIME ZONE '0:00:00Z'
```
