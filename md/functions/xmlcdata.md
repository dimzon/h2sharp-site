# XMLCDATA

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#xmlcdata) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
XMLCDATA([`valueString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Creates an `XML CDATA` element. If the value contains `]]>`, an XML text element is created instead. This method returns a string.

## Example

```sql
CALL XMLCDATA('data')
```
