# ALTER SEQUENCE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_sequence) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER SEQUENCE [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`sequenceName`](../grammar/name.md) [`alterSequenceOption`](../grammar/alter_sequence_option.md) [...]
```

🟢 includes non-standard H2 syntax

Changes the parameters of a sequence. Schema owner rights are required to execute this command. This command does not commit the current transaction; however the new value is used by other transactions immediately, and rolling back this command has no effect.

## Example

```sql
ALTER SEQUENCE SEQ_ID RESTART WITH 1000
```
