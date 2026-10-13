# Exact numeric

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#exact_numeric) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[ + | - ] { { [`number`](number.md) [ . [`number`](number.md) ] } | { . [`number`](number.md) } }
```

An exact numeric value. Exact numeric values with dot have [NUMERIC](../datatypes/numeric_type.md) data type, values without dot small enough to fit into [INTEGER](../datatypes/integer_type.md) data type have this type, larger values small enough to fit into [BIGINT](../datatypes/bigint_type.md) data type have this type, others also have `NUMERIC` data type.

## Example

```sql
-1600.05
134_518.235_114
```
