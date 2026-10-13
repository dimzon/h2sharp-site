# PREPARE COMMIT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#prepare_commit) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
PREPARE COMMIT [`newTransactionName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Prepares committing a transaction. This command is part of the 2-phase-commit protocol.

## Example

```sql
PREPARE COMMIT XID_TEST
```
