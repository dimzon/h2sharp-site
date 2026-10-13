# INTERVAL HOUR TO SECOND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval_hour_to_second) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL [-|+] '[-|+]hh:mm:ss[.nnnnnnnnn]' HOUR [ ( [`precisionInt`](int.md) ) ]
TO SECOND [ ( [`fractionalPrecisionInt`](int.md) ) ]
```

An `INTERVAL HOUR TO SECOND` literal. If leading field precision is specified it should be from 1 to 18. If fractional seconds precision is specified it should be from 0 to 9.

## Example

```sql
INTERVAL '10:11:12.123' HOUR TO SECOND
```
