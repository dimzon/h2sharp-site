# ASCII

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#ascii) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ASCII([`string`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Returns the `ASCII` value of the first character in the string. This method returns an int.

## Example

```sql
ASCII('Hi')
```
