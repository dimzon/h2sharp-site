# EXTRACT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#extract) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
EXTRACT ( [`datetimeField`](../grammar/datetime_field.md) FROM { [`dateAndTime`](../grammar/date_and_time.md) | [`interval`](../grammar/interval.md) })
```

Returns a value of the specific time unit from a date/time value. This method returns a numeric value with `EPOCH` field and an int for all other fields.

## Example

```sql
EXTRACT(SECOND FROM CURRENT_TIMESTAMP)
```
