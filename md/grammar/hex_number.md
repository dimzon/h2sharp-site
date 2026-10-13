# Hex Number

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#hex_number) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[+|-] {0x|0X} { [_] { [`digit`](digit.md) | a-f | A-F } [...] } [...]
```

A number written in hexadecimal notation.

## Example

```sql
0xff
0x_ABCD_1234
```
