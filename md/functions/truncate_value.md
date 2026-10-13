# TRUNCATE_VALUE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#truncate_value) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TRUNCATE_VALUE([`value`](../grammar/value.md), [`precisionInt`](../grammar/int.md), [`forceBoolean`](../grammar/boolean.md))
```

🟢 includes non-standard H2 syntax

Truncate a value to the required precision. If force flag is set to `FALSE` fixed precision values are not truncated. The method returns a value with the same data type as the first parameter.

## Example

```sql
CALL TRUNCATE_VALUE(X, 10, TRUE);
```
