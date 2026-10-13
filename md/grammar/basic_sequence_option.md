# Basic sequence option

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#basic_sequence_option) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
INCREMENT BY [`long`](long.md)
| MINVALUE [`long`](long.md) | NO MINVALUE | { NOMINVALUE }
| MAXVALUE [`long`](long.md) | NO MAXVALUE | { NOMAXVALUE }
| CYCLE | NO CYCLE | { EXHAUSTED } | { NOCYCLE }
| { CACHE [`long`](long.md) } | { NO CACHE } | { NOCACHE }
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Basic option of a sequence.

`INCREMENT BY` specifies the step of the sequence, may be positive or negative, but may not be zero. The default is 1.

`MINVALUE` and `MAXVALUE` specify the bounds of the sequence.

Sequences with `CYCLE` option start the generation again from `MINVALUE` (incrementing sequences) or `MAXVALUE` (decrementing sequences) instead of exhausting with an error. Sequences with `EXHAUSTED` option can't return values until they will be restarted.

The `CACHE` option sets the number of pre-allocated numbers. If the system crashes without closing the database, at most this many numbers are lost. The default cache size is 32 if sequence has enough range of values. `NO CACHE` option or the cache size 1 or lower disable the cache. If `CACHE` option is specified, it cannot be larger than the total number of values that sequence can produce within a cycle.

## Example

```sql
MAXVALUE 100000
CYCLE
NO CACHE
```
