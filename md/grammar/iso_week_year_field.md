# ISO week year field

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#iso_week_year_field) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ ISO_WEEK_YEAR } | { ISO_YEAR | ISOYEAR }
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Returns the `ISO` week-based year from a date/time value.

## Example

```sql
ISO_WEEK_YEAR
```
