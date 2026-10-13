# OCTET_LENGTH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#octet_length) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
OCTET_LENGTH([`bytes`](../grammar/bytes.md))
```

Returns the number of bytes in a binary string. This method returns a long.

## Example

```sql
OCTET_LENGTH(NAME)
```
