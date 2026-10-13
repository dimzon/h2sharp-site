# ISO_WEEK

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#iso_week) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ISO_WEEK([`dateAndTime`](../grammar/date_and_time.md))
```

🔴 compatibility-only syntax

Returns the `ISO` week (1-53) from a date/time value.

This function is deprecated, use [EXTRACT](extract.md) instead of it.

This function uses the `ISO` definition when first week of year should have at least four days and week is started with Monday.

## Example

```sql
ISO_WEEK(CREATED)
```
