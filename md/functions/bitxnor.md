# BITXNOR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#bitxnor) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BITXNOR([`expression`](../grammar/expression.md), [`expression`](../grammar/expression.md))
```

🟢 includes non-standard H2 syntax

The bitwise `XNOR` operation equivalent to `BITNOT(BITXOR(expression, expression))`. Arguments should have `TINYINT, SMALLINT, INTEGER, BIGINT, BINARY`, or `BINARY VARYING` data type. This function returns result of the same data type.

For aggregate function see [BIT_XNOR_AGG](../functions-aggregate/bit_xnor_agg.md).

## Example

```sql
BITXNOR(A, B)
```
