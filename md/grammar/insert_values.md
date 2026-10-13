# Insert values

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#insert_values) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
VALUES { DEFAULT|[`expression`](expression.md) | [ROW] ({DEFAULT|[`expression`](expression.md)} [,...]) }, [,...]
```

Values for `INSERT` statement.

## Example

```sql
VALUES (1, 'Test')
```
