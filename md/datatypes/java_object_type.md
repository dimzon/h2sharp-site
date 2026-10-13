# JAVA_OBJECT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#java_object_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ JAVA_OBJECT | OBJECT | OTHER } [ ( [`lengthInt`](../grammar/int.md) ) ]
```

🟢 includes non-standard H2 syntax

This type allows storing serialized Java objects. Internally, a byte array with serialized form is used. The allowed length is from 1 (useful only with custom serializer) to 1,000,000,000 bytes. The length is a size constraint; only the actual data is persisted.

Serialization and deserialization is done on the client side only with two exclusions described below. Deserialization is only done when `getObject` is called. Java operations cannot be executed inside the database engine for security reasons. Use `PreparedStatement.setObject` with `Types.JAVA_OBJECT` or `H2Type.JAVA_OBJECT` as a third argument to store values.

If Java method alias has `Object` parameter(s), values are deserialized during invocation of this method on the server side.

If a linked table has a column with `Types.JAVA_OBJECT JDBC` data type and its database is not an another H2, Java objects need to be serialized and deserialized during interaction between H2 and database that owns the table on the server side of H2.

This data type needs special attention in secure environments.

Mapped to `java.lang.Object` (or any subclass).

## Example

```sql
JAVA_OBJECT
JAVA_OBJECT(10000)
```
