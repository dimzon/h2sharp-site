# Referential Action

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#referential_action) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CASCADE | RESTRICT | NO ACTION | SET { DEFAULT | NULL }
```

The action `CASCADE` will cause conflicting rows in the referencing (child) table to be deleted or updated. `NO ACTION` is the default action, but because this database does not support deferred checking, `RESTRICT` and `NO ACTION` will both throw an exception immediately if the constraint is violated. The action `SET DEFAULT` will set the column in the referencing (child) table to the default value, while `SET NULL` will set it to `NULL`.

## Example

```sql
CASCADE
SET NULL
```
