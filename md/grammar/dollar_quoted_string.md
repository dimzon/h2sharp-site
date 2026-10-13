# Dollar Quoted String

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#dollar_quoted_string) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
$$anything$$
```

🟢 includes non-standard H2 syntax

A string starts and ends with two dollar signs. Two dollar signs are not allowed within the text. A whitespace is required before the first set of dollar signs. No escaping is required within the text.

## Example

```sql
$$John's car$$
```
