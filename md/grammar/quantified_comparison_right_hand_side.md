# Quantified Comparison Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#quantified_comparison_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`compare`](compare.md) { ALL | ANY | SOME } ( { [`query`](query.md) | { [`array`](array.md) } } )
```

🟢 includes non-standard H2 syntax

Right side of quantified comparison predicates.

Quantified comparison predicate `ALL` returns `TRUE` if specified comparison operation between left size of condition and each row from a subquery or each element of array returns `TRUE`, including case when there are no rows (elements). `ALL` predicate returns `FALSE` if at least one such comparison returns `FALSE`. Otherwise it returns `UNKNOWN`.

Quantified comparison predicates `ANY` and `SOME` return `TRUE` if specified comparison operation between left size of condition and at least one row from a subquery or at least one element of array returns `TRUE`. `ANY` and `SOME` predicates return `FALSE` if all such comparisons return `FALSE`. Otherwise they return `UNKNOWN`.

Note that these predicates have priority over `ANY` and `SOME` aggregate functions with subquery on the right side. Use parentheses around aggregate function.

If version with array is required and this array is returned from a subquery, wrap this subquery with a cast to distinguish this operation from standard quantified comparison predicate with a query.

## Example

```sql
< ALL(SELECT V FROM TEST)
= ANY(ARRAY_COLUMN)
= ANY(CAST((SELECT ARRAY_COLUMN FROM OTHER_TABLE WHERE ID = 5) AS INTEGER ARRAY)
```
