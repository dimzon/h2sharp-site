# CREATE VIEW

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_view) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE [ OR REPLACE ] [ FORCE ]
VIEW [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`viewName`](../grammar/name.md)
[ ( [`columnName`](../grammar/name.md) [,...] ) ] AS [`query`](../grammar/query.md)
```

🟢 includes non-standard H2 syntax

Creates a new view. If the force option is used, then the view is created even if the underlying table(s) don't exist. Schema owner rights are required to execute this command.

If the `OR REPLACE` clause is used an existing view will be replaced, and any dependent views will not need to be recreated. If dependent views will become invalid as a result of the change an error will be generated, but this error can be ignored if the `FORCE` clause is also used.

Views are not updatable except when using 'instead of' triggers.

This command commits an open transaction in this connection.

## Example

```sql
CREATE VIEW TEST_VIEW AS SELECT * FROM TEST WHERE ID < 100
```
