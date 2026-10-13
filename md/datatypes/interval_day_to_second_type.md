# INTERVAL DAY TO SECOND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#interval_day_to_second_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL DAY [ ( [`precisionInt`](../grammar/int.md) ) ] TO SECOND [ ( [`fractionalPrecisionInt`](../grammar/int.md) ) ]
```

Interval data type. If leading field precision is specified it should be from 1 to 18, 2 is default. If fractional seconds precision is specified it should be from 0 to 9, 6 is default.

See also [day to second interval](../grammar/interval_day_to_second.md) literal grammar. Mapped to `org.h2.api.Interval`. `java.time.Duration` is also supported.

## Example

```sql
INTERVAL DAY TO SECOND
```
