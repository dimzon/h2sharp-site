# LOCK_MODE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#lock_mode) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
LOCK_MODE()
```

🟢 includes non-standard H2 syntax

Returns the current lock mode. See `SET LOCK_MODE`. This method returns an int.

## Example

```sql
CALL LOCK_MODE();
```
