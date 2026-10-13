# PARAMETERS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_parameters) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about parameters of routines.

| Column | Type | Description |
| --- | --- | --- |
| SPECIFIC_CATALOG | CHARACTER VARYING | The catalog (database name). |
| SPECIFIC_SCHEMA | CHARACTER VARYING | The schema of the overloaded version of routine. |
| SPECIFIC_NAME | CHARACTER VARYING | The name of the overloaded version of routine. |
| ORDINAL_POSITION | INTEGER | The ordinal position (1-based). |
| PARAMETER_MODE | CHARACTER VARYING | 'IN'. |
| IS_RESULT | CHARACTER VARYING | 'NO'. |
| AS_LOCATOR | CHARACTER VARYING | 'YES' for LOBs, 'NO' for others. |
| PARAMETER_NAME | CHARACTER VARYING | The name of the parameter. |
| DATA_TYPE | CHARACTER VARYING | The SQL data type name. |
| CHARACTER_MAXIMUM_LENGTH | BIGINT | The maximum length in characters for character string data types. For binary string data types contains the same value as CHARACTER_OCTET_LENGTH. |
| CHARACTER_OCTET_LENGTH | BIGINT | The maximum length in bytes for binary string data types. For character string data types contains the same value as CHARACTER_MAXIMUM_LENGTH. |
| CHARACTER_SET_CATALOG | CHARACTER VARYING | The catalog (database name) for character string data types. |
| CHARACTER_SET_SCHEMA | CHARACTER VARYING | The name of public schema for character string data types. |
| CHARACTER_SET_NAME | CHARACTER VARYING | The 'Unicode' for character string data types. |
| COLLATION_CATALOG | CHARACTER VARYING | The catalog (database name) for character string data types. |
| COLLATION_SCHEMA | CHARACTER VARYING | The name of public schema for character string data types. |
| COLLATION_NAME | CHARACTER VARYING | The name of collation for character string data types. |
| NUMERIC_PRECISION | INTEGER | The precision for numeric data types. |
| NUMERIC_PRECISION_RADIX | INTEGER | The radix of precision (2 or 10) for numeric data types. |
| NUMERIC_SCALE | INTEGER | The scale for numeric data types. |
| DATETIME_PRECISION | INTEGER | The fractional seconds precision for datetime data types. |
| INTERVAL_TYPE | CHARACTER VARYING | The data type of interval qualifier for interval data types. |
| INTERVAL_PRECISION | INTEGER | The leading field precision for interval data types. |
| MAXIMUM_CARDINALITY | INTEGER | The maximum cardinality for array data types. |
| DTD_IDENTIFIER | CHARACTER VARYING | The data type identifier to read additional information from INFORMATION_SCHEMA.ELEMENT_TYPES for array data types, INFORMATION_SCHEMA.ENUM_VALUES for ENUM data type, and INFORMATION_SCHEMA.FIELDS for row value data types. |
| DECLARED_DATA_TYPE | CHARACTER VARYING | The declared SQL data type name for numeric data types. |
| DECLARED_NUMERIC_PRECISION | INTEGER | The declared precision, if any, for numeric data types. |
| DECLARED_NUMERIC_SCALE | INTEGER | The declared scale, if any, for numeric data types. |
| PARAMETER_DEFAULT | CHARACTER VARYING | NULL. |
| GEOMETRY_TYPE | CHARACTER VARYING | The geometry type constraint, if any, for geometry data types. |
| GEOMETRY_SRID | INTEGER | The geometry SRID (Spatial Reference Identifier) constraint, if any, for geometry data types. |
