# GRANT ROLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#grant_role) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
GRANT { [`roleName`](../grammar/name.md) [,...] } TO { PUBLIC | [`userName`](../grammar/name.md) | [`roleName`](../grammar/name.md) }
```

Grants a role to a user or role.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
GRANT READONLY TO PUBLIC
```
