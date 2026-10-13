# CURRVAL

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#currval) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CURRVAL( [ [`schemaNameString`](../grammar/string.md), ] [`sequenceString`](../grammar/string.md) )
```

🔴 compatibility-only syntax

Returns the latest generated value of the sequence for the current session. Current value may only be requested after generation of the sequence value in the current session. This method exists only for compatibility, when it isn't required use [CURRENT VALUE FOR sequenceName](../grammar/sequence_value_expression.md) instead. If the schema name is not set, the current schema is used. When sequence is not found, the uppercase name is also checked. This method returns a long.

## Example

```sql
CURRVAL('TEST_SEQ')
```
