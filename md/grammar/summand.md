# Summand

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#summand) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`factor`](factor.md) [ { { + | - } [`factor`](factor.md) } [...] ]
```

A value or a numeric sum.

Please note the text concatenation operator is `||`.

## Example

```sql
ID + 20
```
