# USERS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_users) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about users.
Only users with ADMIN privileges can see all users, other users can see only themselves.

| Column | Type | Description |
| --- | --- | --- |
| USER_NAME | CHARACTER VARYING | The name of the user. |
| IS_ADMIN | BOOLEAN | Whether user has ADMIN privileges. |
| REMARKS | CHARACTER VARYING | Optional remarks. |
