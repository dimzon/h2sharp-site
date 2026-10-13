# CHARACTER VARYING

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#character_varying_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ { CHARACTER | CHAR } VARYING
| VARCHAR
| { NATIONAL { CHARACTER | CHAR } | NCHAR } VARYING
| { VARCHAR_CASESENSITIVE } }
[ ( [`lengthInt`](../grammar/int.md) [CHARACTERS|OCTETS] ) ]
```

🟢 includes non-standard H2 syntax

A Unicode String. Use two single quotes ('') to create a quote.

The allowed length is from 1 to 1,000,000,000 characters. The length is a size constraint; only the actual data is persisted. Length, if any, should be specified in characters, `CHARACTERS` and `OCTETS` units have no effect in H2.

The whole text is loaded into memory when using this data type. For large text data [CHARACTER LARGE OBJECT](character_large_object_type.md) should be used; see there for details.

See also [string](../grammar/string.md) literal grammar. Mapped to `java.lang.String`.

## Example

```sql
CHARACTER VARYING(100)
VARCHAR(255)
```
