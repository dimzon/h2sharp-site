# TRANSACTION_ID

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#transaction_id) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TRANSACTION_ID()
```

🟢 includes non-standard H2 syntax

Returns the current transaction id for this session. This method returns `NULL` if there is no uncommitted change, or if the database is not persisted. Otherwise a value of the following form is returned: `logFileId-position-sessionId`. This method returns a string. The value is unique across database restarts (values are not re-used).

## Example

```sql
CALL TRANSACTION_ID()
```
