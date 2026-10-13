# Time

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#time) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TIME [ WITHOUT TIME ZONE ] 'hh:mm:ss[.nnnnnnnnn]'
```

A time literal. A value is between 0:00:00 and 23:59:59.999999999 and has nanosecond resolution.

## Example

```sql
TIME '23:59:59'
```
