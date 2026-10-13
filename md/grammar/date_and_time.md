# Date and time

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#date_and_time) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`date`](date.md) | [`time`](time.md) | [`timeWithTimeZone`](time_with_time_zone.md) | [`timestamp`](timestamp.md) | [`timestampWithTimeZone`](timestamp_with_time_zone.md)
```

A literal value of any date-time data type.

## Example

```sql
TIMESTAMP '1999-01-31 10:00:00'
```
