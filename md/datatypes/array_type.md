# ARRAY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#array_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`baseDataType`](../grammar/data_type.md) ARRAY [ '[' [`maximumCardinalityInt`](../grammar/int.md) ']' ]
```

A data type for array of values. Base data type specifies the data type of elements. Array may have `NULL` elements. Maximum cardinality, if any, specifies maximum allowed number of elements in the array. The allowed cardinality is from 0 to 65536 elements.

See also [array](../grammar/array.md) literal grammar. Mapped to `java.lang.Object[]` (arrays of any non-primitive type are also supported).

Use `PreparedStatement.setArray(..)` or `PreparedStatement.setObject(.., new Object[] {..})` to store values, and `ResultSet.getObject(..)` or `ResultSet.getArray(..)` to retrieve the values.

## Example

```sql
BOOLEAN ARRAY
VARCHAR(100) ARRAY
INTEGER ARRAY[10]
```
