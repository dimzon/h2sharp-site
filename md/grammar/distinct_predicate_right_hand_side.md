# Distinct Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#distinct_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
IS [ NOT ] [ DISTINCT FROM ] [`operand`](operand.md)
```

Right side of distinct predicate.

Distinct predicate is null-safe, meaning `NULL` is considered the same as `NULL`, and the condition never evaluates to `UNKNOWN`.

## Example

```sql
IS NOT DISTINCT FROM OTHER
```
