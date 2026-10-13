# Like Predicate Right Hand Side

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#like_predicate_right_hand_side) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[ NOT ] { LIKE | { ILIKE } } [`operand`](operand.md) [ ESCAPE [`string`](string.md) ]
```

🟢 includes non-standard H2 syntax

Right side of like predicate.

The wildcards characters are `_` (any one character) and `%` (any characters). The database uses an index when comparing with `LIKE` except if the operand starts with a wildcard. To search for the characters `%` and `_`, the characters need to be escaped. The default escape character is `\` (backslash). To select no escape character, use `ESCAPE ''` (empty string). At most one escape character is allowed. Each character that follows the escape character in the pattern needs to match exactly. Patterns that end with an escape character are invalid and the expression returns `NULL`.

`ILIKE` does a case-insensitive compare.

## Example

```sql
LIKE 'a%'
```
