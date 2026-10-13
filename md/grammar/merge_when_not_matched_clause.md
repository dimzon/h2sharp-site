# Merge when not matched clause

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#merge_when_not_matched_clause) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
WHEN NOT MATCHED [ AND [`expression`](expression.md) ] THEN INSERT
[ ( [`columnName`](name.md) [,...] ) ]
[ [`overrideClause`](override_clause.md) ]
VALUES ({DEFAULT|[`expression`](expression.md)} [,...])
```

`WHEN NOT MATCHED` clause for `MERGE USING` command.

Inserts rows into a target table.

If column names aren't specified a list of all visible columns in the target table is assumed.

## Example

```sql
WHEN NOT MATCHED THEN INSERT (ID, NAME) VALUES (S.ID, S.NAME)
```
