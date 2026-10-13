# SET LAZY_QUERY_EXECUTION

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_lazy_query_execution) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET LAZY_QUERY_EXECUTION [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the lazy query execution mode. The values 0, 1 are supported.

If true, then large results are retrieved in chunks.

Note that not all queries support this feature, queries which do not are processed normally.

This command does not commit a transaction, and rollback does not affect it. This setting can be appended to the database URL: `jdbc:h2:./test;LAZY_QUERY_EXECUTION=1`

## Example

```sql
SET LAZY_QUERY_EXECUTION 1
```
