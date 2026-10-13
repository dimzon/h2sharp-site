# CREATE USER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_user) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE USER [ IF NOT EXISTS ] [`newUserName`](../grammar/name.md)
{ PASSWORD [`string`](../grammar/string.md) | SALT [`bytes`](../grammar/bytes.md) HASH [`bytes`](../grammar/bytes.md) } [ ADMIN ]
```

🟢 includes non-standard H2 syntax

Creates a new user. For compatibility, only unquoted or uppercase user names are allowed. The password must be in single quotes. It is case sensitive and can contain spaces. The salt and hash values are hex strings.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
CREATE USER GUEST PASSWORD 'abc'
```
