# SET CLUSTER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_cluster) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET CLUSTER [`serverListString`](../grammar/string.md)
```

🟢 includes non-standard H2 syntax

This command should not be used directly by an application, the statement is executed automatically by the system. The behavior may change in future releases. Sets the cluster server list. An empty string switches off the cluster mode. Switching on the cluster mode requires admin rights, but any user can switch it off (this is automatically done when the client detects the other server is not responding).

This command is effective immediately, but does not commit an open transaction.

## Example

```sql
SET CLUSTER ''
```
