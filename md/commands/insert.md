# INSERT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#insert) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INSERT INTO [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) [ ( [`columnName`](../grammar/name.md) [,...] ) ]
{ [ [`overrideClause`](../grammar/override_clause.md) ] { [`insertValues`](../grammar/insert_values.md) | [ DIRECT ] [`query`](../grammar/query.md) } }
| DEFAULT VALUES
```

🟢 includes non-standard H2 syntax

Inserts a new row / new rows into a table.

If column names aren't specified a list of all visible columns in the table is assumed.

When using `DIRECT`, then the results from the query are directly applied in the target table without any intermediate step.

## Example

```sql
INSERT INTO TEST VALUES(1, 'Hello')
```
