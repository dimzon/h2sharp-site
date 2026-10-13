# Operand

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#operand) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`summand`](summand.md) [ { || [`summand`](summand.md) } [...] ]
```

Performs the concatenation of character string, binary string, or array values. In the default mode, the result is `NULL` if either parameter is `NULL`. In compatibility modes result of string concatenation with `NULL` parameter can be different.

## Example

```sql
'Hi' || ' Eva'
X'AB' || X'CD'
ARRAY[1, 2] || 3
1 || ARRAY[2, 3]
ARRAY[1, 2] || ARRAY[3, 4]
```
