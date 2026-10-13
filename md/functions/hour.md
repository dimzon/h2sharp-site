# HOUR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#hour) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
HOUR({[`dateAndTime`](../grammar/date_and_time.md)|[`interval`](../grammar/interval.md)})
```

🔴 compatibility-only syntax

Returns the hour (0-23) from a date/time value.

This function is deprecated, use [EXTRACT](extract.md) instead of it.

## Example

```sql
HOUR(CREATED)
```
