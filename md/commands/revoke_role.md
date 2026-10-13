# REVOKE ROLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#revoke_role) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REVOKE { [`roleName`](../grammar/name.md) [,...] } FROM { PUBLIC | [`userName`](../grammar/name.md) | [`roleName`](../grammar/name.md) }
```

Removes a role from a user or role.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
REVOKE READONLY FROM TOM
```
