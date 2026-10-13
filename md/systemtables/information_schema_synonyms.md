# SYNONYMS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_synonyms) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about table synonyms.

| Column | Type | Description |
| --- | --- | --- |
| SYNONYM_CATALOG | CHARACTER VARYING | The catalog (database name). |
| SYNONYM_SCHEMA | CHARACTER VARYING | The schema of the synonym. |
| SYNONYM_NAME | CHARACTER VARYING | The name of the synonym. |
| SYNONYM_FOR | CHARACTER VARYING | The name of the referenced table. |
| SYNONYM_FOR_SCHEMA | CHARACTER VARYING | The name of the referenced schema. |
| TYPE_NAME | CHARACTER VARYING | 'SYNONYM'. |
| STATUS | CHARACTER VARYING | 'VALID'. |
| REMARKS | CHARACTER VARYING | Optional remarks. |
