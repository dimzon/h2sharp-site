# DB_OBJECT_APPROXIMATE_SIZE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#db_object_approximate_size) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DB_OBJECT_APPROXIMATE_SIZE({'INDEX'|'TABLE'}, [`schemaNameString`](../grammar/string.md), [`objectNameString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Returns the coarse approximate amount of space used by the specified table (excluding its indexes) or index. Only size of version used by the current transaction is estimated. Size of large `LOBs` currently is not included into estimation.

## Example

```sql
CALL DB_OBJECT_APPROXIMATE_SIZE('TABLE', 'PUBLIC', 'MY_TABLE');
```
