# EXPLAIN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#explain) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
EXPLAIN { [ PLAN FOR ] | ANALYZE }
{ [`query`](../grammar/query.md) | [`insert`](insert.md) | [`update`](update.md) | [`delete`](delete.md) | [`mergeInto`](merge_into.md) | [`mergeUsing`](merge_using.md) }
```

🟢 includes non-standard H2 syntax

Shows the execution plan for a statement. When using `EXPLAIN ANALYZE`, the statement is actually executed, and the query plan will include the actual row scan count for each table.

## Example

```sql
EXPLAIN SELECT * FROM TEST WHERE ID=1
```
