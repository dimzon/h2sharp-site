# ABS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#abs) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ABS( { [`numeric`](../grammar/numeric.md) | [`interval`](../grammar/interval.md) } )
```

Returns the absolute value of a specified value. The returned value is of the same data type as the parameter.

Note that `TINYINT, SMALLINT, INT`, and `BIGINT` data types cannot represent absolute values of their minimum negative values, because they have more negative values than positive. For example, for `INT` data type allowed values are from -2147483648 to 2147483647. `ABS`(-2147483648) should be 2147483648, but this value is not allowed for this data type. It leads to an exception. To avoid it cast argument of this function to a higher data type.

## Example

```sql
ABS(I)
ABS(CAST(I AS BIGINT))
```
