# DROP AGGREGATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_aggregate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP AGGREGATE [ IF EXISTS ] [`aggregateName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Drops an existing user-defined aggregate function. Schema owner rights are required to execute this command.

This command commits an open transaction in this connection.

## Example

```sql
DROP AGGREGATE SIMPLE_MEDIAN
```
