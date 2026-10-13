# PARSEDATETIME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#parsedatetime) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
PARSEDATETIME([`string`](../grammar/string.md), [`formatString`](../grammar/string.md)
[, [`localeString`](../grammar/string.md) [, [`timeZoneString`](../grammar/string.md)]])
```

🟢 includes non-standard H2 syntax

Parses a string and returns a `TIMESTAMP WITH TIME ZONE` value. The most important format characters are: y year, M month, d day, H hour, m minute, s second. For details of the format, see `java.time.format.DateTimeFormatter`.

If timeZoneString is specified, it is used as default.

See also [cast specification](../grammar/cast_specification.md).

## Example

```sql
CALL PARSEDATETIME('Sat, 3 Feb 2001 03:05:06 GMT',
    'EEE, d MMM yyyy HH:mm:ss z', 'en', 'GMT')
```
