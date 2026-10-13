# BIT_NAND_AGG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#bit_nand_agg) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BIT_NAND_AGG([`expression`](../grammar/expression.md))
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

The bitwise `NAND` of all non-null values. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

For non-aggregate function see [BITNAND](../functions/bitnand.md).

## Example

```sql
BIT_NAND_AGG(X)
```
