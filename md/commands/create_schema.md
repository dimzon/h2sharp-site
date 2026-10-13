# CREATE SCHEMA

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_schema) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE SCHEMA [ IF NOT EXISTS ]
{ [`name`](../grammar/name.md) [ AUTHORIZATION [`ownerName`](../grammar/name.md) ] | [ AUTHORIZATION [`ownerName`](../grammar/name.md) ] }
[ WITH [`tableEngineParamName`](../grammar/name.md) [,...] ]
```

🟢 includes non-standard H2 syntax

Creates a new schema. Schema admin rights are required to execute this command.

If schema name is not specified, the owner name is used as a schema name. If schema name is specified, but no owner is specified, the current user is used as an owner.

Schema owners can create, rename, and drop objects in the schema. Schema owners can drop the schema itself, but cannot rename it. Some objects may still require admin rights for their creation, see documentation of their `CREATE` statements for details.

Optional table engine parameters are used when `CREATE TABLE` command is run on this schema without having its engine params set.

This command commits an open transaction in this connection.

## Example

```sql
CREATE SCHEMA TEST_SCHEMA AUTHORIZATION SA
```
