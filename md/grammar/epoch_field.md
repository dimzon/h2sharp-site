# Epoch field

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#epoch_field) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
EPOCH
```

🟢 includes non-standard H2 syntax

For `TIMESTAMP` values number of seconds since 1970-01-01 00:00:00 in local time zone. For `TIMESTAMP WITH TIME ZONE` values number of seconds since 1970-01-01 00:00:00 in `UTC` time zone. For `DATE` values number of seconds since 1970-01-01. For `TIME` values number of seconds since midnight.

## Example

```sql
EPOCH
```
