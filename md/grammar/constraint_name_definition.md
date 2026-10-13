# Constraint Name Definition

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#constraint_name_definition) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CONSTRAINT [ IF NOT EXISTS ] [`newConstraintName`](name.md)
```

🟢 includes non-standard H2 syntax

Defines a constraint name.

## Example

```sql
CONSTRAINT CONST_ID
```
