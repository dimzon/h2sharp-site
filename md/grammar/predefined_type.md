# Predefined Type

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#predefined_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`characterType`](../datatypes/character_type.md) | [`characterVaryingType`](../datatypes/character_varying_type.md) | [`characterLargeObjectType`](../datatypes/character_large_object_type.md)
| [`binaryType`](../datatypes/binary_type.md) | [`binaryVaryingType`](../datatypes/binary_varying_type.md) | [`binaryLargeObjectType`](../datatypes/binary_large_object_type.md)
| [`booleanType`](../datatypes/boolean_type.md)
| [`smallintType`](../datatypes/smallint_type.md) | [`integerType`](../datatypes/integer_type.md) | [`bigintType`](../datatypes/bigint_type.md)
| [`numericType`](../datatypes/numeric_type.md) | [`realType`](../datatypes/real_type.md) | [`doublePrecisionType`](../datatypes/double_precision_type.md) | [`decfloatType`](../datatypes/decfloat_type.md)
| [`dateType`](../datatypes/date_type.md) | [`timeType`](../datatypes/time_type.md) | [`timeWithTimeZoneType`](../datatypes/time_with_time_zone_type.md)
| [`timestampType`](../datatypes/timestamp_type.md) | [`timestampWithTimeZoneType`](../datatypes/timestamp_with_time_zone_type.md)
| [`intervalType`](../datatypes/interval_type.md)
| { [`tinyintType`](../datatypes/tinyint_type.md) | [`javaObjectType`](../datatypes/java_object_type.md) | [`enumType`](../datatypes/enum_type.md)
| [`geometryType`](../datatypes/geometry_type.md) | [`jsonType`](../datatypes/json_type.md) | [`uuidType`](../datatypes/uuid_type.md) }
```

🟢 includes non-standard H2 syntax

A predefined data type.

## Example

```sql
INTEGER
```
