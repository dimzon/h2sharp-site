# Nulls Distinct

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#nulls_distinct) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
NULLS { DISTINCT | NOT DISTINCT | { ALL DISTINCT } }
```

🟢 includes non-standard H2 syntax

Are nulls distinct for unique constraint, index, or predicate.

If `NULLS DISTINCT` is specified, rows with null value in any column are distinct. If `NULLS ALL DISTINCT` is specified, rows with null value in all columns are distinct. If `NULLS NOT DISTINCT` is specified, null values are identical.

Treatment of null values inside composite data types is not affected.

## Example

```sql
NULLS DISTINCT
NULLS NOT DISTINCT
```
