# LINK_SCHEMA

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#link_schema) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LINK_SCHEMA ([`targetSchemaString`](../grammar/string.md), [`driverString`](../grammar/string.md), [`urlString`](../grammar/string.md),
[`userString`](../grammar/string.md), [`passwordString`](../grammar/string.md), [`sourceSchemaString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Creates table links for all tables in a schema. If tables with the same name already exist, they are dropped first. The target schema is created automatically if it does not yet exist. The driver name may be empty if the driver is already loaded. The list of tables linked is returned in the form of a result set. Admin rights are required to execute this command.

## Example

```sql
SELECT * FROM LINK_SCHEMA('TEST2', '', 'jdbc:h2:./test2', 'sa', 'sa', 'PUBLIC');
```
