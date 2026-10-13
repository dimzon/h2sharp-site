# ENUM_VALUES

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_enum_values) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about enum values.

| Column | Type | Description |
| --- | --- | --- |
| OBJECT_CATALOG | CHARACTER VARYING | The catalog (database name). |
| OBJECT_SCHEMA | CHARACTER VARYING | The schema of the object. |
| OBJECT_NAME | CHARACTER VARYING | The name of the object. |
| OBJECT_TYPE | CHARACTER VARYING | The TYPE of the object ('CONSTANT', 'DOMAIN', 'TABLE', or 'ROUTINE'). |
| ENUM_IDENTIFIER | CHARACTER VARYING | The DTD_IDENTIFIER value of the object. |
| VALUE_NAME | CHARACTER VARYING | The name of enum value. |
| VALUE_ORDINAL | CHARACTER VARYING | The ordinal of enum value. |
