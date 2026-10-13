# MAX

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#max) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
MAX([`value`](../grammar/value.md))
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

The highest value. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements. The returned value is of the same data type as the parameter.

## Example

```sql
MAX(NAME)
```
