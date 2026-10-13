# DROP ROLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_role) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP ROLE [ IF EXISTS ] [`roleName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Drops a role. Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
DROP ROLE READONLY
```
