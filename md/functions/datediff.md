# DATEDIFF

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#datediff) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ DATEDIFF | TIMESTAMPDIFF } ([`datetimeField`](../grammar/datetime_field.md), [`aDateAndTime`](../grammar/date_and_time.md), [`bDateAndTime`](../grammar/date_and_time.md))
```

🟢 includes non-standard H2 syntax

Returns the number of crossed unit boundaries between two date/time values. This method returns a long. The datetimeField indicates the unit. Only `TIMEZONE_HOUR, TIMEZONE_MINUTE`, and `TIMEZONE_SECOND` fields use the time zone offset component. With all other fields if date/time values have time zone offset component it is ignored.

## Example

```sql
DATEDIFF(YEAR, T1.CREATED, T2.CREATED)
```
