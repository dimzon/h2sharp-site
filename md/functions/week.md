# WEEK

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#week) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
WEEK([`dateAndTime`](../grammar/date_and_time.md))
```

🔴 compatibility-only syntax

Returns the week (1-53) from a date/time value.

This function is deprecated, use [EXTRACT](extract.md) instead of it.

This function uses the current system locale.

## Example

```sql
WEEK(CREATED)
```
