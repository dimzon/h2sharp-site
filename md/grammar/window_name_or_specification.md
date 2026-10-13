# Window name or specification

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#window_name_or_specification) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`windowName`](name.md) | [`windowSpecification`](window_specification.md)
```

A window name or inline specification for a window function or aggregate.

Window functions in H2 may require a lot of memory for large queries.

## Example

```sql
W1
(ORDER BY ID)
```
