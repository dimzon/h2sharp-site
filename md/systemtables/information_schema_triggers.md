# TRIGGERS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_triggers) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about triggers.

| Column | Type | Description |
| --- | --- | --- |
| TRIGGER_CATALOG | CHARACTER VARYING | The catalog (database name). |
| TRIGGER_SCHEMA | CHARACTER VARYING | The schema of the trigger. |
| TRIGGER_NAME | CHARACTER VARYING | The name of the trigger. |
| EVENT_MANIPULATION | CHARACTER VARYING | 'INSERT', 'UPDATE', 'DELETE', or 'SELECT'. |
| EVENT_OBJECT_CATALOG | CHARACTER VARYING | The catalog (database name). |
| EVENT_OBJECT_SCHEMA | CHARACTER VARYING | The schema of the table. |
| EVENT_OBJECT_TABLE | CHARACTER VARYING | The name of the table. |
| ACTION_ORIENTATION | CHARACTER VARYING | 'ROW' or 'STATEMENT'. |
| ACTION_TIMING | CHARACTER VARYING | 'BEFORE', 'AFTER', or 'INSTEAD OF'. |
| IS_ROLLBACK | BOOLEAN | Whether this trigger is executed on rollback. |
| JAVA_CLASS | CHARACTER VARYING | The Java class name. |
| QUEUE_SIZE | INTEGER | The size of the queue (is not actually used). |
| NO_WAIT | BOOLEAN | Whether trigger is defined with NO WAIT clause (is not actually used). |
| REMARKS | CHARACTER VARYING | Optional remarks. |
