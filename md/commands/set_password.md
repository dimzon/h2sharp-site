# SET PASSWORD

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_password) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET PASSWORD [`string`](../grammar/string.md)
```

🟢 includes non-standard H2 syntax

Changes the password of the current user. The password must be in single quotes. It is case sensitive and can contain spaces.

This command commits an open transaction in this connection.

## Example

```sql
SET PASSWORD 'abcstzri!.5'
```
