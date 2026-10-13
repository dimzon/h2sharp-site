# HASH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#hash) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
HASH([`algorithmString`](../grammar/string.md), [`expression`](../grammar/expression.md) [, [`iterationInt`](../grammar/int.md)])
```

🟢 includes non-standard H2 syntax

Calculate the hash value using an algorithm, and repeat this process for a number of iterations.

This function supports `MD5, SHA`-1, `SHA`-224, `SHA`-256, `SHA`-384, `SHA`-512, `SHA3`-224, `SHA3`-256, `SHA3`-384, and `SHA3`-512 algorithms. `SHA`-224, `SHA`-384, and `SHA`-512 may be unavailable in some `JREs`.

`MD5` and `SHA`-1 algorithms should not be considered as secure.

If this function is used to encrypt a password, a random salt should be concatenated with a password and this salt and result of the function should be stored to prevent a rainbow table attack and number of iterations should be large enough to slow down a dictionary or a brute force attack.

This method returns bytes.

## Example

```sql
CALL HASH('SHA-256', 'Text', 1000)
CALL HASH('SHA3-256', X'0102')
```
