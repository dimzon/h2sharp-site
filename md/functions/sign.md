# SIGN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#sign) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SIGN( { [`numeric`](../grammar/numeric.md) | [`interval`](../grammar/interval.md) } )
```

🟢 includes non-standard H2 syntax

Returns -1 if the value is smaller than 0, 0 if zero or NaN, and otherwise 1.

## Example

```sql
SIGN(N)
```
