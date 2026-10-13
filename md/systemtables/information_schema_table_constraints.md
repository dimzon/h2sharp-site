# TABLE_CONSTRAINTS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_table_constraints) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains basic information about table constraints (check, primary key, unique, and referential).

| Column | Type | Description |
| --- | --- | --- |
| CONSTRAINT_CATALOG | CHARACTER VARYING | The catalog (database name). |
| CONSTRAINT_SCHEMA | CHARACTER VARYING | The schema of the constraint. |
| CONSTRAINT_NAME | CHARACTER VARYING | The name of the constraint. |
| CONSTRAINT_TYPE | CHARACTER VARYING | 'CHECK', 'PRIMARY KEY', 'UNIQUE', or 'REFERENTIAL'. |
| TABLE_CATALOG | CHARACTER VARYING | The catalog (database name). |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
| IS_DEFERRABLE | CHARACTER VARYING | 'NO'. |
| INITIALLY_DEFERRED | CHARACTER VARYING | 'NO'. |
| ENFORCED | CHARACTER VARYING | 'YES' for non-referential constants. 'YES' for referential constants when checks for referential integrity are enabled for the both referenced and referencing tables and 'NO' when they are disabled. |
| NULLS_DISTINCT | CHARACTER VARYING | 'YES' for unique constraints with distinct null values, 'NO' for unique constraints with not distinct null values, 'ALL' for multi-column unique constraints where only rows with null values in all unique columns are distinct, NULL for other types of constraints. |
| INDEX_CATALOG | CHARACTER VARYING | The catalog (database name). |
| INDEX_SCHEMA | CHARACTER VARYING | The schema of the index. |
| INDEX_NAME | CHARACTER VARYING | The name of the index. |
| REMARKS | CHARACTER VARYING | Optional remarks. |
