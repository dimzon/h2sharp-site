# CREATE ROLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_role) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE ROLE [ IF NOT EXISTS ] [`newRoleName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Creates a new role. This command commits an open transaction in this connection.

## Example

```sql
CREATE ROLE READONLY
```
