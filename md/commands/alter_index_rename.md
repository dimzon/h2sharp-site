# ALTER INDEX RENAME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_index_rename) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER INDEX [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`indexName`](../grammar/name.md) RENAME TO [`newIndexName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Renames an index. This command commits an open transaction in this connection.

## Example

```sql
ALTER INDEX IDXNAME RENAME TO IDX_TEST_NAME
```
