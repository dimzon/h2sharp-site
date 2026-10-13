# INTERVAL YEAR TO MONTH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval_year_to_month) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL [-|+] '[-|+][`yearInt`](int.md)-[`monthInt`](int.md)' YEAR [ ( [`precisionInt`](int.md) ) ] TO MONTH
```

An `INTERVAL YEAR TO MONTH` literal. If leading field precision is specified it should be from 1 to 18.

## Example

```sql
INTERVAL '1-6' YEAR TO MONTH
```
