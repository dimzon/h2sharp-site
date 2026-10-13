# DECRYPT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#decrypt) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DECRYPT([`algorithmString`](../grammar/string.md), [`keyBytes`](../grammar/bytes.md), [`dataBytes`](../grammar/bytes.md))
```

🟢 includes non-standard H2 syntax

Decrypts data using a key. The supported algorithm is `AES`. The block size is 16 bytes. This method returns bytes.

## Example

```sql
CALL TRIM(CHAR(0) FROM UTF8TOSTRING(
    DECRYPT('AES', '00', '3fabb4de8f1ee2e97d7793bab2db1116')))
```
