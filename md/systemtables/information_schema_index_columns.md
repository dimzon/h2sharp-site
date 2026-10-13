# INDEX_COLUMNS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_index_columns) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about columns used in indexes.

| Column | Type | Description |
| --- | --- | --- |
| INDEX_CATALOG | CHARACTER VARYING | The catalog (database name). |
| INDEX_SCHEMA | CHARACTER VARYING | The schema of the index. |
| INDEX_NAME | CHARACTER VARYING | The name of the index. |
| TABLE_CATALOG | CHARACTER VARYING | The catalog (database name). |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
| COLUMN_NAME | CHARACTER VARYING | The name of the column. |
| ORDINAL_POSITION | INTEGER | The ordinal position (1-based). |
| ORDERING_SPECIFICATION | CHARACTER VARYING | 'ASC' or 'DESC'. |
| NULL_ORDERING | CHARACTER VARYING | 'FIRST', 'LAST', or NULL. |
| IS_UNIQUE | BOOLEAN | Whether this column is a part of unique column list of a unique index (TRUE or FALSE). |
