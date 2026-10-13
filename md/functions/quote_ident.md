# QUOTE_IDENT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#quote_ident) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
QUOTE_IDENT([`string`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Quotes the specified identifier. Identifier is surrounded by double quotes. If identifier contains double quotes they are repeated twice.

## Example

```sql
QUOTE_IDENT('Column 1')
```
