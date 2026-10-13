# INTERVAL DAY TO HOUR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval_day_to_hour) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL [-|+] '[-|+][`dayInt`](int.md) [`hoursInt`](int.md)' DAY [ ( [`precisionInt`](int.md) ) ] TO HOUR
```

An `INTERVAL DAY TO HOUR` literal. If leading field precision is specified it should be from 1 to 18.

## Example

```sql
INTERVAL '10 11' DAY TO HOUR
```
