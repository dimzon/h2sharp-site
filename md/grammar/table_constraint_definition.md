# Table Constraint Definition

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#table_constraint_definition) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[ [`constraintNameDefinition`](constraint_name_definition.md) ]
{ PRIMARY KEY [ HASH ] ( [`columnName`](name.md) [,...] ) }
| UNIQUE [ [`nullsDistinct`](nulls_distinct.md) ] ( { [`columnName`](name.md) [,...] | VALUE } )
| [`referentialConstraint`](referential_constraint.md)
| CHECK ([`condition`](condition.md))
```

🟢 includes non-standard H2 syntax

Defines a constraint.

`PRIMARY KEY` and `UNIQUE` require unique values. `PRIMARY KEY` also disallows `NULL` values and marks the column as a primary key, a table can have only one primary key. `UNIQUE` constraint supports `NULL` values and rows with `NULL` value in any column are considered as unique. `UNIQUE` constraint allows `NULL` values, if nulls distinct clause is not specified, the default is `NULLS DISTINCT`, excluding some compatibility modes. `UNIQUE` (`VALUE`) creates a unique constraint on entire row, excluding invisible columns; but if new columns will be added to the table, they will not be included into this constraint.

Referential constraint requires values that exist in other column(s) (usually in another table).

Check constraint requires a specified condition to return `TRUE` or `UNKNOWN` (`NULL`). It can reference columns of the table, and can reference objects that exist while the statement is executed. Conditions are only checked when a row is added or modified in the table where the constraint exists.

## Example

```sql
PRIMARY KEY(ID, NAME)
```
