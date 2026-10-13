# STRINGDECODE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#stringdecode) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
STRINGDECODE([`string`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Converts a encoded string using the Java string literal encoding format. Special characters are \b, \t, \n, \f, \r, \", \\, \<octal>, \u<unicode>. This method returns a string.

## Example

```sql
CALL STRINGENCODE(STRINGDECODE('Lines 1\nLine 2'))
```
