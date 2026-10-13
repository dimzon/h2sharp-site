# Column

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#column) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[[[`schemaName`](name.md).][`tableAlias`](alias.md).] { [`columnName`](name.md) | { _ROWID_ } }
```

🟢 includes non-standard H2 syntax

A column name with optional table alias and schema. _`ROWID_` can be used to access unique row identifier.

## Example

```sql
ID
```
