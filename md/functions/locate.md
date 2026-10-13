# LOCATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#locate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ LOCATE([`searchString`](../grammar/string.md), [`string`](../grammar/string.md) [, [`startInt`](../grammar/int.md)]) }
| { INSTR([`string`](../grammar/string.md), [`searchString`](../grammar/string.md), [, [`startInt`](../grammar/int.md)]) }
| { POSITION([`searchString`](../grammar/string.md), [`string`](../grammar/string.md)) }
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Returns the location of a search string in a string. If a start position is used, the characters before it are ignored. If position is negative, the rightmost location is returned. 0 is returned if the search string is not found. Please note this function is case sensitive, even if the parameters are not.

## Example

```sql
LOCATE('.', NAME)
```
