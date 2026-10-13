# SET THROTTLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_throttle) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET THROTTLE [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the throttle for the current connection. The value is the number of milliseconds delay after each 50 ms. The default value is 0 (throttling disabled).

This command does not commit a transaction, and rollback does not affect it. This setting can be appended to the database URL: `jdbc:h2:./test;THROTTLE=50`

## Example

```sql
SET THROTTLE 200
```
