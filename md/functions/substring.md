# SUBSTRING

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#substring) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SUBSTRING ( {[`string`](../grammar/string.md)|[`bytes`](../grammar/bytes.md)} FROM [`startInt`](../grammar/int.md) [ FOR [`lengthInt`](../grammar/int.md) ] )
| { { SUBSTRING | SUBSTR } ( {[`string`](../grammar/string.md)|[`bytes`](../grammar/bytes.md)}, [`startInt`](../grammar/int.md) [, [`lengthInt`](../grammar/int.md) ] ) }
```

🔴 compatibility-only syntax

Returns a substring of a string starting at a position. If the start index is negative, then the start index is relative to the end of the string. The length is optional.

## Example

```sql
CALL SUBSTRING('[Hello]' FROM 2 FOR 5);
CALL SUBSTRING('hour' FROM 2);
```
