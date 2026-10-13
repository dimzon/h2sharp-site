# ALTER VIEW RENAME

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_view_rename) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER VIEW [ IF EXISTS ] [[`schemaName`](../grammar/name.md).][`viewName`](../grammar/name.md) RENAME TO [`newName`](../grammar/name.md)
```

🟢 includes non-standard H2 syntax

Renames a view. Schema owner rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
ALTER VIEW TEST RENAME TO MY_VIEW
```
