# DROP USER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_user) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP USER [ IF EXISTS ] [`userName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Drops a user. The current user cannot be dropped. For compatibility, only unquoted or uppercase user names are allowed.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
DROP USER TOM
```
