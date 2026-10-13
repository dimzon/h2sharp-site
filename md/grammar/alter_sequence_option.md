# Alter sequence option

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#alter_sequence_option) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ START WITH [`long`](long.md) }
| RESTART [ WITH [`long`](long.md) ]
| [`basicSequenceOption`](basic_sequence_option.md)
```

🟢 includes non-standard H2 syntax

Option of a sequence.

`START WITH` is used to change the initial value of the sequence. It does not affect the current value of the sequence, it only changes the preserved initial value that is used for simple `RESTART` without a value.

`RESTART` is used to restart the sequence from its initial value or with the specified value.

## Example

```sql
START WITH 10000
NO CACHE
```
