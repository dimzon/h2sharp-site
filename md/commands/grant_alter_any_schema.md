# GRANT ALTER ANY SCHEMA

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#grant_alter_any_schema) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
GRANT ALTER ANY SCHEMA TO [`userName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Grant schema admin rights to a user.

Schema admin can create, rename, or drop schemas and also has schema owner rights in every schema.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
GRANT ALTER ANY SCHEMA TO Bob
```
