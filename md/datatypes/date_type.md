# DATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#date_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DATE
```

The date data type. The proleptic Gregorian calendar is used.

See also [date](../grammar/date.md) literal grammar.

In `JDBC` this data type is mapped to `java.sql.Date`, with the time set to `00:00:00` (or to the next possible time if midnight doesn't exist for the given date and time zone due to a daylight saving change). `java.time.LocalDate` is also supported and recommended.

In `org.h2.api.Aggregate, org.h2.api.AggregateFunction`, and `org.h2.api.Trigger` this data type is mapped to `java.time.LocalDate`.

If your time zone had `LMT` (local mean time) in the past and you use such old dates (depends on the time zone, usually 100 or more years ago), don't use `java.sql.Date` to read and write them.

If you deal with very old dates (before 1582-10-15) note that `java.sql.Date` uses a mixed Julian/Gregorian calendar, `java.util.GregorianCalendar` can be configured to proleptic Gregorian with `setGregorianChange(new java.util.Date(Long.MIN_VALUE))` and used to read or write fields of dates.

## Example

```sql
DATE
```
