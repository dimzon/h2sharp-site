# REVOKE ALTER ANY SCHEMA

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#revoke_alter_any_schema) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REVOKE ALTER ANY SCHEMA FROM [`userName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Removes schema admin rights from a user.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
GRANT ALTER ANY SCHEMA TO Bob
```
