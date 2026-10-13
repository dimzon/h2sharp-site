# DECFLOAT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#decfloat_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DECFLOAT [ ( [`precisionInt`](../grammar/int.md) ) ]
```

Decimal floating point number. This data type is not recommended to represent currency values, because of variable scale.

If precision is specified, it must be from 1 to 100000.

See also [numeric](../grammar/numeric.md) literal grammar. Mapped to `java.math.BigDecimal`. There are three special values: 'Infinity', '-Infinity', and 'NaN'. These special values can't be read or set as `BigDecimal` values, but they can be read or set using `java.lang.String`, float, or double.

## Example

```sql
DECFLOAT
DECFLOAT(20)
```
