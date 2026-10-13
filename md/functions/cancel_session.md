# CANCEL_SESSION

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#cancel_session) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CANCEL_SESSION([`sessionInt`](../grammar/int.md))
```

🟢 includes non-standard H2 syntax

Cancels the currently executing statement of another session. Returns true if the statement was canceled, false if the session is closed or no statement is currently executing.

Admin rights are required to execute this command.

## Example

```sql
CANCEL_SESSION(3)
```
