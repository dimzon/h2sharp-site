# MEMORY_FREE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#memory_free) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
MEMORY_FREE()
```

🟢 includes non-standard H2 syntax

Returns the free memory in KB (where 1024 bytes is a KB). This method returns a long. The garbage collector is run before returning the value. Admin rights are required to execute this command.

## Example

```sql
MEMORY_FREE()
```
