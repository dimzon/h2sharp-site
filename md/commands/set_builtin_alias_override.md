# SET BUILTIN_ALIAS_OVERRIDE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_builtin_alias_override) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET BUILTIN_ALIAS_OVERRIDE { TRUE | FALSE }
```

🟢 includes non-standard H2 syntax

Allows the overriding of the builtin system date/time functions for unit testing purposes.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
SET BUILTIN_ALIAS_OVERRIDE TRUE
```
