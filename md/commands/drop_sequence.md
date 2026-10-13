# DROP SEQUENCE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_sequence) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP SEQUENCE [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`sequenceName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Drops a sequence. Schema owner rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
DROP SEQUENCE SEQ_ID
```
