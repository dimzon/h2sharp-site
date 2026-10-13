# JSON_OBJECTAGG

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions-aggregate.html#json_objectagg) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
JSON_OBJECTAGG(
{[KEY] [`string`](../grammar/string.md) VALUE [`value`](../grammar/value.md)} | {[`string`](../grammar/string.md) : [`value`](../grammar/value.md)}
[ { NULL | ABSENT } ON NULL ]
[ { WITH | WITHOUT } UNIQUE KEYS ]
)
[FILTER (WHERE [`expression`](../grammar/expression.md))] [OVER [`windowNameOrSpecification`](../grammar/window_name_or_specification.md)]
```

Aggregates the keys with values into a `JSON` object. If `ABSENT ON NULL` is specified properties with `NULL` value are not included in the object. If `WITH UNIQUE KEYS` is specified the constructed object is checked for uniqueness of keys, nested objects, if any, are checked too. If no values are selected, the result is `SQL NULL` value.

## Example

```sql
JSON_OBJECTAGG(NAME: VAL);
JSON_OBJECTAGG(KEY NAME VALUE VAL);
```
