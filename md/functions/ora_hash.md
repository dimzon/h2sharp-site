# ORA_HASH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#ora_hash) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ORA_HASH([`expression`](../grammar/expression.md) [, [`bucketLong`](../grammar/long.md) [, [`seedLong`](../grammar/long.md)]])
```

🔴 compatibility-only syntax

Computes a hash value. Optional bucket argument determines the maximum returned value. This argument should be between 0 and 4294967295, default is 4294967295. Optional seed argument is combined with the given expression to return the different values for the same expression. This argument should be between 0 and 4294967295, default is 0. This method returns a long value between 0 and the specified or default bucket value inclusive.

## Example

```sql
ORA_HASH(A)
```
