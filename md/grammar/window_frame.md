# Window frame

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#window_frame) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ROWS|RANGE|GROUP
{[`windowFramePreceding`](window_frame_preceding.md)|BETWEEN [`windowFrameBound`](window_frame_bound.md) AND [`windowFrameBound`](window_frame_bound.md)}
[EXCLUDE {CURRENT ROW|GROUP|TIES|NO OTHERS}]
```

A window frame clause. May be specified only for aggregates and `FIRST_VALUE`(), `LAST_VALUE`(), and `NTH_VALUE`() window functions.

If this clause is not specified for an aggregate or window function that supports this clause the default window frame depends on window order clause. If window order clause is also not specified the default window frame contains all the rows in the partition. If window order clause is specified the default window frame contains all preceding rows and all rows from the current group.

Window frame unit determines how rows or groups of rows are selected and counted. If `ROWS` is specified rows are not grouped in any way and relative numbers of rows are used in bounds. If `RANGE` is specified rows are grouped according window order clause, preceding and following values mean the difference between value in the current row and in the target rows, and `CURRENT ROW` in bound specification means current group of rows. If `GROUPS` is specified rows are grouped according window order clause, preceding and following values means relative number of groups of rows, and `CURRENT ROW` in bound specification means current group of rows.

If only window frame preceding clause is specified it is treated as `BETWEEN` windowFramePreceding `AND CURRENT ROW`.

Optional window frame exclusion clause specifies rows that should be excluded from the frame. `EXCLUDE CURRENT ROW` excludes only the current row regardless the window frame unit. `EXCLUDE GROUP` excludes the whole current group of rows, including the current row. `EXCLUDE TIES` excludes the current group of rows, but not the current row. `EXCLUDE NO OTHERS` is default and it does not exclude anything.

## Example

```sql
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES
```
