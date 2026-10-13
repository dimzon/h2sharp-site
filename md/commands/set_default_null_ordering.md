# SET DEFAULT_NULL_ORDERING

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_default_null_ordering) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET DEFAULT_NULL_ORDERING { LOW | HIGH | FIRST | LAST }
```

🟢 includes non-standard H2 syntax

Changes the default ordering of `NULL` values. This setting affects new indexes without explicit `NULLS FIRST` or `NULLS LAST` columns, and ordering clauses of other commands without explicit null ordering. This setting doesn't affect ordering of `NULL` values inside `ARRAY` or `ROW` values (`ARRAY[NULL]` is always considered as smaller than `ARRAY[1]` during sorting).

`LOW` is the default one, `NULL` values are considered as smaller than other values during sorting.

With `HIGH` default ordering `NULL` values are considered as larger than other values during sorting.

With `FIRST` default ordering `NULL` values are sorted before other values, no matter if ascending or descending order is used.

With `LAST` default ordering `NULL` values are sorted after other values, no matter if ascending or descending order is used.

Please note that `FIRST` and `LAST` make impossible to use an index on `(A ASC)` for `ORDER BY A DESC` if column is nullable.

This setting is not persistent, but indexes are persisted with explicit `NULLS FIRST` or `NULLS LAST` ordering and aren't affected by changes in this setting. Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting can be appended to the database URL: `jdbc:h2:./test;DEFAULT_NULL_ORDERING=HIGH`

## Example

```sql
SET DEFAULT_NULL_ORDERING HIGH
```
