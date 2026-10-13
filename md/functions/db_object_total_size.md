# DB_OBJECT_TOTAL_SIZE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#db_object_total_size) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DB_OBJECT_TOTAL_SIZE('TABLE', [`schemaNameString`](../grammar/string.md), [`objectNameString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Returns the approximate amount of space used by the specified table and all its indexes. Only size of version used by the current transaction is estimated. Size of large `LOBs` currently is not included into estimation. This function may be expensive since it has to load every page in the table and its indexes. Use [DB_OBJECT_APPROXIMATE_TOTAL_SIZE](db_object_approximate_total_size.md) for a faster coarse approximation.

## Example

```sql
CALL DB_OBJECT_TOTAL_SIZE('TABLE', 'PUBLIC', 'MY_TABLE');
```
