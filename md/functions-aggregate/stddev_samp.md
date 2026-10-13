# STDDEV_SAMP

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#stddev_samp) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
STDDEV_SAMP( [ DISTINCT|ALL ] [`numeric`](../grammar/numeric.md) )
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

The sample standard deviation. This method returns a double. If less than two rows are selected, the result is `NULL`. Aggregates are only allowed in select statements.

## Example

```sql
STDDEV(X)
```
