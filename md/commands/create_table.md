# CREATE TABLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_table) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE [ CACHED | MEMORY ] [ { TEMP } | [ GLOBAL | LOCAL ] TEMPORARY ]
TABLE [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md)
[ ( { [`columnName`](../grammar/name.md) [[`columnDefinition`](../grammar/column_definition.md)] | [`tableConstraintDefinition`](../grammar/table_constraint_definition.md) } [,...] ) ]
[ ENGINE [`tableEngineName`](../grammar/name.md) ]
[ WITH [`tableEngineParamName`](../grammar/name.md) [,...] ]
[ NOT PERSISTENT ] [ TRANSACTIONAL ]
[ AS ( [`query`](../grammar/query.md) ) [ WITH [ NO ] DATA ] ]
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Creates a new table.

Admin rights are required to execute this command if and only if `ENGINE` option is used or custom default table engine is configured in the database. Schema owner rights or `ALTER ANY SCHEMA` rights are required for creation of regular tables and `GLOBAL TEMPORARY` tables.

Cached tables (the default for regular tables) are persistent, and the number of rows is not limited by the main memory. Memory tables (the default for temporary tables) are persistent, but the index data is kept in main memory, that means memory tables should not get too large.

Temporary tables are deleted when closing or opening a database. Temporary tables can be global (accessible by all connections) or local (only accessible by the current connection). The default for temporary tables is global. Indexes of temporary tables are kept fully in main memory, unless the temporary table is created using `CREATE CACHED TABLE`.

The `ENGINE` option is only required when custom table implementations are used. The table engine class must implement the interface `org.h2.api.TableEngine`. Any table engine parameters are passed down in the tableEngineParams field of the CreateTableData object.

Either `ENGINE`, or `WITH` (table engine params), or both may be specified. If `ENGINE` is not specified in `CREATE TABLE`, then the engine specified by `DEFAULT_TABLE_ENGINE` option of database params is used.

Tables with the `NOT PERSISTENT` modifier are kept fully in memory, and all rows are lost when the database is closed.

The column definitions are optional if a query is specified. In that case the column list of the query is used. If the query is specified its results are inserted into created table unless `WITH NO DATA` is specified.

This command commits an open transaction, except when using `TRANSACTIONAL` (only supported for temporary tables).

## Example

```sql
CREATE TABLE TEST(ID INT PRIMARY KEY, NAME VARCHAR(255))
```
