# Sort specification list

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#sort_specification_list) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`sortSpecification`](sort_specification.md) [,...]
```

Sorts the result by expressions.

## Example

```sql
V
A, B DESC NULLS FIRST
```
