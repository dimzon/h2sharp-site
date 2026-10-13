# LCM

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#lcm) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LCM([`numeric`](../grammar/numeric.md), [`numeric`](../grammar/numeric.md) [,...])
```

🟢 includes non-standard H2 syntax

Returns the least common multiple of specified arguments. Arguments must have `TINYINT, SMALLINT, INTEGER, BIGINT`, or `NUMERIC` data type with scale 0. This function returns result of `NUMERIC` data type with scale 0.

For aggregate function see [LCM_AGG](../functions-aggregate/lcm_agg.md).

## Example

```sql
LCM(A, B)
```
