# SET SALT HASH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_salt_hash) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET SALT [`bytes`](../grammar/bytes.md) HASH [`bytes`](../grammar/bytes.md)
```

🟢 includes non-standard H2 syntax

Sets the password salt and hash for the current user. The password must be in single quotes. It is case sensitive and can contain spaces.

This command commits an open transaction in this connection.

## Example

```sql
SET SALT '00' HASH '1122'
```
