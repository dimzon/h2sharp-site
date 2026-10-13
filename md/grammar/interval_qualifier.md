# Interval qualifier

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#interval_qualifier) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
YEAR [([`precisionInt`](int.md))] [ TO MONTH ]
| MONTH [([`precisionInt`](int.md))]
| DAY [([`precisionInt`](int.md))] [ TO { HOUR | MINUTE | SECOND [([`scaleInt`](int.md))] } ]
| HOUR [([`precisionInt`](int.md))] [ TO { MINUTE | SECOND [([`scaleInt`](int.md))] } ]
| MINUTE [([`precisionInt`](int.md))] [ TO SECOND [([`scaleInt`](int.md))] ]
| SECOND [([`precisionInt`](int.md) [, [`scaleInt`](int.md)])]
```

An interval qualifier.

## Example

```sql
DAY TO SECOND
```
