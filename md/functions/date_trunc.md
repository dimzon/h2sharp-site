# DATE_TRUNC

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#date_trunc) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DATE_TRUNC([`datetimeField`](../grammar/datetime_field.md), [`dateAndTime`](../grammar/date_and_time.md))
```

🟢 includes non-standard H2 syntax

Truncates the specified date-time value to the specified field.

## Example

```sql
DATE_TRUNC(DAY, TIMESTAMP '2010-01-03 10:40:00');
```
