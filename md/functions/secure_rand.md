# SECURE_RAND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#secure_rand) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SECURE_RAND([`int`](../grammar/int.md))
```

🟢 includes non-standard H2 syntax

Generates a number of cryptographically secure random numbers. This method returns bytes.

## Example

```sql
CALL SECURE_RAND(16)
```
