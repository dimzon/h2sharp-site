# CREATE AGGREGATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_aggregate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE AGGREGATE [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`aggregateName`](../grammar/name.md) FOR [`classNameString`](../grammar/string.md)
```

🟢 includes non-standard H2 syntax

Creates a new user-defined aggregate function. The method name must be the full qualified class name. The class must implement the interface `org.h2.api.Aggregate` or `org.h2.api.AggregateFunction`.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
CREATE AGGREGATE SIMPLE_MEDIAN FOR 'com.acme.db.Median'
```
