# ALTER TYPE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#alter_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ALTER TYPE [[`schemaName`](../grammar/name.md).][`enumName`](../grammar/name.md) ADD VALUE [`string`](../grammar/string.md)
```

🟢 includes non-standard H2 syntax

Adds new value to enum.

Duplicate and empty values are not permitted. The maximum number of values is 65536. The maximum allowed length of complete data type definition with all values is 1,000,000,000 characters.

## Example

```sql
ALTER TYPE card_suit ADD VALUE 'clubs'
```
