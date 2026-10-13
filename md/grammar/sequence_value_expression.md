# Sequence value expression

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#sequence_value_expression) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ NEXT | { CURRENT } } VALUE FOR [[`schemaName`](name.md).][`sequenceName`](name.md)
```

🟢 includes non-standard H2 syntax

The next or current value of a sequence.

When the next value is requested the sequence is incremented and the current value of the sequence and the last identity in the current session are updated with the generated value. The next value of the sequence is generated only once for each processed row. If this expression is used multiple times with the same sequence it returns the same value within a processed row. Used values are never re-used, even when the transaction is rolled back.

Current value may only be requested after generation of the sequence value in the current session. It returns the latest generated value for the current session.

If a single command contains next and current value expressions for the same sequence there is no guarantee that the next value expression will be evaluated before the evaluation of current value expression.

## Example

```sql
NEXT VALUE FOR SEQ1
CURRENT VALUE FOR SCHEMA2.SEQ2
```
