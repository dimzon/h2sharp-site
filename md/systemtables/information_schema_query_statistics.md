# QUERY_STATISTICS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_query_statistics) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains statistics of queries when query statistics gathering is enabled.

| Column | Type | Description |
| --- | --- | --- |
| SQL_STATEMENT | CHARACTER VARYING | The SQL statement. |
| EXECUTION_COUNT | INTEGER | The execution count. |
| MIN_EXECUTION_TIME | DOUBLE PRECISION | The minimum execution time in milliseconds. |
| MAX_EXECUTION_TIME | DOUBLE PRECISION | The maximum execution time in milliseconds. |
| CUMULATIVE_EXECUTION_TIME | DOUBLE PRECISION | The total execution time in milliseconds. |
| AVERAGE_EXECUTION_TIME | DOUBLE PRECISION | The average execution time in milliseconds. |
| STD_DEV_EXECUTION_TIME | DOUBLE PRECISION | The standard deviation of execution time in milliseconds. |
| MIN_ROW_COUNT | BIGINT | The minimum number of rows. |
| MAX_ROW_COUNT | BIGINT | The maximum number of rows. |
| CUMULATIVE_ROW_COUNT | BIGINT | The total number of rows. |
| AVERAGE_ROW_COUNT | DOUBLE PRECISION | The average number of rows. |
| STD_DEV_ROW_COUNT | DOUBLE PRECISION | The standard deviation of number of rows. |
