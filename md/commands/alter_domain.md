# ALTER DOMAIN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_domain) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER DOMAIN [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`domainName`](../grammar/name.md)
{ SET DEFAULT [`expression`](../grammar/expression.md) }
| { DROP DEFAULT }
| { SET ON UPDATE [`expression`](../grammar/expression.md) }
| { DROP ON UPDATE }
```

🟢 includes non-standard H2 syntax

Changes the default or on update expression of a domain. Schema owner rights are required to execute this command.

`SET DEFAULT` changes the default expression of a domain.

`DROP DEFAULT` removes the default expression of a domain. Old expression is copied into domains and columns that use this domain and don't have an own default expression.

`SET ON UPDATE` changes the expression that is set on update if value for this domain is not specified in update statement.

`DROP ON UPDATE` removes the expression that is set on update of a column with this domain. Old expression is copied into domains and columns that use this domain and don't have an own on update expression.

This command commits an open transaction in this connection.

## Example

```sql
ALTER DOMAIN D1 SET DEFAULT '';
ALTER DOMAIN D1 DROP DEFAULT;
ALTER DOMAIN D1 SET ON UPDATE CURRENT_TIMESTAMP;
ALTER DOMAIN D1 DROP ON UPDATE;
```
