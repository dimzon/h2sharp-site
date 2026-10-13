# CURRENT_TIMESTAMP

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#current_timestamp) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CURRENT_TIMESTAMP [ ([`int`](../grammar/int.md)) ]
```

Returns the current timestamp with time zone. Time zone offset is set to a current time zone offset. If fractional seconds precision is specified it should be from 0 to 9, 6 is default. The specified value can be used only to limit precision of a result. The actual maximum available precision depends on operating system and `JVM` and can be 3 (milliseconds) or higher. Higher precision is not available before Java 9.

This function returns the same value within a transaction (default) or within a command depending on database mode.

[SET TIME ZONE](../commands/set_time_zone.md) command reevaluates the value for this function using the same original `UTC` timestamp of transaction.

## Example

```sql
CURRENT_TIMESTAMP
CURRENT_TIMESTAMP(9)
```
