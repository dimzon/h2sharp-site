# DROP ALL OBJECTS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_all_objects) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP ALL OBJECTS [ DELETE FILES ]
```

🟢 includes non-standard H2 syntax

Drops all existing views, tables, sequences, schemas, function aliases, roles, user-defined aggregate functions, domains, and users (except the current user). If `DELETE FILES` is specified, the database files will be removed when the last user disconnects from the database. Warning: this command can not be rolled back.

Admin rights are required to execute this command.

## Example

```sql
DROP ALL OBJECTS
```
