# SESSION_ID

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#session_id) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SESSION_ID()
```

🟢 includes non-standard H2 syntax

Returns the unique session id number for the current database connection. This id stays the same while the connection is open. This method returns an int. The database engine may re-use a session id after the connection is closed.

## Example

```sql
CALL SESSION_ID()
```
