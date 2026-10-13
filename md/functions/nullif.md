# NULLIF

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#nullif) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
NULLIF([`aValue`](../grammar/value.md), [`bValue`](../grammar/value.md))
```

Returns `NULL` if 'a' is equal to 'b', otherwise 'a'.

## Example

```sql
NULLIF(A, B)
A / NULLIF(B, 0)
```
