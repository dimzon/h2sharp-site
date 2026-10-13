# ALTER USER SET PASSWORD

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_user_set_password) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER USER [`userName`](../grammar/name.md) SET { PASSWORD [`string`](../grammar/string.md) | SALT [`bytes`](../grammar/bytes.md) HASH [`bytes`](../grammar/bytes.md) }
```

🟢 includes non-standard H2 syntax

Changes the password of a user. Only unquoted or uppercase user names are allowed. The password must be enclosed in single quotes. It is case sensitive and can contain spaces. The salt and hash values are hex strings.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
ALTER USER SA SET PASSWORD 'rioyxlgt'
```
