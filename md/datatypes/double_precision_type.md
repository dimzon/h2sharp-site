# DOUBLE PRECISION

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#double_precision_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DOUBLE PRECISION | FLOAT [ ( [`precisionInt`](../grammar/int.md) ) ]
```

A double precision floating point number. Should not be used to represent currency values, because of rounding problems. If precision value is specified for `FLOAT` type name, it should be from 25 to 53.

See also [numeric](../grammar/numeric.md) literal grammar. Mapped to `java.lang.Double`.

## Example

```sql
DOUBLE PRECISION
```
