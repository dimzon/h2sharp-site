# MERGE INTO

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#merge_into) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
MERGE INTO [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) [ ( [`columnName`](../grammar/name.md) [,...] ) ]
[ KEY ( [`columnName`](../grammar/name.md) [,...] ) ]
{ [`insertValues`](../grammar/insert_values.md) | [`query`](../grammar/query.md) }
```

🟢 includes non-standard H2 syntax

Updates existing rows, and insert rows that don't exist. If no key column is specified, the primary key columns are used to find the row. If more than one row per new row is affected, an exception is thrown.

## Example

```sql
MERGE INTO TEST KEY(ID) VALUES(2, 'World')
```
