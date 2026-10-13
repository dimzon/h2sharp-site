# SESSIONS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_sessions) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about sessions.
Only users with ADMIN privileges can see all sessions, other users can see only own session.

| Column | Type | Description |
| --- | --- | --- |
| SESSION_ID | INTEGER | The identifier of the session. |
| USER_NAME | CHARACTER VARYING | The name of the user. |
| SERVER | CHARACTER VARYING | The name of the server used by remote connection. |
| CLIENT_ADDR | CHARACTER VARYING | The client address and port used by remote connection. |
| CLIENT_INFO | CHARACTER VARYING | Additional client information provided by remote connection. |
| SESSION_START | TIMESTAMP(9) WITH TIME ZONE | When this session was started. |
| ISOLATION_LEVEL | CHARACTER VARYING | The isolation level of the session ('READ UNCOMMITTED', 'READ COMMITTED', 'REPEATABLE READ', 'SNAPSHOT', or 'SERIALIZABLE'). |
| EXECUTING_STATEMENT | CHARACTER VARYING | The currently executing statement, if any. |
| EXECUTING_STATEMENT_START | TIMESTAMP(9) WITH TIME ZONE | When the current command was started, if any. |
| CONTAINS_UNCOMMITTED | BOOLEAN | Whether the session contains any uncommitted changes. |
| SESSION_STATE | CHARACTER VARYING | The state of the session ('RUNNING', 'SLEEP', etc.) |
| BLOCKER_ID | INTEGER | The identifier or blocking session, if any. |
| SLEEP_SINCE | TIMESTAMP(9) WITH TIME ZONE | When the last command was finished if session is sleeping. |
