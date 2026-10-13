# Compare

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#compare) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
<> | <= | >= | = | < | > | { != } | &&
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Comparison operator. The operator != is the same as <>. The operator `&&` means overlapping; it can only be used with geometry types.

## Example

```sql
<>
```
