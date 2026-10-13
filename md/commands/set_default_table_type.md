# SET DEFAULT_TABLE_TYPE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_default_table_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET DEFAULT_TABLE_TYPE { MEMORY | CACHED }
```

🟢 includes non-standard H2 syntax

Sets the default table storage type that is used when creating new tables. Memory tables are kept fully in the main memory (including indexes), however the data is still stored in the database file. The size of memory tables is limited by the memory. The default is `CACHED`.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. It has no effect for in-memory databases.

## Example

```sql
SET DEFAULT_TABLE_TYPE MEMORY
```
