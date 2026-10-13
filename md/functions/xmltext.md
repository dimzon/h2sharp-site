# XMLTEXT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#xmltext) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
XMLTEXT([`valueString`](../grammar/string.md) [, [`escapeNewlineBoolean`](../grammar/boolean.md)])
```

🟢 includes non-standard H2 syntax

Creates an XML text element. If enabled, newline and linefeed is converted to an XML entity (&#). This method returns a string.

## Example

```sql
CALL XMLTEXT('test')
```
