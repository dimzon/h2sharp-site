# SET DATABASE_EVENT_LISTENER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_database_event_listener) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET DATABASE_EVENT_LISTENER [`classNameString`](../grammar/string.md)
```

🟢 includes non-standard H2 syntax

Sets the event listener class. An empty string ('') means no listener should be used. This setting is not persistent.

Admin rights are required to execute this command, except if it is set when opening the database (in this case it is reset just after opening the database). This setting can be appended to the database URL: `jdbc:h2:./test;DATABASE_EVENT_LISTENER='sample.MyListener'`

## Example

```sql
SET DATABASE_EVENT_LISTENER 'sample.MyListener'
```
