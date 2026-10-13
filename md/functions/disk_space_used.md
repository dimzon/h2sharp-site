# DISK_SPACE_USED

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#disk_space_used) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DISK_SPACE_USED([`tableNameString`](../grammar/string.md))
```

🔴 compatibility-only syntax

Returns the approximate amount of space used by the table specified. Only size of version used by the current transaction is estimated. Does not currently take into account indexes or `LOB`'s. This function may be expensive since it has to load every page in the table. This function is deprecated, use [DB_OBJECT_SIZE](db_object_size.md) instead of it.

## Example

```sql
CALL DISK_SPACE_USED('my_table');
```
