# Name

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#name) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ { A-Z|_ } [ { A-Z|_|0-9 } [...] ] } | [`quotedName`](quoted_name.md)
```

With default settings unquoted names are converted to upper case. The maximum name length is 256 characters.

Identifiers in H2 are case sensitive by default. Because unquoted names are converted to upper case, they can be written in any case anyway. When both quoted and unquoted names are used for the same identifier the quoted names must be written in upper case. Identifiers with lowercase characters can be written only as a quoted name, they aren't accessible with unquoted names.

If `DATABASE_TO_UPPER` setting is set to `FALSE` the unquoted names aren't converted to upper case.

If `DATABASE_TO_LOWER` setting is set to `TRUE` the unquoted names are converted to lower case instead.

If `CASE_INSENSITIVE_IDENTIFIERS` setting is set to `TRUE` all identifiers are case insensitive.

## Example

```sql
TEST
```
