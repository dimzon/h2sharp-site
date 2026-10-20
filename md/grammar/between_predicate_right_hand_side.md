# Between Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#between_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[ NOT ] BETWEEN [ ASYMMETRIC | SYMMETRIC ] [`operand`](operand.md) AND [`operand`](operand.md)
```

Right side of between predicate.

Checks whether the value is within the range inclusive. `V BETWEEN [ ASYMMETRIC ] A AND B` is equivalent to `A <= V AND V <= B`. `V BETWEEN SYMMETRIC A AND B` is equivalent to `A <= V AND V <= B OR A >= V AND V >= B`.

## Example

```sql
BETWEEN LOW AND HIGH
```
