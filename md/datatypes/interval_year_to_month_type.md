# INTERVAL YEAR TO MONTH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#interval_year_to_month_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INTERVAL YEAR [ ( [`precisionInt`](../grammar/int.md) ) ] TO MONTH
```

Interval data type. If leading field precision is specified it should be from 1 to 18, 2 is default.

See also [year to month interval](../grammar/interval_year_to_month.md) literal grammar. Mapped to `org.h2.api.Interval`. `java.time.Period` is also supported.

## Example

```sql
INTERVAL YEAR TO MONTH
```
