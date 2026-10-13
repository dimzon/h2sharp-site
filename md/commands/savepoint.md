# SAVEPOINT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#savepoint) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SAVEPOINT [`savepointName`](../grammar/name.md)
```

Create a new savepoint. See also `ROLLBACK`. Savepoints are only valid until the transaction is committed or rolled back.

## Example

```sql
SAVEPOINT HALF_DONE
```
