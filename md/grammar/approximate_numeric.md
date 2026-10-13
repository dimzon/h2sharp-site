# Approximate numeric

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#approximate_numeric) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[ + | - ] { { [`number`](number.md) [ . [ [`number`](number.md) ] ] } | { . [`number`](number.md) } }
E [ + | - ] [`expNumber`](number.md)
```

An approximate numeric value. Approximate numeric values have [DECFLOAT](../datatypes/decfloat_type.md) data type. To define a [DOUBLE PRECISION](../datatypes/double_precision_type.md) value, use `CAST(X AS DOUBLE PRECISION)`. To define a [REAL](../datatypes/real_type.md) value, use `CAST(X AS REAL)`. There are some special `REAL, DOUBLE PRECISION`, and `DECFLOAT` values: to represent positive infinity, use `CAST('Infinity' AS dataType)`; for negative infinity, use `CAST('-Infinity' AS dataType)`; for `NaN` (not a number), use `CAST('NaN' AS dataType)`.

## Example

```sql
-1.4e-10
1.111_111E3
CAST(1e2 AS REAL)
CAST('NaN' AS DOUBLE PRECISION)
```
