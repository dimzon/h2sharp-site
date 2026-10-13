# JSON_ARRAY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#json_array) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
JSON_ARRAY(
[[`expression`](../grammar/expression.md) [,...]]|{([`query`](../grammar/query.md)) [FORMAT JSON]}
[ { NULL | ABSENT } ON NULL ]
)
```

Returns a `JSON` array constructed from the specified values or from the specified single-column subquery. If `NULL ON NULL` is specified `NULL` values are included in the array.

## Example

```sql
JSON_ARRAY(10, 15, 20);
JSON_ARRAY(JSON_DATA_A FORMAT JSON, JSON_DATA_B FORMAT JSON);
JSON_ARRAY((SELECT J FROM PROPS) FORMAT JSON);
```
