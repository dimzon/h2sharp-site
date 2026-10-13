# INTERVAL MINUTE TO SECOND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval_minute_to_second) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL [-|+] '[-|+]mm:ss[.nnnnnnnnn]' MINUTE [ ( [`precisionInt`](int.md) ) ]
TO SECOND [ ( [`fractionalPrecisionInt`](int.md) ) ]
```

An `INTERVAL MINUTE TO SECOND` literal. If leading field precision is specified it should be from 1 to 18. If fractional seconds precision is specified it should be from 0 to 9.

## Example

```sql
INTERVAL '11:12.123' MINUTE TO SECOND
```
