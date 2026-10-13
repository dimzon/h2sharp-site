# RIGHTS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_rights) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about granted rights and roles.

| Column | Type | Description |
| --- | --- | --- |
| GRANTEE | CHARACTER VARYING | The name of grantee. |
| GRANTEETYPE | CHARACTER VARYING | 'USER' if grantee is a user, 'ROLE' if grantee is a role. |
| GRANTEDROLE | CHARACTER VARYING | The name of the granted role for role grants. |
| RIGHTS | CHARACTER VARYING | The set of rights ('SELECT', 'DELETE', 'INSERT', 'UPDATE', or 'ALTER ANY SCHEMA' separated with ', ') for table grants. |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
