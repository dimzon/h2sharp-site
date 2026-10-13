# ANY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#any) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ANY|SOME| {BOOL_OR}}([`boolean`](../grammar/boolean.md))
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🔴 compatibility-only syntax

Returns true if any expression is true. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

Note that if `ANY` or `SOME` aggregate function is placed on the right side of comparison operation or distinct predicate and argument of this function is a subquery additional parentheses around aggregate function are required, otherwise it will be parsed as quantified predicate.

## Example

```sql
ANY(NAME LIKE 'W%')
A = (ANY((SELECT B FROM T)))
```
