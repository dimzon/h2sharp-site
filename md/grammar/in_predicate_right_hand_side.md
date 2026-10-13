# In Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#in_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[ NOT ] IN ( { [`query`](query.md) | [`expression`](expression.md) [,...] } )
```

Right side of in predicate.

Checks presence of value in the specified list of values or in result of the specified query.

Returns `TRUE` if row value on the left side is equal to one of values on the right side, `FALSE` if all comparison operations were evaluated to `FALSE` or right side has no values, and `UNKNOWN` otherwise.

This operation is logically equivalent to `OR` between comparison operations comparing left side and each value from the right side.

## Example

```sql
IN (A, B, C)
IN (SELECT V FROM TEST)
```
