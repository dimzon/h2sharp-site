# FILE_READ

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#file_read) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
FILE_READ([`fileNameString`](../grammar/string.md) [,[`encodingString`](../grammar/string.md)])
```

🟢 includes non-standard H2 syntax

Returns the contents of a file. If only one parameter is supplied, the data are returned as a `BLOB`. If two parameters are used, the data is returned as a `CLOB` (text). The second parameter is the character set to use, `NULL` meaning the default character set for this system.

File names and URLs are supported. To read a stream from the classpath, use the prefix `classpath:`.

Admin rights are required to execute this command.

## Example

```sql
SELECT LENGTH(FILE_READ('~/.h2.server.properties')) LEN;
SELECT FILE_READ('http://localhost:8182/stylesheet.css', NULL) CSS;
```
