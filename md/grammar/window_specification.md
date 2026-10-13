# Window specification

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#window_specification) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
([[`existingWindowName`](name.md)]
[PARTITION BY [`expression`](expression.md) [,...]] [ORDER BY [`sortSpecificationList`](sort_specification_list.md)]
[[`windowFrame`](window_frame.md)])
```

A window specification for a window, window function or aggregate.

If name of an existing window is specified its clauses are used by default.

Optional window partition clause separates rows into independent partitions. Each partition is processed separately. If this clause is not present there is one implicit partition with all rows.

Optional window order clause specifies order of rows in the partition. If some rows have the same order position they are considered as a group of rows in optional window frame clause.

Optional window frame clause specifies which rows are processed by a window function, see its documentation for a more details.

## Example

```sql
()
(W1 ORDER BY ID)
(PARTITION BY CATEGORY)
(PARTITION BY CATEGORY ORDER BY NAME, ID)
(ORDER BY Y RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES)
```
