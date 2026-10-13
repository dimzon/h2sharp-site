# ROLLBACK

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#rollback) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ROLLBACK [ WORK ] [ TO SAVEPOINT [`savepointName`](../grammar/name.md) ]
```

Rolls back a transaction. If a savepoint name is used, the transaction is only rolled back to the specified savepoint.

## Example

```sql
ROLLBACK
```
