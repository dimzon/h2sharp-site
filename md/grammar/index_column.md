# Index Column

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#index_column) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`columnName`](name.md) [ ASC | DESC ] [ NULLS { FIRST | LAST } ]
```

Indexes this column in ascending or descending order. Usually it is not required to specify the order; however doing so will speed up large queries that order the column in the same way.

## Example

```sql
NAME
```
