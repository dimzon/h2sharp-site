# SET MODE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_mode) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET MODE { REGULAR | STRICT | LEGACY | DB2 | DERBY | HSQLDB | MSSQLSERVER | MYSQL | ORACLE | POSTGRESQL }
```

🟢 includes non-standard H2 syntax

Changes to another database compatibility mode. For details, see [Compatibility Modes](https://www.h2database.com/html/features.html#compatibility_modes).

This setting is not persistent. Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting can be appended to the database URL: `jdbc:h2:./test;MODE=MYSQL`

## Example

```sql
SET MODE HSQLDB
```
