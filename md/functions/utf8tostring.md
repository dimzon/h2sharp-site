# UTF8TOSTRING

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#utf8tostring) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
UTF8TOSTRING([`bytes`](../grammar/bytes.md))
```

🟢 includes non-standard H2 syntax

Decodes a byte array in the `UTF8` format to a string.

## Example

```sql
CALL UTF8TOSTRING(STRINGTOUTF8('This is a test'))
```
