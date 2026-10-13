# ENCRYPT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#encrypt) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ENCRYPT([`algorithmString`](../grammar/string.md), [`keyBytes`](../grammar/bytes.md), [`dataBytes`](../grammar/bytes.md))
```

🟢 includes non-standard H2 syntax

Encrypts data using a key. The supported algorithm is `AES`. The block size is 16 bytes. This method returns bytes.

## Example

```sql
CALL ENCRYPT('AES', '00', STRINGTOUTF8('Test'))
```
