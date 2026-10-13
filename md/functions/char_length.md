# CHAR_LENGTH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#char_length) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ CHAR_LENGTH | CHARACTER_LENGTH | { LENGTH } } ( [`string`](../grammar/string.md) )
```

🔴 compatibility-only syntax

Returns the number of characters in a character string. This method returns a long.

## Example

```sql
CHAR_LENGTH(NAME)
```
