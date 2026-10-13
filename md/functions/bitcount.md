# BITCOUNT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#bitcount) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BITCOUNT([`expression`](../grammar/expression.md))
```

🟢 includes non-standard H2 syntax

Returns count of set bits in the specified value. Value should have `TINYINT, SMALLINT, INTEGER, BIGINT, BINARY`, or `BINARY VARYING` data type. This method returns a long.

## Example

```sql
BITCOUNT(A)
```
