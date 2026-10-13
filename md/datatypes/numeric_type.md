# NUMERIC

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#numeric_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ NUMERIC | DECIMAL | DEC } [ ( [`precisionInt`](../grammar/int.md) [ , [`scaleInt`](../grammar/int.md) ] ) ]
```

Data type with fixed decimal precision and scale. This data type is recommended for storing currency values.

If precision is specified, it must be from 1 to 100000. If scale is specified, it must be from 0 to 100000, 0 is default.

See also [numeric](../grammar/numeric.md) literal grammar. Mapped to `java.math.BigDecimal`.

## Example

```sql
NUMERIC(20, 2)
```
