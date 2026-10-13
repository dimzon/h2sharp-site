# Bytes

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#bytes) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
X'[`hex`](hex.md)' [ '[`hex`](hex.md)' [...] ]
```

A binary string value. The hex value is not case sensitive and may contain space characters as separators. If there are more than one group of quoted hex values, groups must be separated with whitespace.

## Example

```sql
X''
X'01FF'
X'01 bc 2a'
X'01' '02'
```
