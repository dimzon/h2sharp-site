# Timestamp with time zone

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#timestamp_with_time_zone) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TIMESTAMP WITH TIME ZONE '[-]yyyy-MM-dd hh:mm:ss[.nnnnnnnnn]
[ { Z } | { - | + } [`timeZoneOffsetString`](string.md) | { [`timeZoneNameString`](string.md) } ]'
```

🟢 includes non-standard H2 syntax

A timestamp with time zone literal. If name of time zone is specified it will be converted to time zone offset.

## Example

```sql
TIMESTAMP WITH TIME ZONE '2005-12-31 23:59:59Z'
TIMESTAMP WITH TIME ZONE '2005-12-31 23:59:59-10:00'
TIMESTAMP WITH TIME ZONE '2005-12-31 23:59:59.123+05'
TIMESTAMP WITH TIME ZONE '2005-12-31 23:59:59.123456789 Europe/London'
```
