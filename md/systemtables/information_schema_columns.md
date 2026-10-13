# COLUMNS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_columns) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about columns of tables.

| Column | Type | Description |
| --- | --- | --- |
| TABLE_CATALOG | CHARACTER VARYING | The catalog (database name). |
| TABLE_SCHEMA | CHARACTER VARYING | The schema of the table. |
| TABLE_NAME | CHARACTER VARYING | The name of the table. |
| COLUMN_NAME | CHARACTER VARYING | The name of the column. |
| ORDINAL_POSITION | INTEGER | The ordinal position (1-based). |
| COLUMN_DEFAULT | CHARACTER VARYING | The SQL of DEFAULT expression, if any. |
| IS_NULLABLE | CHARACTER VARYING | Whether column may contain NULL value ('YES' or 'NO'). |
| DATA_TYPE | CHARACTER VARYING | The SQL data type name. |
| CHARACTER_MAXIMUM_LENGTH | BIGINT | The maximum length in characters for character string data types. For binary string data types contains the same value as CHARACTER_OCTET_LENGTH. |
| CHARACTER_OCTET_LENGTH | BIGINT | The maximum length in bytes for binary string data types. For character string data types contains the same value as CHARACTER_MAXIMUM_LENGTH. |
| NUMERIC_PRECISION | INTEGER | The precision for numeric data types. |
| NUMERIC_PRECISION_RADIX | INTEGER | The radix of precision (2 or 10) for numeric data types. |
| NUMERIC_SCALE | INTEGER | The scale for numeric data types. |
| DATETIME_PRECISION | INTEGER | The fractional seconds precision for datetime data types. |
| INTERVAL_TYPE | CHARACTER VARYING | The data type of interval qualifier for interval data types. |
| INTERVAL_PRECISION | INTEGER | The leading field precision for interval data types. |
| CHARACTER_SET_CATALOG | CHARACTER VARYING | The catalog (database name) for character string data types. |
| CHARACTER_SET_SCHEMA | CHARACTER VARYING | The name of public schema for character string data types. |
| CHARACTER_SET_NAME | CHARACTER VARYING | The 'Unicode' for character string data types. |
| COLLATION_CATALOG | CHARACTER VARYING | The catalog (database name) for character string data types. |
| COLLATION_SCHEMA | CHARACTER VARYING | The name of public schema for character string data types. |
| COLLATION_NAME | CHARACTER VARYING | The name of collation for character string data types. |
| DOMAIN_CATALOG | CHARACTER VARYING | The catalog for columns with domain. |
| DOMAIN_SCHEMA | CHARACTER VARYING | The schema of domain for columns with domain. |
| DOMAIN_NAME | CHARACTER VARYING | The name of domain for columns with domain. |
| MAXIMUM_CARDINALITY | INTEGER | The maximum cardinality for array data types. |
| DTD_IDENTIFIER | CHARACTER VARYING | The data type identifier to read additional information from INFORMATION_SCHEMA.ELEMENT_TYPES for array data types, INFORMATION_SCHEMA.ENUM_VALUES for ENUM data type, and INFORMATION_SCHEMA.FIELDS for row value data types. |
| IS_IDENTITY | CHARACTER VARYING | Whether column is an identity column ('YES' or 'NO'). |
| IDENTITY_GENERATION | CHARACTER VARYING | Identity generation ('ALWAYS' or 'BY DEFAULT') for identity columns. |
| IDENTITY_START | BIGINT | The initial start value for identity columns. |
| IDENTITY_INCREMENT | BIGINT | The increment value for identity columns. |
| IDENTITY_MAXIMUM | BIGINT | The maximum value for identity columns. |
| IDENTITY_MINIMUM | BIGINT | The minimum value for identity columns. |
| IDENTITY_CYCLE | CHARACTER VARYING | Whether identity values are cycled ('YES' or 'NO') for identity columns. |
| IS_GENERATED | CHARACTER VARYING | Whether column is an generated column ('ALWAYS' or 'NEVER') |
| GENERATION_EXPRESSION | CHARACTER VARYING | The SQL of GENERATED ALWAYS AS expression for generated columns. |
| DECLARED_DATA_TYPE | CHARACTER VARYING | The declared SQL data type name for numeric data types. |
| DECLARED_NUMERIC_PRECISION | INTEGER | The declared precision, if any, for numeric data types. |
| DECLARED_NUMERIC_SCALE | INTEGER | The declared scale, if any, for numeric data types. |
| GEOMETRY_TYPE | CHARACTER VARYING | The geometry type constraint, if any, for geometry data types. |
| GEOMETRY_SRID | INTEGER | The geometry SRID (Spatial Reference Identifier) constraint, if any, for geometry data types. |
| IDENTITY_BASE | BIGINT | The current base value for identity columns. |
| IDENTITY_CACHE | BIGINT | The cache size for identity columns. |
| COLUMN_ON_UPDATE | CHARACTER VARYING | The SQL of ON UPDATE expression, if any. |
| IS_VISIBLE | BOOLEAN | Whether column is visible (included into SELECT *). |
| DEFAULT_ON_NULL | BOOLEAN | Whether value of DEFAULT expression is used when NULL value is inserted. |
| SELECTIVITY | INTEGER | The selectivity of a column (0-100), used to choose the best index. |
| REMARKS | CHARACTER VARYING | Optional remarks. |
