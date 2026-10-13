# CHARACTER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#character_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ CHARACTER | CHAR | NATIONAL { CHARACTER | CHAR } | NCHAR }
[ ( [`lengthInt`](../grammar/int.md) [CHARACTERS|OCTETS] ) ]
```

A Unicode String of fixed length.

Length, if any, should be specified in characters, `CHARACTERS` and `OCTETS` units have no effect in H2. The allowed length is from 1 to 1,000,000,000 characters. If length is not specified, 1 character is used by default.

The whole text is kept in memory when using this data type. For variable-length strings use [CHARACTER VARYING](character_varying_type.md) data type instead. For large text data [CHARACTER LARGE OBJECT](character_large_object_type.md) should be used; see there for details.

Too short strings are right-padded with space characters. Too long strings are truncated by `CAST` specification and rejected by column assignment.

Two `CHARACTER` strings of different length are considered as equal if all additional characters in the longer string are space characters.

See also [string](../grammar/string.md) literal grammar. Mapped to `java.lang.String`.

## Example

```sql
CHARACTER
CHAR(10)
```
