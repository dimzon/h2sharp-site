# LISTAGG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#listagg) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LISTAGG ( [ DISTINCT|ALL ] [`string`](../grammar/string.md) [, [`separatorString`](../grammar/string.md)]
[ ON OVERFLOW { ERROR
| TRUNCATE [ [`filterString`](../grammar/string.md) ] { WITH | WITHOUT } COUNT } ] )
[`withinGroupSpecification`](../grammar/within_group_specification.md)
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

Concatenates strings with a separator. The default separator is a ',' (without space). This method returns a string. `NULL` values are ignored in the calculation, `COALESCE` can be used to replace them. If no rows are selected, the result is `NULL`.

If `ON OVERFLOW TRUNCATE` is specified, values that don't fit into returned string are truncated and replaced with filter string placeholder ('...' by default) and count of truncated elements in parentheses. If `WITHOUT COUNT` is specified, count of truncated elements is not appended.

Aggregates are only allowed in select statements.

## Example

```sql
LISTAGG(NAME, ', ') WITHIN GROUP (ORDER BY ID)
LISTAGG(COALESCE(NAME, 'null'), ', ') WITHIN GROUP (ORDER BY ID)
LISTAGG(ID, ', ') WITHIN GROUP (ORDER BY ID) OVER (ORDER BY ID)
LISTAGG(ID, ';' ON OVERFLOW TRUNCATE 'etc' WITHOUT COUNT) WITHIN GROUP (ORDER BY ID)
```
