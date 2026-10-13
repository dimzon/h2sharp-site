# COMMIT TRANSACTION

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#commit_transaction) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
COMMIT TRANSACTION [`transactionName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Sets the resolution of an in-doubt transaction to 'commit'.

Admin rights are required to execute this command. This command is part of the 2-phase-commit protocol.

## Example

```sql
COMMIT TRANSACTION XID_TEST
```
