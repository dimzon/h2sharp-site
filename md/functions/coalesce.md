# COALESCE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#coalesce) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ COALESCE | { NVL } } ([`aValue`](../grammar/value.md), [`bValue`](../grammar/value.md) [,...])
| IFNULL([`aValue`](../grammar/value.md), [`bValue`](../grammar/value.md))
```

🔴 compatibility-only syntax

Returns the first value that is not null.

## Example

```sql
COALESCE(A, B, C)
```
