# RTRIM

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#rtrim) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
RTRIM([`string`](../grammar/string.md) [, [`charactersToTrimString`](../grammar/string.md)])
```

Removes all trailing spaces or other specified characters from a string, multiple characters can be specified.

## Example

```sql
RTRIM(NAME)
RTRIM(NAME, ' _~');
```
