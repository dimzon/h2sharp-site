# ESTIMATED_ENVELOPE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#estimated_envelope) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ESTIMATED_ENVELOPE([`tableNameString`](../grammar/string.md), [`columnNameString`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Returns the estimated minimum bounding box that encloses all specified `GEOMETRY` values. Only 2D coordinate plane is supported. `NULL` values are ignored. Column must have a spatial index. This function is fast, but estimation may include uncommitted data (including data from other transactions), may return approximate bounds, or be different with actual value due to other reasons. Use with caution. If estimation is not available this function returns `NULL`. For accurate and reliable result use `ESTIMATE` aggregate function instead.

## Example

```sql
CALL ESTIMATED_ENVELOPE('MY_TABLE', 'GEOMETRY_COLUMN');
```
