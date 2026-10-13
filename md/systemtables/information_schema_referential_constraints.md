# REFERENTIAL_CONSTRAINTS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_referential_constraints) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains additional information about referential constraints.

| Column | Type | Description |
| --- | --- | --- |
| CONSTRAINT_CATALOG | CHARACTER VARYING | The catalog (database name). |
| CONSTRAINT_SCHEMA | CHARACTER VARYING | The schema of the constraint. |
| CONSTRAINT_NAME | CHARACTER VARYING | The name of the constraint. |
| UNIQUE_CONSTRAINT_CATALOG | CHARACTER VARYING | The catalog (database name). |
| UNIQUE_CONSTRAINT_SCHEMA | CHARACTER VARYING | The schema of referenced unique constraint. |
| UNIQUE_CONSTRAINT_NAME | CHARACTER VARYING | The name of referenced unique constraint. |
| MATCH_OPTION | CHARACTER VARYING | 'NONE'. |
| UPDATE_RULE | CHARACTER VARYING | The rule for UPDATE in referenced table ('RESTRICT', 'CASCADE', 'SET DEFAULT', or 'SET NULL'). |
| DELETE_RULE | CHARACTER VARYING | The rule for DELETE in referenced table ('RESTRICT', 'CASCADE', 'SET DEFAULT', or 'SET NULL'). |
