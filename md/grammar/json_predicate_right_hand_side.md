# JSON Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#json_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
IS [ NOT ] JSON [ VALUE | ARRAY | OBJECT | SCALAR ]
 [ [ WITH | WITHOUT ] UNIQUE [ KEYS ] ]
```

Right side of `JSON` predicate.

Checks whether value of the specified string, binary data, or a `JSON` is a valid `JSON`. If `ARRAY, OBJECT`, or `SCALAR` is specified, only `JSON` items of the specified type are considered as valid. If `WITH UNIQUE [ KEYS ]` is specified only `JSON` with unique keys is considered as valid. This predicate isn't null-safe, it returns `UNKNOWN` if operand is `NULL`.

## Example

```sql
IS JSON OBJECT WITH UNIQUE KEYS
```
