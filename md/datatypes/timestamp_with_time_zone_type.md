# TIMESTAMP WITH TIME ZONE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#timestamp_with_time_zone_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TIMESTAMP [ ( [`precisionInt`](../grammar/int.md) ) ] WITH TIME ZONE
```

The timestamp with time zone data type. The proleptic Gregorian calendar is used. If fractional seconds precision is specified it should be from 0 to 9, 6 is default.

See also [timestamp with time zone](../grammar/timestamp_with_time_zone.md) literal grammar. Mapped to `java.time.OffsetDateTime`. `java.time.ZonedDateTime` and `java.time.Instant` are also supported.

Values of this data type are compared by `UTC` values. It means that `2010-01-01 10:00:00+01` is greater than `2010-01-01 11:00:00+03`.

Conversion to `TIMESTAMP` uses time zone offset to get `UTC` time and converts it to local time using the system time zone. Conversion from `TIMESTAMP` does the same operations in reverse and sets time zone offset to offset of the system time zone. Cast from higher fractional seconds precision to lower fractional seconds precision performs round half up.

## Example

```sql
TIMESTAMP WITH TIME ZONE
TIMESTAMP(9) WITH TIME ZONE
```
