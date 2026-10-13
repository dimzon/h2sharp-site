# Condition

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#condition) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`operand`](operand.md) [ [`conditionRightHandSide`](condition_right_hand_side.md) ]
| NOT [`condition`](condition.md)
| EXISTS ( [`query`](query.md) )
| UNIQUE [ [`nullsDistinct`](nulls_distinct.md) ] ( [`query`](query.md) )
| INTERSECTS ([`operand`](operand.md), [`operand`](operand.md))
```

🟢 includes non-standard H2 syntax

Boolean value or condition.

`NOT` condition negates the result of subcondition and returns `TRUE, FALSE`, or `UNKNOWN` (`NULL`).

`EXISTS` predicate tests whether the result of the specified subquery is not empty and returns `TRUE` or `FALSE`.

`UNIQUE` predicate tests absence of duplicate rows in the specified subquery and returns `TRUE` or `FALSE`. If nulls distinct clause is not specified, `NULLS DISTINCT` is implicit.

`INTERSECTS` checks whether 2D bounding boxes of specified geometries intersect with each other and returns `TRUE` or `FALSE`.

## Example

```sql
ID <> 2
NOT(A OR B)
EXISTS (SELECT NULL FROM TEST T WHERE T.GROUP_ID = P.ID)
UNIQUE (SELECT A, B FROM TEST T WHERE T.CATEGORY = CAT)
INTERSECTS(GEOM1, GEOM2)
```
