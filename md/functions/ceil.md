# CEIL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#ceil) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ CEIL | CEILING } ([`numeric`](../grammar/numeric.md))
```

Returns the smallest integer value that is greater than or equal to the argument. This method returns value of the same type as argument, but with scale set to 0 and adjusted precision, if applicable.

## Example

```sql
CEIL(A)
```
