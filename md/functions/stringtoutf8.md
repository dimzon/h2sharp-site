# STRINGTOUTF8

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#stringtoutf8) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
STRINGTOUTF8([`string`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Encodes a string to a byte array using the `UTF8` encoding format. This method returns bytes.

## Example

```sql
CALL UTF8TOSTRING(STRINGTOUTF8('This is a test'))
```
