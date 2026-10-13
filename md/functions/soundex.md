# SOUNDEX

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#soundex) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SOUNDEX([`string`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Returns a four character upper-case code representing the sound of a string as pronounced in English. This method returns a string, or null if parameter is null. See [https://en.wikipedia.org/wiki/Soundex](https://en.wikipedia.org/wiki/Soundex) for more information.

## Example

```sql
SOUNDEX(NAME)
```
