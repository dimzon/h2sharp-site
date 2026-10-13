# CHAR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#char) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ CHAR | CHR } ( [`int`](../grammar/int.md) )
```

🟢 includes non-standard H2 syntax

Returns the character that represents the `ASCII` value. This method returns a string.

## Example

```sql
CHAR(65)
```
