# EVERY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#every) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{EVERY| {BOOL_AND}}([`boolean`](../grammar/boolean.md))
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🔴 compatibility-only syntax

Returns true if all expressions are true. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

## Example

```sql
EVERY(ID>10)
```
