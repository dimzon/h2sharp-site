# Timezone second field

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#timezone_second_field) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TIMEZONE_SECOND
```

🟢 includes non-standard H2 syntax

Timezone second (from -59 to +59). Local mean time (`LMT`) used in the past may have offsets with seconds. Standard time doesn't use such offsets.

## Example

```sql
TIMEZONE_SECOND
```
