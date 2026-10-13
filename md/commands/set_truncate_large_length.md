# SET TRUNCATE_LARGE_LENGTH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_truncate_large_length) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET TRUNCATE_LARGE_LENGTH { TRUE | FALSE }
```

🟢 includes non-standard H2 syntax

If `TRUE` is specified, the `CHARACTER, CHARACTER VARYING, VARCHAR_IGNORECASE, BINARY, BINARY_VARYING, JAVA_OBJECT` and `JSON` data types with too large length will be treated as these data types with maximum allowed length instead. By default, or if `FALSE` is specified, such definitions throw an exception. This setting can be used for compatibility with definitions from older versions of H2.

This setting can be appended to the database URL: `jdbc:h2:./test;TRUNCATE_LARGE_LENGTH=TRUE`

## Example

```sql
SET TRUNCATE_LARGE_LENGTH TRUE
```
