# Table Expression

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#table_expression) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ [ [`schemaName`](name.md). ] [`tableName`](name.md)
| ( [`query`](query.md) )
| [`unnest`](../functions/unnest.md)
| [`table`](../functions/table.md)
| [`dataChangeDeltaTable`](data_change_delta_table.md) }
[ [ AS ] [`newTableAlias`](alias.md) [ ( [`columnName`](name.md) [,...] ) ] ]
[ USE INDEX ([ [`indexName`](name.md) [,...] ]) ]
[ { { LEFT | RIGHT } [ OUTER ] | [ INNER ] | CROSS | NATURAL }
JOIN [`tableExpression`](table_expression.md) [ [`joinSpecification`](join_specification.md) ] ]
```

🟢 includes non-standard H2 syntax

Joins a table. The join specification is not supported for cross and natural joins. A natural join is an inner join, where the condition is automatically on the columns with the same name.

## Example

```sql
TEST1 AS T1 LEFT JOIN TEST2 AS T2 ON T1.ID = T2.PARENT_ID
```
