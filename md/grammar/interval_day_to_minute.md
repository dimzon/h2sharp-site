# INTERVAL DAY TO MINUTE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval_day_to_minute) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL [-|+] '[-|+][`dayInt`](int.md) hh:mm' DAY [ ( [`precisionInt`](int.md) ) ] TO MINUTE
```

An `INTERVAL DAY TO MINUTE` literal. If leading field precision is specified it should be from 1 to 18.

## Example

```sql
INTERVAL '10 11:12' DAY TO MINUTE
```
