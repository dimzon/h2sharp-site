# ROTATELEFT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#rotateleft) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ROTATELEFT([`expression`](../grammar/expression.md), [`long`](../grammar/long.md))
```

🟢 includes non-standard H2 syntax

The bitwise left rotation operation. Rotates the first argument by the number of bits given by the second argument. Argument should have `TINYINT, SMALLINT, INTEGER, BIGINT, BINARY`, or `BINARY VARYING` data type. This function returns result of the same data type.

## Example

```sql
ROTATELEFT(A, B)
```
