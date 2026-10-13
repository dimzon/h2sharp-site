# Array element reference

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#array_element_reference) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ [`array`](array.md) | [`json`](json.md) } '[' [`indexInt`](int.md) ']'
```

Returns array element at specified 1-based index. Returns `NULL` if array or json is null, index is null, or element with specified index isn't found in `JSON`.

## Example

```sql
A[2]
M[5][8]
```
