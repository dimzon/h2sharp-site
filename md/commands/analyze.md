# ANALYZE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#analyze) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ANALYZE [ TABLE [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) ] [ SAMPLE_SIZE [`rowCountInt`](../grammar/int.md) ]
```

🟢 includes non-standard H2 syntax

Updates the selectivity statistics of tables. If no table name is given, all tables are analyzed. The selectivity is used by the cost based optimizer to select the best index for a given query. If no sample size is set, up to 10000 rows per table are read. The value 0 means all rows are read. The selectivity can be set manually using `ALTER TABLE ALTER COLUMN SELECTIVITY`. Manual values are overwritten by this statement. The selectivity is available in the `INFORMATION_SCHEMA.COLUMNS` table.

This command commits an open transaction in this connection.

## Example

```sql
ANALYZE SAMPLE_SIZE 1000
```
