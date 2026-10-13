# Referential Constraint

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#referential_constraint) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
FOREIGN KEY ( [`columnName`](name.md) [,...] ) [`referencesSpecification`](references_specification.md)
```

Defines a referential constraint.

## Example

```sql
FOREIGN KEY(ID) REFERENCES TEST(ID)
```
