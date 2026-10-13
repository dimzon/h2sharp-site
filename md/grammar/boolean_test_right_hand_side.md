# Boolean Test Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#boolean_test_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
IS [ NOT ] { TRUE | FALSE | UNKNOWN }
```

Right side of boolean test.

Checks whether the specified value is (not) `TRUE, FALSE`, or `UNKNOWN` (`NULL`) and return `TRUE` or `FALSE`. This test is null-safe.

## Example

```sql
IS TRUE
```
