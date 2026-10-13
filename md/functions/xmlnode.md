# XMLNODE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#xmlnode) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
XMLNODE([`elementString`](../grammar/string.md) [, [`attributesString`](../grammar/string.md) [, [`contentString`](../grammar/string.md) [, [`indentBoolean`](../grammar/boolean.md)]]])
```

🟢 includes non-standard H2 syntax

Create an XML node element. An empty or null attribute string means no attributes are set. An empty or null content string means the node is empty. The content is indented by default if it contains a newline. This method returns a string.

## Example

```sql
CALL XMLNODE('a', XMLATTR('href', 'https://h2database.com'), 'H2')
```
