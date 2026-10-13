# LOCALTIMESTAMP

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#localtimestamp) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LOCALTIMESTAMP [ ([`int`](../grammar/int.md)) ]
```

Returns the current timestamp without time zone. If fractional seconds precision is specified it should be from 0 to 9, 6 is default. The specified value can be used only to limit precision of a result. The actual maximum available precision depends on operating system and `JVM` and can be 3 (milliseconds) or higher. Higher precision is not available before Java 9.

The returned value has date and time without time zone information. If time zone has `DST` transitions the returned values are ambiguous during transition from `DST` to normal time. For absolute timestamps use the [CURRENT_TIMESTAMP](current_timestamp.md) function and [TIMESTAMP WITH TIME ZONE](../datatypes/timestamp_with_time_zone_type.md) data type.

These functions return the same value within a transaction (default) or within a command depending on database mode.

[SET TIME ZONE](../commands/set_time_zone.md) reevaluates the value for these functions using the same original `UTC` timestamp of transaction.

## Example

```sql
LOCALTIMESTAMP
LOCALTIMESTAMP(9)
```
