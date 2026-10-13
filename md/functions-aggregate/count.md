# COUNT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#count) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
COUNT( { * | { [ DISTINCT|ALL ] [`expression`](../grammar/expression.md) } } )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

The count of all row, or of the non-null values. This method returns a long. If no rows are selected, the result is 0. Aggregates are only allowed in select statements.

## Example

```sql
COUNT(*)
```
