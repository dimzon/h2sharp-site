# GCD

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#gcd) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
GCD([`numeric`](../grammar/numeric.md), [`numeric`](../grammar/numeric.md) [,...])
```

🟢 includes non-standard H2 syntax

Returns the greatest common divisor of specified arguments. Arguments must have `TINYINT, SMALLINT, INTEGER, BIGINT`, or `NUMERIC` data type with scale 0. This function returns result of `NUMERIC` data type with scale 0.

For aggregate function see [GCD_AGG](../functions-aggregate/gcd_agg.md).

## Example

```sql
GCD(A, B)
```
