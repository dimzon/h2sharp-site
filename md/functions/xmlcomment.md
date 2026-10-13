# XMLCOMMENT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#xmlcomment) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
XMLCOMMENT([`commentString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Creates an XML comment. Two dashes (`--`) are converted to `- -`. This method returns a string.

## Example

```sql
CALL XMLCOMMENT('Test')
```
