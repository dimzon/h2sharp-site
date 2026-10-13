# ULSHIFT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#ulshift) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ULSHIFT([`expression`](../grammar/expression.md), [`long`](../grammar/long.md))
```

🟢 includes non-standard H2 syntax

The bitwise unsigned left shift operation. Shifts the first argument by the number of bits given by the second argument. Argument should have `TINYINT, SMALLINT, INTEGER, BIGINT, BINARY`, or `BINARY VARYING` data type. This function returns result of the same data type.

If number of bits is negative, an unsigned right shift is performed instead. If number of bits is equal to or larger than number of bits in value all bits are pushed out from the value. For binary string arguments signed and unsigned shifts return the same results.

## Example

```sql
ULSHIFT(A, B)
```
