# CONCAT_WS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#concat_ws) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CONCAT_WS([`separatorString`](../grammar/string.md), [`string`](../grammar/string.md), [`string`](../grammar/string.md) [,...])
```

🟢 includes non-standard H2 syntax

Combines strings with separator. If separator is `NULL` it is treated like an empty string. Other `NULL` parameters are ignored. Remaining non-`NULL` parameters, if any, are concatenated with the specified separator. If there are no remaining parameters the result is an empty string. This method returns a string.

## Example

```sql
CONCAT_WS(',', NAME, '!')
```
