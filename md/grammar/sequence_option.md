# Sequence option

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#sequence_option) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
START WITH [`long`](long.md)
| { RESTART WITH [`long`](long.md) }
| [`basicSequenceOption`](basic_sequence_option.md)
```

🟢 includes non-standard H2 syntax

Option of a sequence.

`START WITH` is used to set the initial value of the sequence. If initial value is not defined, `MINVALUE` for incrementing sequences and `MAXVALUE` for decrementing sequences is used.

`RESTART` is used to immediately restart the sequence with the specified value.

## Example

```sql
START WITH 10000
NO CACHE
```
