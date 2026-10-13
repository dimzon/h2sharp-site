# Merge when clause

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#merge_when_clause) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`mergeWhenMatchedClause`](merge_when_matched_clause.md)|[`mergeWhenNotMatchedClause`](merge_when_not_matched_clause.md)
```

`WHEN MATCHED` or `WHEN NOT MATCHED` clause for `MERGE USING` command.

## Example

```sql
WHEN MATCHED THEN DELETE
```
