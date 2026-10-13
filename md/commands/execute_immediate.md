# EXECUTE IMMEDIATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#execute_immediate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
EXECUTE IMMEDIATE [`sqlString`](../grammar/string.md)
```

Dynamically prepares and executes the SQL command specified as a string. Query commands may not be used.

## Example

```sql
EXECUTE IMMEDIATE 'ALTER TABLE TEST DROP CONSTRAINT ' ||
    QUOTE_IDENT((SELECT CONSTRAINT_NAME
        FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
        WHERE TABLE_SCHEMA = 'PUBLIC' AND TABLE_NAME = 'TEST'
            AND CONSTRAINT_TYPE = 'UNIQUE'));
```
