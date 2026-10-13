# BIT_AND_AGG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#bit_and_agg) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{{BIT_AND_AGG}|{BIT_AND}}([`expression`](../grammar/expression.md))
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

The bitwise `AND` of all non-null values. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

For non-aggregate function see [BITAND](../functions/bitand.md).

## Example

```sql
BIT_AND_AGG(X)
```
