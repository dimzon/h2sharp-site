# TABLE_PRIVILEGES

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_table_privileges) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about privileges of tables.
See INFORMATION_SCHEMA.CHECK_CONSTRAINTS, INFORMATION_SCHEMA.KEY_COLUMN_USAGE,
and INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS for additional information.

| Column | Type | Description |
| --- | --- | --- |
| GRANTOR | CHARACTER VARYING | NULL. |
| GRANTEE | CHARACTER VARYING | The name of grantee. |
| TABLE_CATALOG | CHARACTER VARYING | The catalog (database name). |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
| PRIVILEGE_TYPE | CHARACTER VARYING | 'SELECT', 'INSERT', 'UPDATE', or 'DELETE'. |
| IS_GRANTABLE | CHARACTER VARYING | Whether grantee may grant rights to this object to others ('YES' or 'NO'). |
| WITH_HIERARCHY | CHARACTER VARYING | 'NO'. |
