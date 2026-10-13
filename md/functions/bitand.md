# BITAND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#bitand) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BITAND([`expression`](../grammar/expression.md), [`expression`](../grammar/expression.md))
```

🟢 includes non-standard H2 syntax

The bitwise `AND` operation. Arguments should have `TINYINT, SMALLINT, INTEGER, BIGINT, BINARY`, or `BINARY VARYING` data type. This function returns result of the same data type.

For aggregate function see [BIT_AND_AGG](../functions-aggregate/bit_and_agg.md).

## Example

```sql
BITAND(A, B)
```
