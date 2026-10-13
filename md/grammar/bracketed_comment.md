# Bracketed comment

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#bracketed_comment) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
/* [ [ [`bracketedComment`](bracketed_comment.md) ] [ anything ] [...] ] */
```

Comments can be used anywhere in a command and are ignored by the database. Bracketed comments `/* */` can be nested and can be multiple lines long.

## Example

```sql
/* comment */
/* comment /* nested comment */ comment */
```
