# REGR_SYY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#regr_syy) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REGR_SYY([`dependentExpression`](../grammar/expression.md), [`independentExpression`](../grammar/expression.md))
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

The the sum of squares of dependent expression. Rows in which either argument is `NULL` are ignored in the calculation. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

## Example

```sql
REGR_SYY(Y, X)
```
