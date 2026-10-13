# CONVERT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#convert) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CONVERT([`value`](../grammar/value.md), [`dataTypeOrDomain`](../grammar/data_type_or_domain.md))
```

🔴 compatibility-only syntax

Converts a value to another data type.

This function is deprecated, use [CAST](../grammar/cast_specification.md) instead of it.

## Example

```sql
CONVERT(NAME, INT)
```
