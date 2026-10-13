# Merge when matched clause

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#merge_when_matched_clause) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
WHEN MATCHED [ AND [`expression`](expression.md) ] THEN
UPDATE SET [`setClauseList`](set_clause_list.md) | DELETE
```

`WHEN MATCHED` clause for `MERGE USING` command.

Updates or deletes rows in a target table.

## Example

```sql
WHEN MATCHED THEN UPDATE SET NAME = S.NAME
WHEN MATCHED THEN DELETE
```
