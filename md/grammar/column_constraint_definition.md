# Column Constraint Definition

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#column_constraint_definition) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[ [`constraintNameDefinition`](constraint_name_definition.md) ]
NOT NULL | PRIMARY KEY | UNIQUE [ [`nullsDistinct`](nulls_distinct.md) ] | [`referencesSpecification`](references_specification.md) | CHECK ([`condition`](condition.md))
```

`NOT NULL` disallows `NULL` value for a column.

`PRIMARY KEY` and `UNIQUE` require unique values. `PRIMARY KEY` also disallows `NULL` values and marks the column as a primary key. `UNIQUE` constraint allows `NULL` values, if nulls distinct clause is not specified, the default is `NULLS DISTINCT`, excluding some compatibility modes.

Referential constraint requires values that exist in other column (usually in another table).

Check constraint require a specified condition to return `TRUE` or `UNKNOWN` (`NULL`). It can reference columns of the table, and can reference objects that exist while the statement is executed. Conditions are only checked when a row is added or modified in the table where the constraint exists.

## Example

```sql
NOT NULL
PRIMARY KEY
UNIQUE
REFERENCES T2(ID)
CHECK (VALUE > 0)
```
