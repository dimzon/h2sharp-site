# SHOW

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#show) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SHOW { SCHEMAS | TABLES [ FROM [`schemaName`](../grammar/name.md) ] |
COLUMNS FROM [`tableName`](../grammar/name.md) [ FROM [`schemaName`](../grammar/name.md) ] }
```

🔴 compatibility-only syntax

Lists the schemas, tables, or the columns of a table.

## Example

```sql
SHOW TABLES
```
