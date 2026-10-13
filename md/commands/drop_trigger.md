# DROP TRIGGER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_trigger) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP TRIGGER [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`triggerName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Drops an existing trigger. This command commits an open transaction in this connection.

## Example

```sql
DROP TRIGGER TRIG_INS
```
