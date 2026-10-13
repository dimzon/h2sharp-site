# COMMENT ON

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#comment_on) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
COMMENT ON
{ { COLUMN [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md).[`columnName`](../grammar/name.md) }
| { { TABLE | VIEW | CONSTANT | CONSTRAINT | ALIAS | INDEX | ROLE
| SCHEMA | SEQUENCE | TRIGGER | USER | DOMAIN } [[`schemaName`](../grammar/name.md).][`objectName`](../grammar/name.md) } }
IS [`expression`](../grammar/expression.md)
```

🟢 includes non-standard H2 syntax

Sets the comment of a database object. Use `NULL` or empty string to remove the comment.

Admin rights are required to execute this command if object is a `USER` or `ROLE`. Schema owner rights are required to execute this command for all other types of objects. This command commits an open transaction in this connection.

## Example

```sql
COMMENT ON TABLE TEST IS 'Table used for testing'
```
