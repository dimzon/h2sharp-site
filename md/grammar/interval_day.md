# INTERVAL DAY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval_day) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL [-|+] '[-|+][`dayInt`](int.md)' DAY [ ( [`precisionInt`](int.md) ) ]
```

An `INTERVAL DAY` literal. If precision is specified it should be from 1 to 18.

## Example

```sql
INTERVAL '10' DAY
```
