# SET IGNORECASE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_ignorecase) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET IGNORECASE { TRUE | FALSE }
```

🟢 includes non-standard H2 syntax

If `IGNORECASE` is enabled, text columns in newly created tables will be case-insensitive. Already existing tables are not affected. The effect of case-insensitive columns is similar to using a collation with strength `PRIMARY`. Case-insensitive columns are compared faster than when using a collation. String literals and parameters are however still considered case sensitive even if this option is set.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. This setting can be appended to the database URL: `jdbc:h2:./test;IGNORECASE=TRUE`

## Example

```sql
SET IGNORECASE TRUE
```
