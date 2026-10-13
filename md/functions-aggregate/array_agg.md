# ARRAY_AGG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#array_agg) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY_AGG ( [ DISTINCT|ALL ] [`value`](../grammar/value.md)
[ ORDER BY [`sortSpecificationList`](../grammar/sort_specification_list.md) ] )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Aggregate the value into an array. This method returns an array. `NULL` values are included in the array, `FILTER` clause can be used to exclude them. If no rows are selected, the result is `NULL`. If `ORDER BY` is not specified order of values is not determined. When this aggregate is used with `OVER` clause that contains `ORDER BY` subclause it does not enforce exact order of values. This aggregate needs additional own `ORDER BY` clause to make it deterministic. Aggregates are only allowed in select statements.

## Example

```sql
ARRAY_AGG(NAME ORDER BY ID)
ARRAY_AGG(NAME ORDER BY ID) FILTER (WHERE NAME IS NOT NULL)
ARRAY_AGG(ID ORDER BY ID) OVER (ORDER BY ID)
```
