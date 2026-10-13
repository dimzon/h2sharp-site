# Sort specification

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#sort_specification) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`expression`](expression.md) [ ASC | DESC ] [ NULLS { FIRST | LAST } ]
```

Sorts the result by an expression.

## Example

```sql
X ASC NULLS FIRST
```
