# SECOND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#second) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SECOND([`dateAndTime`](../grammar/date_and_time.md))
```

🔴 compatibility-only syntax

Returns the second (0-59) from a date/time value.

This function is deprecated, use [EXTRACT](extract.md) instead of it.

## Example

```sql
SECOND(CREATED|interval)
```
