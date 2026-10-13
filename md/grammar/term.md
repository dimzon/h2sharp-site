# Term

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#term) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ [`value`](value.md)
| [`column`](column.md)
| ?[ [`int`](int.md) ]
| [`sequenceValueExpression`](sequence_value_expression.md)
| function
| { - | + } [`term`](term.md)
| ( [`expression`](expression.md) )
| [`arrayElementReference`](array_element_reference.md)
| [`fieldReference`](field_reference.md)
| ( [`query`](query.md) )
| [`caseExpression`](case_expression.md)
| [`castSpecification`](cast_specification.md)
| [`userDefinedFunctionName`](name.md) }
[ [`timeZone`](time_zone.md) | [`intervalQualifier`](interval_qualifier.md) ]
```

A value. Parameters can be indexed, for example `?1` meaning the first parameter.

Interval qualifier may only be specified for a compatible value or for a subtraction operation between two datetime values. The subtraction operation ignores the leading field precision of the qualifier.

## Example

```sql
'Hello'
```
