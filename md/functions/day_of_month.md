# DAY_OF_MONTH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#day_of_month) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DAY_OF_MONTH({[`dateAndTime`](../grammar/date_and_time.md)|[`interval`](../grammar/interval.md)})
```

🔴 compatibility-only syntax

Returns the day of the month (1-31).

This function is deprecated, use [EXTRACT](extract.md) instead of it.

## Example

```sql
DAY_OF_MONTH(CREATED)
```
