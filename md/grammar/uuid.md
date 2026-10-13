# UUID

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#uuid) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
UUID '{ [`digit`](digit.md) | a-f | A-F | - } [...]'
```

🟢 includes non-standard H2 syntax

A `UUID` literal. Must contain 32 hexadecimal digits. Digits may be separated with - signs.

## Example

```sql
UUID '12345678-1234-1234-1234-123456789ABC'
```
