# JSON

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#json_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
JSON [([`lengthInt`](../grammar/int.md))]
```

🟢 includes non-standard H2 syntax

A `RFC` 8259-compliant `JSON` text.

See also [json](../grammar/json.md) literal grammar. Mapped to `byte[]`. The allowed length is from 1 to 1,000,000,000 bytes. The length is a size constraint; only the actual data is persisted.

To set a `JSON` value with `java.lang.String` in a PreparedStatement use a `FORMAT JSON` data format (`INSERT INTO TEST(ID, DATA) VALUES (?, ? FORMAT JSON)`) or use `setObject(parameter, jsonText, H2Type.JSON)` instead of `setString()`.

Without the data format `VARCHAR` values are converted to `JSON` string values.

SQL/`JSON` null value `JSON 'null'` is distinct from the SQL null value `NULL`.

Order of object members is preserved as is. Duplicate object member names are allowed.

## Example

```sql
JSON
```
