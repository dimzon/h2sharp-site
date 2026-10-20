# Range Table

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#range_table) · © H2 Group (MPL-2.0 / EPL-1.0)

The range table is a dynamic system table that contains all values from a start to an end value.
Non-zero step value may be also specified, default is 1.
Start value, end value, and optional step value are converted to BIGINT data type.
The table contains one column called X.
If start value is greater than end value and step is positive the result is empty.
If start value is less than end value and step is negative the result is empty too.
If start value is equal to end value the result contains only start value.
Start value, start value plus step, start value plus step multiplied by two and so on are included in result.
If step is positive the last value is less than or equal to the specified end value.
If step in negative the last value is greater than or equal to the specified end value.
The table is used as follows:

Examples:

SELECT X FROM SYSTEM_RANGE(1, 10);
-- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
SELECT X FROM SYSTEM_RANGE(1, 10, 2);
-- 1, 3, 5, 7, 9
SELECT X FROM SYSTEM_RANGE(1, 10, -1);
-- No rows
SELECT X FROM SYSTEM_RANGE(10, 2, -2);
-- 10, 8, 6, 4, 2
