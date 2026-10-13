# SET ALLOW_LITERALS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_allow_literals) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET ALLOW_LITERALS { NONE | ALL | NUMBERS }
```

🟢 includes non-standard H2 syntax

This setting can help solve the SQL injection problem. By default, text and number literals are allowed in SQL statements. However, this enables SQL injection if the application dynamically builds SQL statements. SQL injection is not possible if user data is set using parameters ('?').

`NONE` means literals of any kind are not allowed, only parameters and constants are allowed. `NUMBERS` mean only numerical and boolean literals are allowed. `ALL` means all literals are allowed (default).

See also `CREATE CONSTANT`.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. This setting can be appended to the database URL: `jdbc:h2:./test;ALLOW_LITERALS=NONE`

## Example

```sql
SET ALLOW_LITERALS NONE
```
