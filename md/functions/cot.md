# COT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#cot) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
COT([`numeric`](../grammar/numeric.md))
```

🟢 includes non-standard H2 syntax

Calculate the trigonometric cotangent (`1/TAN(ANGLE)`).

This function returns a double precision value.

## Example

```sql
COT(ANGLE)
```
