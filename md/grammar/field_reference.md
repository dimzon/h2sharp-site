# Field reference

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#field_reference) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
([`expression`](expression.md)).[`fieldName`](name.md)
```

Returns field value from the row value or `JSON` value. Returns `NULL` if value is null or field with specified name isn't found in `JSON`. Expression on the left must be enclosed in parentheses if it is an identifier (column name), in other cases they aren't required.

## Example

```sql
(R).FIELD1
(TABLE1.COLUMN2).FIELD.SUBFIELD
JSON '{"a": 1, "b": 2}'."b"
```
