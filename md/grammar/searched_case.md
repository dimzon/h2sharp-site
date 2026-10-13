# Searched case

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#searched_case) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CASE { WHEN [`expression`](expression.md) THEN [`expression`](expression.md) } [...]
[ ELSE [`expression`](expression.md) ] END
```

Returns the first expression where the condition is true. If no else part is specified, return `NULL`.

## Example

```sql
CASE WHEN CNT<10 THEN 'Low' ELSE 'High' END
CASE WHEN A IS NULL THEN 'Null' ELSE 'Not null' END
```
