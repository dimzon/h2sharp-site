# ISO_DAY_OF_WEEK

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#iso_day_of_week) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ISO_DAY_OF_WEEK([`dateAndTime`](../grammar/date_and_time.md))
```

🔴 compatibility-only syntax

Returns the `ISO` day of the week (1 means Monday).

This function is deprecated, use [EXTRACT](extract.md) instead of it.

## Example

```sql
ISO_DAY_OF_WEEK(CREATED)
```
