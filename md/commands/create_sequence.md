# CREATE SEQUENCE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_sequence) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE SEQUENCE [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`sequenceName`](../grammar/name.md)
[ { AS [`dataType`](../grammar/data_type.md) | [`sequenceOption`](../grammar/sequence_option.md) } [...] ]
```

🟢 includes non-standard H2 syntax

Creates a new sequence. Schema owner rights are required to execute this command.

The data type of a sequence must be a numeric type, the default is `BIGINT`. Sequence can produce only integer values. For `TINYINT` the allowed values are between -128 and 127. For `SMALLINT` the allowed values are between -32768 and 32767. For `INTEGER` the allowed values are between -2147483648 and 2147483647. For `BIGINT` the allowed values are between -9223372036854775808 and 9223372036854775807. For `NUMERIC` and `DECFLOAT` the allowed values depend on precision, but cannot exceed the range of `BIGINT` data type (from -9223372036854775808 to 9223372036854775807); the scale of `NUMERIC` must be 0. For `REAL` the allowed values are between -16777216 and 16777216. For `DOUBLE PRECISION` the allowed values are between -9007199254740992 and 9007199254740992.

Used values are never re-used, even when the transaction is rolled back.

This command commits an open transaction in this connection.

## Example

```sql
CREATE SEQUENCE SEQ_ID;
CREATE SEQUENCE SEQ2 AS INTEGER START WITH 10;
```
