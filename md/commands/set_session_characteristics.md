# SET SESSION CHARACTERISTICS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_session_characteristics) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL
{ READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE }
```

Changes the transaction isolation level of the current session. The actual support of isolation levels depends on the database engine.

This command commits an open transaction in this session.

## Example

```sql
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL SERIALIZABLE
```
