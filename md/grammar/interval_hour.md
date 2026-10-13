# INTERVAL HOUR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval_hour) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL [-|+] '[-|+][`hourInt`](int.md)' HOUR [ ( [`precisionInt`](int.md) ) ]
```

An `INTERVAL HOUR` literal. If precision is specified it should be from 1 to 18.

## Example

```sql
INTERVAL '10' HOUR
```
