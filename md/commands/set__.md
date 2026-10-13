# SET @

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set__) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET [`@variableName`](../grammar/name.md) [ = ] [`expression`](../grammar/expression.md)
```

🟢 includes non-standard H2 syntax

Updates a user-defined variable. Variables are not persisted and session scoped, that means only visible from within the session in which they are defined. This command does not commit a transaction, and rollback does not affect it.

## Example

```sql
SET @TOTAL=0
```
