# JSON_OBJECT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#json_object) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
JSON_OBJECT(
[{{[KEY] [`string`](../grammar/string.md) VALUE [`expression`](../grammar/expression.md)} | {[`string`](../grammar/string.md) : [`expression`](../grammar/expression.md)}} [,...] ]
[ { NULL | ABSENT } ON NULL ]
[ { WITH | WITHOUT } UNIQUE KEYS ]
)
```

Returns a `JSON` object constructed from the specified properties. If `ABSENT ON NULL` is specified properties with `NULL` value are not included in the object. If `WITH UNIQUE KEYS` is specified the constructed object is checked for uniqueness of keys, nested objects, if any, are checked too.

## Example

```sql
JSON_OBJECT('id': 100, 'name': 'Joe', 'groups': '[2,5]' FORMAT JSON);
```
