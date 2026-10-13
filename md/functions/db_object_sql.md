# DB_OBJECT_SQL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#db_object_sql) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DB_OBJECT_SQL({{'ROLE'|'SETTING'|'SCHEMA'|'USER'}, [`objectNameString`](../grammar/string.md)
| {'CONSTANT'|'CONSTRAINT'|'DOMAIN'|'INDEX'|'ROUTINE'|'SEQUENCE'
    |'SYNONYM'|'TABLE'|'TRIGGER'}, [`schemaNameString`](../grammar/string.md), [`objectNameString`](../grammar/string.md) })
```

🟢 includes non-standard H2 syntax

Returns internal SQL definition of the specified database object or `NULL` if object doesn't exist or it is a system object without SQL definition.

This function should not be used to analyze structure of the object by machine code. Internal SQL representation may contain undocumented non-standard clauses and may be different in different versions of H2. Objects are described in the `INFORMATION_SCHEMA` in machine-readable way.

Admin rights are required to execute this function.

## Example

```sql
CALL DB_OBJECT_SQL('ROLE', 'MANAGER');
CALL DB_OBJECT_SQL('TABLE', 'PUBLIC', 'MY_TABLE');
```
