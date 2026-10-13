# FLOOR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#floor) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
FLOOR([`numeric`](../grammar/numeric.md))
```

Returns the largest integer value that is less than or equal to the argument. This method returns value of the same type as argument, but with scale set to 0 and adjusted precision, if applicable.

## Example

```sql
FLOOR(A)
```
