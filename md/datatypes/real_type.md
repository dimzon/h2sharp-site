# REAL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#real_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REAL | FLOAT ( [`precisionInt`](../grammar/int.md) )
```

A single precision floating point number. Should not be used to represent currency values, because of rounding problems. Precision value for `FLOAT` type name should be from 1 to 24.

See also [numeric](../grammar/numeric.md) literal grammar. Mapped to `java.lang.Float`.

## Example

```sql
REAL
```
