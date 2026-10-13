# Quantified Distinct Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#quantified_distinct_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
IS [ NOT ] [ DISTINCT FROM ] { ALL | ANY | SOME } ( { [`query`](query.md) | [`array`](array.md) } )
```

🟢 includes non-standard H2 syntax

Right side of quantified distinct predicate.

Quantified distinct predicate is null-safe, meaning `NULL` is considered the same as `NULL`, and the condition never evaluates to `UNKNOWN`.

Quantified distinct predicate `ALL` returns `TRUE` if specified distinct predicate between left size of condition and each row from a subquery or each element of array returns `TRUE`, including case when there are no rows. Otherwise it returns `FALSE`.

Quantified distinct predicates `ANY` and `SOME` return `TRUE` if specified distinct predicate between left size of condition and at least one row from a subquery or at least one element of array returns `TRUE`. Otherwise they return `FALSE`.

Note that these predicates have priority over `ANY` and `SOME` aggregate functions with subquery on the right side. Use parentheses around aggregate function.

If version with array is required and this array is returned from a subquery, wrap this subquery with a cast to distinguish this operation from quantified comparison predicate with a query.

## Example

```sql
IS DISTINCT FROM ALL(SELECT V FROM TEST)
IS NOT DISTINCT FROM ANY(ARRAY_COLUMN)
IS NOT DISTINCT FROM ANY(CAST((SELECT ARRAY_COLUMN FROM OTHER_TABLE WHERE ID = 5) AS INTEGER ARRAY)
```
