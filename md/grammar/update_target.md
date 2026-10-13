# Update target

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#update_target) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`columnName`](name.md) [ '[' [`int`](int.md) ']' [...] ]
```

Column or element of a column of `ARRAY` data type.

If array indexes are specified, column must have a compatible `ARRAY` data type and updated rows may not have `NULL` values in this column. It means for C[2][3] both C and C[2] may not be `NULL`. Too short arrays are expanded, missing elements are set to `NULL`.

## Example

```sql
A
B[1]
C[2][3]
```
