# BITGET

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#bitget) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BITGET([`expression`](../grammar/expression.md), [`long`](../grammar/long.md))
```

🟢 includes non-standard H2 syntax

Returns true if and only if the first argument has a bit set in the position specified by the second parameter. The first argument should have `TINYINT, SMALLINT, INTEGER, BIGINT, BINARY`, or `BINARY VARYING` data type. This method returns a boolean. The second argument is zero-indexed; the least significant bit has position 0.

## Example

```sql
BITGET(A, 1)
```
