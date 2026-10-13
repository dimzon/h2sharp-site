# DROP DOMAIN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#drop_domain) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DROP DOMAIN [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`domainName`](../grammar/name.md) [ RESTRICT | CASCADE ]
```

🟢 includes non-standard H2 syntax

Drops a data type (domain). Schema owner rights are required to execute this command.

The command will fail if it is referenced by a column or another domain (the default). Column descriptors are replaced with original definition of specified domain if the `CASCADE` clause is used. Default and on update expressions are copied into domains and columns that use this domain and don't have own expressions. Domain constraints are copied into domains that use this domain and to columns (as check constraints) that use this domain. This command commits an open transaction in this connection.

## Example

```sql
DROP DOMAIN EMAIL
```
