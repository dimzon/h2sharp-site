# LOCKS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_locks) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about tables locked by sessions.

| Column | Type | Description |
| --- | --- | --- |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
| SESSION_ID | INTEGER | The identifier of the session. |
| LOCK_TYPE | CHARACTER VARYING | 'READ' or 'WRITE'. |
