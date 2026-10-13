# INSERT Function

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#insert_function) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INSERT([`originalString`](../grammar/string.md), [`startInt`](../grammar/int.md), [`lengthInt`](../grammar/int.md), [`addString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Inserts a additional string into the original string at a specified start position. The length specifies the number of characters that are removed at the start position in the original string. This method returns a string.

## Example

```sql
INSERT(NAME, 1, 1, ' ')
```
