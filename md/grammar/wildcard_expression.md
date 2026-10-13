# Wildcard expression

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#wildcard_expression) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[[[`schemaName`](name.md).][`tableAlias`](alias.md).]*
[EXCEPT ([[[`schemaName`](name.md).][`tableAlias`](alias.md).][`columnName`](name.md), [,...])]
```

🟢 includes non-standard H2 syntax

A wildcard expression in a `SELECT` statement. A wildcard expression represents all visible columns. Some columns can be excluded with optional `EXCEPT` clause.

## Example

```sql
*
* EXCEPT (DATA)
```
