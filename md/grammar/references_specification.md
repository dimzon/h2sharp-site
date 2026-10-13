# References Specification

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#references_specification) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REFERENCES [ [`refTableName`](name.md) ] [ ( [`refColumnName`](name.md) [,...] ) ]
[ [`referentialTriggeredAction`](referential_triggered_action.md) ]
```

Defines a referential specification of a referential constraint. If the table name is not specified, then the same table is referenced. `NO ACTION` is the default action, but currently it works like stricter `RESTRICT`. If the referenced columns are not specified, then the primary key columns are used. Referential constraint requires an existing unique or primary key constraint on referenced columns, this constraint must include all referenced columns in any order and must not include any other columns. Some tables may not be referenced, such as metadata tables.

## Example

```sql
REFERENCES TEST(ID)
```
