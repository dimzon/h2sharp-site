# LOCALTIME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#localtime) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LOCALTIME [ ([`int`](../grammar/int.md)) ]
```

Returns the current time without time zone. If fractional seconds precision is specified it should be from 0 to 9, 0 is default. The specified value can be used only to limit precision of a result. The actual maximum available precision depends on operating system and `JVM` and can be 3 (milliseconds) or higher. Higher precision is not available before Java 9.

These functions return the same value within a transaction (default) or within a command depending on database mode.

[SET TIME ZONE](../commands/set_time_zone.md) command reevaluates the value for these functions using the same original `UTC` timestamp of transaction.

## Example

```sql
LOCALTIME
LOCALTIME(9)
```
