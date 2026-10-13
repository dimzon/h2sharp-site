# CREATE DOMAIN

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_domain) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE DOMAIN [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`domainName`](../grammar/name.md)
[ AS ] [`dataTypeOrDomain`](../grammar/data_type_or_domain.md)
[ DEFAULT [`expression`](../grammar/expression.md) ]
[ ON UPDATE [`expression`](../grammar/expression.md) ]
[ COMMENT [`expression`](../grammar/expression.md) ]
[ CHECK ([`condition`](../grammar/condition.md)) ] [...]
```

🟢 includes non-standard H2 syntax

Creates a new domain to define a set of permissible values. Schema owner rights are required to execute this command. Domains can be used as data types. The domain constraints must evaluate to `TRUE` or to `UNKNOWN`. In the conditions, the term `VALUE` refers to the value being tested.

This command commits an open transaction in this connection.

## Example

```sql
CREATE DOMAIN EMAIL AS VARCHAR(255) CHECK (POSITION('@', VALUE) > 1)
```
