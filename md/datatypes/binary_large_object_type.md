# BINARY LARGE OBJECT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#binary_large_object_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ BINARY LARGE OBJECT | BLOB }
[ ( [`lengthLong`](../grammar/long.md) [K|M|G|T|P]) ]
```

`BINARY LARGE OBJECT` is intended for very large binary values such as files or images. Unlike when using [BINARY VARYING](binary_varying_type.md), large objects are not kept fully in-memory; instead, they are streamed. Use `PreparedStatement.setBinaryStream` to store values. See also [CHARACTER LARGE OBJECT](character_large_object_type.md) and Large Objects section.

Mapped to `java.sql.Blob` (`java.io.InputStream` is also supported).

## Example

```sql
BINARY LARGE OBJECT
BLOB(10K)
```
