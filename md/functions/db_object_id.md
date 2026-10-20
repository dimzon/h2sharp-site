# DB_OBJECT_ID

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#db_object_id) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DB_OBJECT_ID({{'ROLE'|'SETTING'|'SCHEMA'|'USER'}, [`objectNameString`](../grammar/string.md)
| {'CONSTANT'|'CONSTRAINT'|'DOMAIN'|'INDEX'|'ROUTINE'|'SEQUENCE'
 |'SYNONYM'|'TABLE'|'TRIGGER'}, [`schemaNameString`](../grammar/string.md), [`objectNameString`](../grammar/string.md) })
```

🟢 includes non-standard H2 syntax

Returns internal identifier of the specified database object as integer value or `NULL` if object doesn't exist.

Admin rights are required to execute this function.

## Example

```sql
CALL DB_OBJECT_ID('ROLE', 'MANAGER');
CALL DB_OBJECT_ID('TABLE', 'PUBLIC', 'MY_TABLE');
```
