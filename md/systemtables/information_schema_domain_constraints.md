# DOMAIN_CONSTRAINTS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_domain_constraints) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains basic information about domain constraints.
See also INFORMATION_SCHEMA.CHECK_CONSTRAINTS.

| Column | Type | Description |
| --- | --- | --- |
| CONSTRAINT_CATALOG | CHARACTER VARYING | The catalog (database name). |
| CONSTRAINT_SCHEMA | CHARACTER VARYING | The schema of the constraint. |
| CONSTRAINT_NAME | CHARACTER VARYING | The name of the constraint. |
| DOMAIN_CATALOG | CHARACTER VARYING | The catalog (database name). |
| DOMAIN_SCHEMA | CHARACTER VARYING | The schema of domain. |
| DOMAIN_NAME | CHARACTER VARYING | The name of domain. |
| IS_DEFERRABLE | CHARACTER VARYING | 'NO'. |
| INITIALLY_DEFERRED | CHARACTER VARYING | 'NO'. |
| REMARKS | CHARACTER VARYING | Optional remarks. |
