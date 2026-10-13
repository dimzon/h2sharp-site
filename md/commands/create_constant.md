# CREATE CONSTANT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_constant) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE CONSTANT [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`constantName`](../grammar/name.md)
VALUE [`expression`](../grammar/expression.md)
```

🟢 includes non-standard H2 syntax

Creates a new constant. Schema owner rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
CREATE CONSTANT ONE VALUE 1
```
