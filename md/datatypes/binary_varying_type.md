# BINARY VARYING

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#binary_varying_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ BINARY VARYING | VARBINARY }
[ ( [`lengthInt`](../grammar/int.md) ) ]
```

Represents a byte array.

The allowed length is from 1 to 1,000,000,000 bytes. The length is a size constraint; only the actual data is persisted.

The whole binary string is kept in memory when using this data type. For large binary data [BINARY LARGE OBJECT](binary_large_object_type.md) should be used; see there for details.

See also [bytes](../grammar/bytes.md) literal grammar. Mapped to byte[].

## Example

```sql
BINARY VARYING(100)
VARBINARY(1000)
```
