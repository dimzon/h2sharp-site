# BITXOR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#bitxor) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BITXOR([`expression`](../grammar/expression.md), [`expression`](../grammar/expression.md))
```

🟢 includes non-standard H2 syntax

Arguments should have `TINYINT, SMALLINT, INTEGER, BIGINT, BINARY`, or `BINARY VARYING` data type. This function returns result of the same data type.

For aggregate function see [BIT_XOR_AGG](../functions-aggregate/bit_xor_agg.md).

## Example

```sql
The bitwise XOR operation.
```
