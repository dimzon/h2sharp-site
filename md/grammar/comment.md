# Comment

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#comment) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`bracketedComment`](bracketed_comment.md) | -- anything | // anything
```

🔴 compatibility-only syntax

Comments can be used anywhere in a command and are ignored by the database. Line comments `--` and `//` end with a newline.

## Example

```sql
-- comment
/* comment */
```
