# TINYINT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#tinyint_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TINYINT
```

🟢 includes non-standard H2 syntax

Possible values are: -128 to 127.

See also [integer](../grammar/int.md) literal grammar.

In `JDBC` this data type is mapped to `java.lang.Integer`. `java.lang.Byte` is also supported.

In `org.h2.api.Aggregate, org.h2.api.AggregateFunction`, and `org.h2.api.Trigger` this data type is mapped to `java.lang.Byte`.

## Example

```sql
TINYINT
```
