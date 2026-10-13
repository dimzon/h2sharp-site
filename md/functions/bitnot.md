# BITNOT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#bitnot) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BITNOT([`expression`](../grammar/expression.md))
```

🟢 includes non-standard H2 syntax

The bitwise `NOT` operation. Argument should have `TINYINT, SMALLINT, INTEGER, BIGINT, BINARY`, or `BINARY VARYING` data type. This function returns result of the same data type.

## Example

```sql
BITNOT(A)
```
