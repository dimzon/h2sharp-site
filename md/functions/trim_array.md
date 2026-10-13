# TRIM_ARRAY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#trim_array) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TRIM_ARRAY([`arrayExpression`](../grammar/expression.md), [`int`](../grammar/int.md))
```

Removes the specified number of elements from the end of the array.

Returns `NULL` if second parameter is `NULL` or if first parameter is `NULL` and second parameter is not negative. Throws exception if second parameter is negative or larger than number of elements in array. Otherwise returns the truncated array.

## Example

```sql
CALL TRIM_ARRAY(ARRAY[1, 2, 3, 4], 1)
```
