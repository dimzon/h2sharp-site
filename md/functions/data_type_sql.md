# DATA_TYPE_SQL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#data_type_sql) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DATA_TYPE_SQL
([`objectSchemaString`](../grammar/string.md), [`objectNameString`](../grammar/string.md), [`objectTypeString`](../grammar/string.md), [`typeIdentifierString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Returns SQL representation of data type of the specified constant, domain, table column, routine result or argument.

For constants object type is '`CONSTANT`' and type identifier is the value of `INFORMATION_SCHEMA.CONSTANTS.DTD_IDENTIFIER`.

For domains object type is '`DOMAIN`' and type identifier is the value of `INFORMATION_SCHEMA.DOMAINS.DTD_IDENTIFIER`.

For columns object type is '`TABLE`' and type identifier is the value of `INFORMATION_SCHEMA.COLUMNS.DTD_IDENTIFIER`.

For routines object name is the value of `INFORMATION_SCHEMA.ROUTINES.SPECIFIC_NAME`, object type is '`ROUTINE`', and type identifier is the value of `INFORMATION_SCHEMA.ROUTINES.DTD_IDENTIFIER` for data type of the result and the value of `INFORMATION_SCHEMA.PARAMETERS.DTD_IDENTIFIER` for data types of arguments. Aggregate functions aren't supported by this function, because their data type isn't statically known.

This function returns `NULL` if any argument is `NULL`, object type is not valid, or object isn't found.

## Example

```sql
DATA_TYPE_SQL('PUBLIC', 'C', 'CONSTANT', 'TYPE')
DATA_TYPE_SQL('PUBLIC', 'D', 'DOMAIN', 'TYPE')
DATA_TYPE_SQL('PUBLIC', 'T', 'TABLE', '1')
DATA_TYPE_SQL('PUBLIC', 'R_1', 'ROUTINE', 'RESULT')
DATA_TYPE_SQL('PUBLIC', 'R_1', 'ROUTINE', '1')
COALESCE(
    QUOTE_IDENT(DOMAIN_SCHEMA) || '.' || QUOTE_IDENT(DOMAIN_NAME),
    DATA_TYPE_SQL(TABLE_SCHEMA, TABLE_NAME, 'TABLE', DTD_IDENTIFIER))
```
