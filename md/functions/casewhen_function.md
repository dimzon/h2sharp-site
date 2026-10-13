# CASEWHEN Function

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#casewhen_function) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CASEWHEN([`boolean`](../grammar/boolean.md), [`aValue`](../grammar/value.md), [`bValue`](../grammar/value.md))
```

🔴 compatibility-only syntax

Returns 'aValue' if the boolean expression is true, otherwise 'bValue'.

This function is deprecated, use [CASE](../grammar/searched_case.md) instead of it.

## Example

```sql
CASEWHEN(ID=1, 'A', 'B')
```
