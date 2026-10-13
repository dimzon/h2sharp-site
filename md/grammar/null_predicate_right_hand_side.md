# Null Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#null_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
IS [ NOT ] NULL
```

Right side of null predicate.

Check whether the specified value(s) are `NULL` values. To test multiple values a row value must be specified. `IS NULL` returns `TRUE` if and only if all values are `NULL` values; otherwise it returns `FALSE`. `IS NOT NULL` returns `TRUE` if and only if all values are not `NULL` values; otherwise it returns `FALSE`.

## Example

```sql
IS NULL
```
