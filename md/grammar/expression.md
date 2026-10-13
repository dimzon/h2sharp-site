# Expression

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#expression) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`andCondition`](and_condition.md) [ { OR [`andCondition`](and_condition.md) } [...] ]
```

Value or condition.

## Example

```sql
ID=1 OR NAME='Hi'
```
