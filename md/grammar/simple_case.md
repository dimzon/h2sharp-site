# Simple case

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#simple_case) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CASE [`expression`](expression.md)
{ WHEN { [`expression`](expression.md) | [`conditionRightHandSide`](condition_right_hand_side.md) } [,...] THEN [`expression`](expression.md) } [...]
[ ELSE [`expression`](expression.md) ] END
```

Returns then expression from the first when clause where one of its operands was was evaluated to `TRUE` for the case expression. If there are no such clauses, returns else expression or `NULL` if it is absent.

Plain expressions are tested for equality with the case expression, `NULL` is not equal to `NULL`. Right sides of conditions are evaluated with the case expression on the left side.

## Example

```sql
CASE CNT WHEN IS NULL THEN 'Null' WHEN 0 THEN 'No' WHEN 1 THEN 'One' WHEN 2, 3 THEN 'Few' ELSE 'Some' END
```
