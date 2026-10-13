# Condition Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#condition_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`comparisonRightHandSide`](comparison_right_hand_side.md)
| [`quantifiedComparisonRightHandSide`](quantified_comparison_right_hand_side.md)
| [`nullPredicateRightHandSide`](null_predicate_right_hand_side.md)
| [`distinctPredicateRightHandSide`](distinct_predicate_right_hand_side.md)
| [`quantifiedDistinctPredicateRightHandSide`](quantified_distinct_predicate_right_hand_side.md)
| [`booleanTestRightHandSide`](boolean_test_right_hand_side.md)
| [`typePredicateRightHandSide`](type_predicate_right_hand_side.md)
| [`jsonPredicateRightHandSide`](json_predicate_right_hand_side.md)
| [`betweenPredicateRightHandSide`](between_predicate_right_hand_side.md)
| [`inPredicateRightHandSide`](in_predicate_right_hand_side.md)
| [`likePredicateRightHandSide`](like_predicate_right_hand_side.md)
| [`regexpPredicateRightHandSide`](regexp_predicate_right_hand_side.md)
```

The right hand side of a condition.

## Example

```sql
> 10
IS NULL
IS NOT NULL
IS NOT DISTINCT FROM B
IS OF (DATE, TIMESTAMP, TIMESTAMP WITH TIME ZONE)
IS JSON OBJECT WITH UNIQUE KEYS
LIKE 'Jo%'
```
