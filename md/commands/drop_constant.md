# DROP CONSTANT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_constant) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP CONSTANT [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`constantName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Drops a constant. Schema owner rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
DROP CONSTANT ONE
```
