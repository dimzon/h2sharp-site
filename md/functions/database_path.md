# DATABASE_PATH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#database_path) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DATABASE_PATH()
```

🟢 includes non-standard H2 syntax

Returns the directory of the database files and the database name, if it is file based. Returns `NULL` otherwise.

## Example

```sql
CALL DATABASE_PATH();
```
