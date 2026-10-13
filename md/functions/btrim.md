# BTRIM

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#btrim) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BTRIM([`string`](../grammar/string.md) [, [`charactersToTrimString`](../grammar/string.md)])
```

Removes all leading and trailing spaces or other specified characters from a string, multiple characters can be specified.

## Example

```sql
BTRIM(NAME)
BTRIM(NAME, ' _~');
```
