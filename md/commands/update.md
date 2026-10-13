# UPDATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#update) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
UPDATE [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) [ [ AS ] [`newTableAlias`](../grammar/alias.md) ] SET [`setClauseList`](../grammar/set_clause_list.md)
[ WHERE [`expression`](../grammar/expression.md) ] [ ORDER BY [`sortSpecificationList`](../grammar/sort_specification_list.md) ]
FETCH { FIRST | NEXT } [ [`expression`](../grammar/expression.md) ] { ROW | ROWS } ONLY
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Updates data in a table. `ORDER BY` is supported for MySQL compatibility, but it is ignored. If `FETCH` is specified, at most the specified number of rows are updated (no limit if null or smaller than zero).

## Example

```sql
UPDATE TEST SET NAME='Hi' WHERE ID=1;
UPDATE PERSON P SET NAME=(SELECT A.NAME FROM ADDRESS A WHERE A.ID=P.ID);
```
