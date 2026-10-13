# SMALLINT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#smallint_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SMALLINT
```

Possible values: -32768 to 32767.

See also [integer](../grammar/int.md) literal grammar.

In `JDBC` this data type is mapped to `java.lang.Integer`. `java.lang.Short` is also supported.

In `org.h2.api.Aggregate, org.h2.api.AggregateFunction`, and `org.h2.api.Trigger` this data type is mapped to `java.lang.Short`.

## Example

```sql
SMALLINT
```
