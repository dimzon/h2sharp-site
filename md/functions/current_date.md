# CURRENT_DATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#current_date) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CURRENT_DATE
```

Returns the current date.

These functions return the same value within a transaction (default) or within a command depending on database mode.

[SET TIME ZONE](../commands/set_time_zone.md) command reevaluates the value for these functions using the same original `UTC` timestamp of transaction.

## Example

```sql
CURRENT_DATE
```
