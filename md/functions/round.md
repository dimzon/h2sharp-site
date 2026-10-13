# ROUND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#round) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ROUND([`numeric`](../grammar/numeric.md) [, [`digitsInt`](../grammar/int.md)])
```

🟢 includes non-standard H2 syntax

Rounds to a number of fractional digits. This method returns value of the same type as argument, but with adjusted precision and scale, if applicable.

## Example

```sql
ROUND(N, 2)
```
