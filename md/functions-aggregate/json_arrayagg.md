# JSON_ARRAYAGG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#json_arrayagg) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
JSON_ARRAYAGG( [ DISTINCT|ALL ] [`expression`](../grammar/expression.md)
[ ORDER BY [`sortSpecificationList`](../grammar/sort_specification_list.md) ]
[ { NULL | ABSENT } ON NULL ] )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

🟢 includes non-standard H2 syntax

Aggregates the values into a `JSON` array. If `NULL ON NULL` is specified `NULL` values are included in the array. If no values are selected, the result is `SQL NULL` value.

## Example

```sql
JSON_ARRAYAGG(NUMBER)
```
