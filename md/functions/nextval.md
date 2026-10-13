# NEXTVAL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#nextval) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
NEXTVAL ( [ [`schemaNameString`](../grammar/string.md), ] [`sequenceString`](../grammar/string.md) )
```

🔴 compatibility-only syntax

Increments the sequence and returns its value. The current value of the sequence and the last identity in the current session are updated with the generated value. Used values are never re-used, even when the transaction is rolled back. This method exists only for compatibility, it's recommended to use the standard [NEXT VALUE FOR sequenceName](../grammar/sequence_value_expression.md) instead. If the schema name is not set, the current schema is used. When sequence is not found, the uppercase name is also checked. This method returns a long.

## Example

```sql
NEXTVAL('TEST_SEQ')
```
