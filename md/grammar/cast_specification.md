# Cast specification

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#cast_specification) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CAST([`value`](value.md) AS [`dataTypeOrDomain`](data_type_or_domain.md) [ FORMAT [`templateString`](string.md) ])
```

Converts a value to another data type. The following conversion rules are used: When converting a number to a boolean, 0 is false and every other value is true. When converting a boolean to a number, false is 0 and true is 1. When converting a number to a number of another type, the value is checked for overflow. When converting a string to binary, `UTF`-8 encoding is used. Note that some data types may need explicitly specified precision to avoid overflow or rounding.

Template may only be specified for casts from datetime data types to character string data types and for casts from character string data types to datetime data types.

'-', '.', '/', ',', '''', ';', ':' and ' ' (space) characters can be used as delimiters.

Y, `YY, YYY, YYYY` represent last 1, 2, 3, or 4 digits of year. `YYYY`, if delimited, can also be used to parse any year, including negative years. When a year is parsed with Y, `YY`, or `YYY` pattern missing leading digits are filled using digits from the current year.

`RR` and `RRRR` have the same meaning as `YY` and `YYYY` for formatting. When a year is parsed with `RR`, the resulting year is within current year - 49 years and current year + 50 years in H2, other database systems may use different range of years.

`MM` represent a month.

`DD` represent a day of month.

`DDD` represent a day of year, if this pattern in specified, `MM` and `DD` may not be specified.

`HH24` represent an hour (from 0 to 23).

`HH` and `HH12` represent an hour (from 1 to 12), this pattern may only be used together with A.M. or P.M. pattern. These patterns may not be used together with `HH24`.

`MI` represent minutes.

`SS` represent seconds of minute.

`SSSSS` represent seconds of day, this pattern may not be used together with `HH24, HH` (`HH12`), A.M. (P.M.), `MI` or `SS` pattern.

`FF1, FF2`, ..., `FF9` represent fractional seconds.

`TZH, TZM` and `TZH` represent hours, minutes and seconds of time zone offset.

Multiple patterns for the same datetime field may not be specified.

If year is not specified, current year is used. If month is not specified, current month is used. If day is not specified, 1 is used.

If some fields of time or time zone are not specified, 0 is used.

## Example

```sql
CAST(NAME AS INT);
CAST(TIMESTAMP '2010-01-01 10:40:00.123456' AS TIME(6));
CAST('12:00:00 P.M.' AS TIME FORMAT 'HH:MI:SS A.M.');
```
