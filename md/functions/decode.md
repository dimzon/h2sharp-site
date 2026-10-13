# DECODE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#decode) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DECODE([`value`](../grammar/value.md), [`whenValue`](../grammar/value.md), [`thenValue`](../grammar/value.md) [,...])
```

🔴 compatibility-only syntax

Returns the first matching value. `NULL` is considered to match `NULL`. If no match was found, then `NULL` or the last parameter (if the parameter count is even) is returned. This function is provided for Oracle compatibility, use [CASE](../grammar/case_expression.md) instead of it.

## Example

```sql
CALL DECODE(RAND()>0.5, 0, 'Red', 1, 'Black');
```
