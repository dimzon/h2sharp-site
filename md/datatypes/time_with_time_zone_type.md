# TIME WITH TIME ZONE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#time_with_time_zone_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TIME [ ( [`precisionInt`](../grammar/int.md) ) ] WITH TIME ZONE
```

The time with time zone data type. If fractional seconds precision is specified it should be from 0 to 9, 0 is default.

See also [time with time zone](../grammar/time_with_time_zone.md) literal grammar. Mapped to `java.time.OffsetTime`. Cast from higher fractional seconds precision to lower fractional seconds precision performs round half up; if result of rounding is higher than maximum supported value 23:59:59.999999999 the value is rounded down instead. The `CAST` operation to `TIMESTAMP` and `TIMESTAMP WITH TIME ZONE` data types uses the [CURRENT_DATE](../functions/current_date.md) for date fields.

## Example

```sql
TIME WITH TIME ZONE
TIME(9) WITH TIME ZONE
```
