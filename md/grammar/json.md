# JSON

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#json) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
JSON { [`bytes`](bytes.md) | [`string`](string.md) }
```

🟢 includes non-standard H2 syntax

A binary or character string with a `RFC` 8259-compliant `JSON` text and data format. `JSON` text is parsed into internal representation. Order of object members is preserved as is. Duplicate object member names are allowed.

## Example

```sql
JSON '{"id":10,"name":"What''s this?"}'
JSON '[1, ' '2]';
JSON X'7472' '7565'
```
