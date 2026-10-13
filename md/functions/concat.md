# CONCAT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#concat) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CONCAT([`string`](../grammar/string.md), [`string`](../grammar/string.md) [,...])
```

🟢 includes non-standard H2 syntax

Combines strings. Unlike with the operator `||, NULL` parameters are ignored, and do not cause the result to become `NULL`. If all parameters are `NULL` the result is an empty string. This method returns a string.

## Example

```sql
CONCAT(NAME, '!')
```
