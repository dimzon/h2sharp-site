# Grouping element

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#grouping_element) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`expression`](expression.md) | ([`expression`](expression.md) [, ...]) | ()
```

A grouping element of `GROUP BY` clause.

## Example

```sql
A
(B, C)
()
```
