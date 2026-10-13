# Within group specification

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#within_group_specification) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
WITHIN GROUP (ORDER BY [`sortSpecificationList`](sort_specification_list.md))
```

Group specification for ordered set functions.

## Example

```sql
WITHIN GROUP (ORDER BY ID DESC)
```
