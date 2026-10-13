# RAND

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#rand) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ RAND | RANDOM } ( [ [`int`](../grammar/int.md) ] )
```

🟢 includes non-standard H2 syntax

Calling the function without parameter returns the next a pseudo random number. Calling it with an parameter seeds the session's random number generator. This method returns a double between 0 (including) and 1 (excluding).

## Example

```sql
RAND()
```
