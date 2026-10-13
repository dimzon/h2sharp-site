# SET AUTOCOMMIT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_autocommit) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET AUTOCOMMIT { TRUE | ON | FALSE | OFF }
```

🟢 includes non-standard H2 syntax

Switches auto commit on or off. This setting can be appended to the database URL: `jdbc:h2:./test;AUTOCOMMIT=OFF` - however this will not work as expected when using a connection pool (the connection pool manager will re-enable autocommit when returning the connection to the pool, so autocommit will only be disabled the first time the connection is used.

## Example

```sql
SET AUTOCOMMIT OFF
```
