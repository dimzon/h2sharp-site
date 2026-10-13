# Type Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#type_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
IS [ NOT ] OF ([`dataType`](data_type.md) [,...])
```

Right side of type predicate.

Checks whether the data type of the specified operand is one of the specified data types. Some data types have multiple names, these names are considered as equal here. Domains and their base data types are currently not distinguished from each other. Precision and scale are also ignored. If operand is `NULL`, the result is `UNKNOWN`.

## Example

```sql
IS OF (INTEGER, BIGINT)
```
