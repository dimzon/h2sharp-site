# SEQUENCES

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_sequences) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about sequences.

| Column | Type | Description |
| --- | --- | --- |
| SEQUENCE_CATALOG | CHARACTER VARYING | The catalog (database name). |
| SEQUENCE_SCHEMA | CHARACTER VARYING | The schema of the sequence. |
| SEQUENCE_NAME | CHARACTER VARYING | The name of the sequence. |
| DATA_TYPE | CHARACTER VARYING | The SQL data type name. |
| NUMERIC_PRECISION | INTEGER | The precision for numeric data types. |
| NUMERIC_PRECISION_RADIX | INTEGER | The radix of precision (2 or 10) for numeric data types. |
| NUMERIC_SCALE | INTEGER | The scale for numeric data types. |
| START_VALUE | BIGINT | The initial start value. |
| MINIMUM_VALUE | BIGINT | The minimum value. |
| MAXIMUM_VALUE | BIGINT | The maximum value. |
| INCREMENT | BIGINT | The increment value. |
| CYCLE_OPTION | CHARACTER VARYING | Whether values are cycled ('YES' or 'NO'). |
| DECLARED_DATA_TYPE | CHARACTER VARYING | The declared SQL data type name for numeric data types. |
| DECLARED_NUMERIC_PRECISION | INTEGER | The declared precision, if any, for numeric data types. |
| DECLARED_NUMERIC_SCALE | INTEGER | The declared scale, if any, for numeric data types. |
| BASE_VALUE | BIGINT | The current base value. |
| CACHE | BIGINT | The cache size. |
| REMARKS | CHARACTER VARYING | Optional remarks. |
