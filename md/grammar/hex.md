# Hex

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#hex) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[' ' [...]] { { [`digit`](digit.md) | a-f | A-F } [' ' [...]] { [`digit`](digit.md) | a-f | A-F } [' ' [...]] } [...]
```

The hexadecimal representation of a number or of bytes with optional space characters. Two hexadecimal digit characters are one byte.

## Example

```sql
cafe
11 22 33
a b  c d
```
