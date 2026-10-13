# TABLES

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_tables) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about tables.
See also INFORMATION_SCHEMA.COLUMNS.

| Column | Type | Description |
| --- | --- | --- |
| TABLE_CATALOG | CHARACTER VARYING | The catalog (database name). |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
| TABLE_TYPE | CHARACTER VARYING | 'BASE TABLE', 'VIEW', 'GLOBAL TEMPORARY', or 'LOCAL TEMPORARY'. |
| IS_INSERTABLE_INTO | CHARACTER VARYING | Whether the table is insertable ('YES' or 'NO'). |
| COMMIT_ACTION | CHARACTER VARYING | 'DELETE', 'DROP', or 'PRESERVE' for temporary tables. |
| STORAGE_TYPE | CHARACTER VARYING | 'CACHED' for regular persisted tables, 'MEMORY' for in-memory tables or persisted tables with in-memory indexes, 'GLOBAL TEMPORARY' or 'LOCAL TEMPORARY' for temporary tables, 'EXTERNAL' for tables with external table engines, or 'TABLE LINK' for linked tables. |
| REMARKS | CHARACTER VARYING | Optional remarks. |
| LAST_MODIFICATION | BIGINT | The sequence number of the last modification, if applicable. |
| TABLE_CLASS | CHARACTER VARYING | The Java class name of implementation. |
| ROW_COUNT_ESTIMATE | BIGINT | The approximate number of rows if known or some default value if unknown. For regular tables contains the total number of rows including the uncommitted rows. |
