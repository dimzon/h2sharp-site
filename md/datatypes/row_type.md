# ROW

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#row_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ROW ([`fieldName`](../grammar/name.md) [`dataType`](../grammar/data_type.md) [,...])
```

A row value data type. This data type should not be normally used as data type of a column.

See also [row value expression](../grammar/row_value_expression.md) grammar. Mapped to `java.sql.ResultSet`.

## Example

```sql
ROW(A INT, B VARCHAR(10))
```
