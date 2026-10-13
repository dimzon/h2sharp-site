# And Condition

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#and_condition) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`condition`](condition.md) [ { AND [`condition`](condition.md) } [...] ]
```

Value or condition.

## Example

```sql
ID=1 AND NAME='Hi'
```
