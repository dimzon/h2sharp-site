# SET OPTIMIZE_REUSE_RESULTS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_optimize_reuse_results) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET OPTIMIZE_REUSE_RESULTS { 0 | 1 }
```

🟢 includes non-standard H2 syntax

Enabled (1) or disabled (0) the result reuse optimization. If enabled, subqueries and views used as subqueries are only re-run if the data in one of the tables was changed. This option is enabled by default.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting can be appended to the database URL: `jdbc:h2:./test;OPTIMIZE_REUSE_RESULTS=0`

## Example

```sql
SET OPTIMIZE_REUSE_RESULTS 0
```
