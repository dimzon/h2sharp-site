# SET REFERENTIAL_INTEGRITY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_referential_integrity) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET REFERENTIAL_INTEGRITY { TRUE | FALSE }
```

🟢 includes non-standard H2 syntax

Disabled or enables referential integrity checking for the whole database. Enabling it does not check existing data. Use `ALTER TABLE SET` to disable it only for one table.

This setting is not persistent. This command commits an open transaction in this connection. Admin rights are required to execute this command, as it affects all connections.

## Example

```sql
SET REFERENTIAL_INTEGRITY FALSE
```
