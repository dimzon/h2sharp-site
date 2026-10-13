# TRANSLATE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#translate) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
TRANSLATE([`value`](../grammar/value.md), [`searchString`](../grammar/string.md), [`replacementString`](../grammar/string.md))
```

🔴 compatibility-only syntax

Oracle-compatible `TRANSLATE` function that replaces a sequence of characters in a string with another set of characters.

## Example

```sql
CALL TRANSLATE('Hello world', 'eo', 'EO')
```
