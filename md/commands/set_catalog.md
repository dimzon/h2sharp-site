# SET CATALOG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_catalog) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET CATALOG { [`catalogString`](../grammar/string.md) | { [`catalogName`](../grammar/name.md) } }
```

🟢 includes non-standard H2 syntax

This command has no effect if the specified name matches the name of the database, otherwise it throws an exception.

This command does not commit a transaction.

## Example

```sql
SET CATALOG 'DB'
SET CATALOG DB_NAME
```
