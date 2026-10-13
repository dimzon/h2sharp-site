# ABORT_SESSION

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#abort_session) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ABORT_SESSION([`sessionInt`](../grammar/int.md))
```

🟢 includes non-standard H2 syntax

Cancels the currently executing statement of another session. Closes the session and releases the allocated resources. Returns true if the session was closed, false if no session with the given id was found.

If a client was connected while its session was aborted it will see an error.

Admin rights are required to execute this command.

## Example

```sql
CALL ABORT_SESSION(3)
```
