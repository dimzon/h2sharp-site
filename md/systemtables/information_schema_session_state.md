# SESSION_STATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_session_state) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains the state of the current session.

| Column | Type | Description |
| --- | --- | --- |
| STATE_KEY | CHARACTER VARYING | The key. |
| STATE_COMMAND | CHARACTER VARYING | The SQL command that can be used to restore the state. |
