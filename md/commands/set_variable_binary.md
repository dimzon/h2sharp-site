# SET VARIABLE_BINARY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_variable_binary) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET VARIABLE_BINARY { TRUE | FALSE }
```

🟢 includes non-standard H2 syntax

If `TRUE` is specified, the `BINARY` data type will be parsed as `VARBINARY` in the current session. It can be used for compatibility with older versions of H2.

This setting can be appended to the database URL: `jdbc:h2:./test;VARIABLE_BINARY=TRUE`

## Example

```sql
SET VARIABLE_BINARY TRUE
```
