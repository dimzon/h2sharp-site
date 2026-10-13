# Window frame preceding

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#window_frame_preceding) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
UNBOUNDED PRECEDING|[`value`](value.md) PRECEDING|CURRENT ROW
```

A window frame preceding clause. If value is specified it should not be negative.

## Example

```sql
UNBOUNDED PRECEDING
1 PRECEDING
CURRENT ROW
```
