# CHECK_CONSTRAINTS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_check_constraints) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains CHECK clauses of check and domain constraints.

| Column | Type | Description |
| --- | --- | --- |
| CONSTRAINT_CATALOG | CHARACTER VARYING | The catalog (database name). |
| CONSTRAINT_SCHEMA | CHARACTER VARYING | The schema of the constraint. |
| CONSTRAINT_NAME | CHARACTER VARYING | The name of the constraint. |
| CHECK_CLAUSE | CHARACTER VARYING | The SQL of CHECK clause. |
