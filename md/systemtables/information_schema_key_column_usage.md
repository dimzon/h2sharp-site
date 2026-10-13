# KEY_COLUMN_USAGE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_key_column_usage) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about columns used by primary key, unique, or referential constraint.

| Column | Type | Description |
| --- | --- | --- |
| CONSTRAINT_CATALOG | CHARACTER VARYING | The catalog (database name). |
| CONSTRAINT_SCHEMA | CHARACTER VARYING | The schema of the constraint. |
| CONSTRAINT_NAME | CHARACTER VARYING | The name of the constraint. |
| TABLE_CATALOG | CHARACTER VARYING | The catalog (database name). |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
| COLUMN_NAME | CHARACTER VARYING | The name of the column. |
| ORDINAL_POSITION | INTEGER | The ordinal position (1-based). |
| POSITION_IN_UNIQUE_CONSTRAINT | INTEGER | The ordinal position in the referenced unique constraint (1-based). |
