# ALTER USER ADMIN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_user_admin) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER USER [`userName`](../grammar/name.md) ADMIN { TRUE | FALSE }
```

🟢 includes non-standard H2 syntax

Switches the admin flag of a user on or off.

Only unquoted or uppercase user names are allowed. Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
ALTER USER TOM ADMIN TRUE
```
