# CHARACTER LARGE OBJECT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#character_large_object_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ { CHARACTER | CHAR } LARGE OBJECT | CLOB
| { NATIONAL CHARACTER | NCHAR } LARGE OBJECT | NCLOB }
[ ( [`lengthLong`](../grammar/long.md) [K|M|G|T|P] [CHARACTERS|OCTETS]) ]
```

`CHARACTER LARGE OBJECT` is intended for very large Unicode character string values. Unlike when using [CHARACTER VARYING](character_varying_type.md), large `CHARACTER LARGE OBJECT` values are not kept fully in-memory; instead, they are streamed. `CHARACTER LARGE OBJECT` should be used for documents and texts with arbitrary size such as XML or HTML documents, text files, or memo fields of unlimited size. Use `PreparedStatement.setCharacterStream` to store values. See also Large Objects section.

`CHARACTER VARYING` should be used for text with relatively short average size (for example shorter than 200 characters). Short `CHARACTER LARGE OBJECT` values are stored inline, but there is an overhead compared to `CHARACTER VARYING`.

Length, if any, should be specified in characters, `CHARACTERS` and `OCTETS` units have no effect in H2.

Mapped to `java.sql.Clob` (`java.io.Reader` is also supported).

## Example

```sql
CHARACTER LARGE OBJECT
CLOB(10K)
```
