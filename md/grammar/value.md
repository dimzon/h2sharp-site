# Value

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#value) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`string`](string.md) | { [`dollarQuotedString`](dollar_quoted_string.md) } | [`numeric`](numeric.md) | [`dateAndTime`](date_and_time.md) | [`boolean`](boolean.md) | [`bytes`](bytes.md)
| [`interval`](interval.md) | [`array`](array.md) | { [`geometry`](geometry.md) | [`json`](json.md) | [`uuid`](uuid.md) } | [`null`](null.md)
```

🟢 includes non-standard H2 syntax

A literal value of any data type, or null.

## Example

```sql
10
```
