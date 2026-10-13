# Numeric

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#numeric) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`exactNumeric`](exact_numeric.md) | [`approximateNumeric`](approximate_numeric.md) | [`int`](int.md) | [`long`](long.md) | [`hexNumber`](hex_number.md) | [`octalNumber`](octal_number.md) | [`binaryNumber`](binary_number.md)
```

The data type of a numeric literal is the one of numeric data types, such as `NUMERIC, DECFLOAT, BIGINT`, or `INTEGER` depending on format and value.

An explicit `CAST` can be used to change the data type.

## Example

```sql
-1600.05
CAST(0 AS DOUBLE PRECISION)
-1.4e-10
999_999_999.999_999
```
