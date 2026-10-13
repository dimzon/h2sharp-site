# ALTER DOMAIN ADD CONSTRAINT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_domain_add_constraint) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER DOMAIN [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`domainName`](../grammar/name.md)
ADD [ [`constraintNameDefinition`](../grammar/constraint_name_definition.md) ]
CHECK ([`condition`](../grammar/condition.md)) [ CHECK | NOCHECK ]
```

🟢 includes non-standard H2 syntax

Adds a constraint to a domain. Schema owner rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
ALTER DOMAIN D ADD CONSTRAINT D_POSITIVE CHECK (VALUE > 0)
```
