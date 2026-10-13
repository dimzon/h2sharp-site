# SET NON_KEYWORDS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_non_keywords) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET NON_KEYWORDS [ [`name`](../grammar/name.md) [,...] ]
```

🟢 includes non-standard H2 syntax

Converts the specified tokens from keywords to plain identifiers for the current session. This setting may break some commands and should be used with caution and only when necessary. Use [quoted identifiers](../grammar/quoted_name.md) instead of this setting if possible.

This command does not commit a transaction, and rollback does not affect it. This setting can be appended to the database URL: `jdbc:h2:./test;NON_KEYWORDS=KEY,VALUE`

## Example

```sql
SET NON_KEYWORDS KEY, VALUE
```
