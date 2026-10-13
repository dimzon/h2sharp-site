# REPLACE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#replace) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REPLACE([`string`](../grammar/string.md), [`searchString`](../grammar/string.md) [, [`replacementString`](../grammar/string.md)])
```

🟢 includes non-standard H2 syntax

Replaces all occurrences of a search string in a text with another string. If no replacement is specified, the search string is removed from the original string. If any parameter is null, the result is null.

## Example

```sql
REPLACE(NAME, ' ')
```
