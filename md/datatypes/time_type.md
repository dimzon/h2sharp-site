# TIME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#time_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TIME [ ( [`precisionInt`](../grammar/int.md) ) ] [ WITHOUT TIME ZONE ]
```

The time data type. The format is hh:mm:ss[.nnnnnnnnn]. If fractional seconds precision is specified it should be from 0 to 9, 0 is default.

See also [time](../grammar/time.md) literal grammar.

In `JDBC` this data type is mapped to `java.sql.Time`. `java.time.LocalTime` is also supported and recommended.

In `org.h2.api.Aggregate, org.h2.api.AggregateFunction`, and `org.h2.api.Trigger` this data type is mapped to `java.time.LocalTime`.

Use `java.time.LocalTime` or `String` instead of `java.sql.Time` when non-zero precision is needed. Cast from higher fractional seconds precision to lower fractional seconds precision performs round half up; if result of rounding is higher than maximum supported value 23:59:59.999999999 the value is rounded down instead. The `CAST` operation to `TIMESTAMP` and `TIMESTAMP WITH TIME ZONE` data types uses the [CURRENT_DATE](../functions/current_date.md) for date fields.

## Example

```sql
TIME
TIME(9)
```
