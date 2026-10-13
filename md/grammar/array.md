# Array

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#array) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ARRAY '[' [ [`expression`](expression.md) [,...] ] ']'
```

An array of values.

## Example

```sql
ARRAY[1, 2]
ARRAY[1]
ARRAY[]
```
