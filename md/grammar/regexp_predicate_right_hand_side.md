# Regexp Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#regexp_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ [ NOT ] REGEXP [`operand`](operand.md) }
```

🟢 includes non-standard H2 syntax

Right side of Regexp predicate.

Regular expression matching is used. See Java `Matcher.find` for details.

## Example

```sql
REGEXP '[a-z]'
```
