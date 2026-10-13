# Case expression

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#case_expression) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`simpleCase`](simple_case.md) | [`searchedCase`](searched_case.md)
```

Performs conditional evaluation of expressions.

## Example

```sql
CASE A WHEN 'a' THEN 1 ELSE 2 END
CASE WHEN V > 10 THEN 1 WHEN V < 0 THEN 2 END
CASE WHEN A IS NULL THEN 'Null' ELSE 'Not null' END
```
