# Query

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#query) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`select`](../commands/select.md) | [`explicitTable`](../commands/explicit_table.md) | [`tableValue`](../commands/table_value.md)
```

A query, such as `SELECT`, explicit table, or table value.

## Example

```sql
SELECT ID FROM TEST;
TABLE TEST;
VALUES (1, 2), (3, 4);
```
