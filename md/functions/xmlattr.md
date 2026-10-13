# XMLATTR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#xmlattr) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
XMLATTR([`nameString`](../grammar/string.md), [`valueString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Creates an XML attribute element of the form `name=value`. The value is encoded as XML text. This method returns a string.

## Example

```sql
CALL XMLNODE('a', XMLATTR('href', 'https://h2database.com'))
```
