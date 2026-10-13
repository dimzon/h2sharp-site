# NVL2

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#nvl2) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
NVL2([`testValue`](../grammar/value.md), [`aValue`](../grammar/value.md), [`bValue`](../grammar/value.md))
```

🔴 compatibility-only syntax

If the test value is null, then 'b' is returned. Otherwise, 'a' is returned. The data type of the returned value is the data type of 'a' if this is a text type.

This function is provided for Oracle compatibility, use [CASE](../grammar/case_expression.md) or [COALESCE](coalesce.md) instead of it.

## Example

```sql
NVL2(X, 'not null', 'null')
```
