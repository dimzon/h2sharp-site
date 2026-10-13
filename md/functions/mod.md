# MOD

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#mod) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
MOD([`dividendNumeric`](../grammar/numeric.md), [`divisorNumeric`](../grammar/numeric.md))
```

The modulus expression.

Result has the same type as divisor. Result is `NULL` if either of arguments is `NULL`. If divisor is 0, an exception is raised. Result has the same sign as dividend or is equal to 0.

Usually arguments should have scale 0, but it isn't required by H2.

## Example

```sql
MOD(A, B)
```
