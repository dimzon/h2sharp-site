# UUID

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#uuid_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
UUID
```

🟢 includes non-standard H2 syntax

`RFC` 9562-compliant universally unique identifier. This is a 128 bit value. To store values, use `PreparedStatement.setBytes, setString`, or `setObject(uuid)` (where `uuid` is a `java.util.UUID`). `ResultSet.getObject` will return a `java.util.UUID`.

Please note that using an index on randomly generated data will result on poor performance once there are millions of rows in a table. The reason is that the cache behavior is very bad with randomly distributed data. This is a problem for any database system. To avoid this problem use `UUID` version 7 values.

For details, see the documentation of `java.util.UUID`.

## Example

```sql
UUID
```
