# TIMESTAMP

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#timestamp_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TIMESTAMP [ ( [`precisionInt`](../grammar/int.md) ) ] [ WITHOUT TIME ZONE ]
```

The timestamp data type. The proleptic Gregorian calendar is used. If fractional seconds precision is specified it should be from 0 to 9, 6 is default.

This data type holds the local date and time without time zone information. It cannot distinguish timestamps near transitions from `DST` to normal time. For absolute timestamps use the [TIMESTAMP WITH TIME ZONE](timestamp_with_time_zone_type.md) data type instead.

See also [timestamp](../grammar/timestamp.md) literal grammar.

In `JDBC` this data type is mapped to `java.sql.Timestamp` (`java.util.Date` may be used too). `java.time.LocalDateTime` is also supported and recommended.

In `org.h2.api.Aggregate, org.h2.api.AggregateFunction`, and `org.h2.api.Trigger` this data type is mapped to `java.time.LocalDateTime`.

If your time zone had `LMT` (local mean time) in the past and you use such old dates (depends on the time zone, usually 100 or more years ago), don't use `java.sql.Timestamp` and `java.util.Date` to read and write them.

If you deal with very old dates (before 1582-10-15) note that `java.sql.Timestamp` and `java.util.Date` use a mixed Julian/Gregorian calendar, `java.util.GregorianCalendar` can be configured to proleptic Gregorian with `setGregorianChange(new java.util.Date(Long.MIN_VALUE))` and used to read or write fields of timestamps.

Cast from higher fractional seconds precision to lower fractional seconds precision performs round half up.

## Example

```sql
TIMESTAMP
TIMESTAMP(9)
```
