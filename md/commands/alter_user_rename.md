# ALTER USER RENAME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_user_rename) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER USER [`userName`](../grammar/name.md) RENAME TO [`newUserName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Renames a user. After renaming a user, the password becomes invalid and needs to be changed as well.

Only unquoted or uppercase user names are allowed. Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
ALTER USER TOM RENAME TO THOMAS
```
