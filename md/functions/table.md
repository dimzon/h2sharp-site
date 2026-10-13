# TABLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#table) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ TABLE | TABLE_DISTINCT }
( { [`name`](../grammar/name.md) [`dataTypeOrDomain`](../grammar/data_type_or_domain.md) = {[`array`](../grammar/array.md)|[`rowValueExpression`](../grammar/row_value_expression.md)} } [,...] )
```

🟢 includes non-standard H2 syntax

Returns the result set. `TABLE_DISTINCT` removes duplicate rows.

## Example

```sql
SELECT * FROM TABLE(V INT = ARRAY[1, 2]);
SELECT * FROM TABLE(ID INT=(1, 2), NAME VARCHAR=('Hello', 'World'));
```
