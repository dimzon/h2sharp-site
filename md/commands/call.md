# CALL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#call) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CALL [`expression`](../grammar/expression.md)
```

Calculates a simple expression. This statement returns a result set with one row, except if the called function returns a result set itself. If the called function returns an array, then each element in this array is returned as a column.

## Example

```sql
CALL 15*25
```
