# ANY_VALUE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#any_value) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ANY_VALUE( [ DISTINCT|ALL ] [`value`](../grammar/value.md) )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Returns any non-`NULL` value from aggregated values. If no rows are selected, the result is `NULL`. This function uses the same pseudo random generator as [RAND()](../functions/rand.md) function.

If `DISTINCT` is specified, each distinct value will be returned with approximately the same probability as other distinct values. If it isn't specified, more frequent values will be returned with higher probability than less frequent.

Aggregates are only allowed in select statements.

## Example

```sql
ANY_VALUE(X)
```
