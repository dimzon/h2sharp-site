# GRANT RIGHT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#grant_right) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
GRANT { { SELECT | INSERT | UPDATE | DELETE } [,..] | ALL [ PRIVILEGES ] } ON
{ { SCHEMA [`schemaName`](../grammar/name.md) } | { [ TABLE ] [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) [,...] } }
TO { PUBLIC | [`userName`](../grammar/name.md) | [`roleName`](../grammar/name.md) }
```

🟢 includes non-standard H2 syntax

Grants rights for a table to a user or role.

Schema owner rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
GRANT SELECT ON TEST TO READONLY
```
