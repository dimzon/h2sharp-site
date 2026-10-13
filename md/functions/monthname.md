# MONTHNAME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#monthname) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
MONTHNAME([`dateAndTime`](../grammar/date_and_time.md))
```

🟢 includes non-standard H2 syntax

Returns the name of the month (in English).

## Example

```sql
MONTHNAME(CREATED)
```
