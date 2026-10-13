# MODE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#mode) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ MODE() WITHIN GROUP (ORDER BY [`sortSpecification`](../grammar/sort_specification.md)) }
| { MODE( [`value`](../grammar/value.md) [ ORDER BY [`sortSpecification`](../grammar/sort_specification.md) ] ) }
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Returns the value that occurs with the greatest frequency. If there are multiple values with the same frequency only one value will be returned. In this situation value will be chosen based on optional `ORDER BY` clause that should specify exactly the same expression as argument of this function. Use ascending order to get smallest value or descending order to get largest value from multiple values with the same frequency. If this clause is not specified the exact chosen value is not determined in this situation. `NULL` values are ignored in the calculation. If no rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

## Example

```sql
MODE() WITHIN GROUP (ORDER BY X)
```
