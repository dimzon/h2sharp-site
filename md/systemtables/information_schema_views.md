# VIEWS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_views) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains additional information about views.
See INFORMATION_SCHEMA.TABLES for basic information.

| Column | Type | Description |
| --- | --- | --- |
| TABLE_CATALOG | CHARACTER VARYING | The catalog (database name). |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
| VIEW_DEFINITION | CHARACTER VARYING | The query SQL, if applicable. |
| CHECK_OPTION | CHARACTER VARYING | 'NONE'. |
| IS_UPDATABLE | CHARACTER VARYING | 'NO'. |
| INSERTABLE_INTO | CHARACTER VARYING | 'NO'. |
| IS_TRIGGER_UPDATABLE | CHARACTER VARYING | Whether the view has INSTEAD OF trigger for UPDATE ('YES' or 'NO'). |
| IS_TRIGGER_DELETABLE | CHARACTER VARYING | Whether the view has INSTEAD OF trigger for DELETE ('YES' or 'NO'). |
| IS_TRIGGER_INSERTABLE_INTO | CHARACTER VARYING | Whether the view has INSTEAD OF trigger for INSERT ('YES' or 'NO'). |
| STATUS | CHARACTER VARYING | 'VALID' or 'INVALID'. |
| REMARKS | CHARACTER VARYING | Optional remarks. |
