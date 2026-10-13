# BINARY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#binary_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BINARY [ ( [`lengthInt`](../grammar/int.md) ) ]
```

Represents a binary string (byte array) of fixed predefined length.

The allowed length is from 1 to 1,000,000,000 bytes. If length is not specified, 1 byte is used by default.

The whole binary string is kept in memory when using this data type. For variable-length binary strings use [BINARY VARYING](binary_varying_type.md) data type instead. For large binary data [BINARY LARGE OBJECT](binary_large_object_type.md) should be used; see there for details.

Too short binary string are right-padded with zero bytes. Too long binary strings are truncated by `CAST` specification and rejected by column assignment.

Binary strings of different length are considered as not equal to each other.

See also [bytes](../grammar/bytes.md) literal grammar. Mapped to byte[].

## Example

```sql
BINARY
BINARY(1000)
```
