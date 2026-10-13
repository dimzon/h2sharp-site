# SET QUERY_TIMEOUT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_query_timeout) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET QUERY_TIMEOUT [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Set the query timeout of the current session to the given value. The timeout is in milliseconds. All kinds of statements will throw an exception if they take longer than the given value. The default timeout is 0, meaning no timeout.

This command does not commit a transaction, and rollback does not affect it.

## Example

```sql
SET QUERY_TIMEOUT 10000
```
