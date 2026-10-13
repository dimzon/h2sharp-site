# LOG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#log) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LOG({[`baseNumeric`](../grammar/numeric.md), [`numeric`](../grammar/numeric.md) | {[`numeric`](../grammar/numeric.md)}})
```

🔴 compatibility-only syntax

Calculates the logarithm with specified base as a double value. Argument and base must be positive numeric values. Base cannot be equal to 1.

The default base is e (natural logarithm), in the PostgreSQL mode the default base is base 10. In `MSSQLServer` mode the optional base is specified after the argument.

Single-argument variant of `LOG` function is deprecated, use [LN](ln.md) or [LOG10](log10.md) instead.

## Example

```sql
LOG(2, A)
```
