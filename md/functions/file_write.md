# FILE_WRITE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#file_write) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
FILE_WRITE([`blobValue`](../grammar/value.md), [`fileNameString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Write the supplied parameter into a file. Return the number of bytes written.

Write access to folder, and admin rights are required to execute this command.

## Example

```sql
SELECT FILE_WRITE('Hello world', '/tmp/hello.txt')) LEN;
```
