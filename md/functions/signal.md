# SIGNAL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#signal) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SIGNAL([`sqlStateString`](../grammar/string.md), [`messageString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Throw an `SQLException` with the passed `SQLState` and reason.

## Example

```sql
CALL SIGNAL('23505', 'Duplicate user ID: ' || user_id);
```
