# ROWNUM

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#rownum) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ROWNUM()
```

🟢 includes non-standard H2 syntax

Returns the number of the current row. This method returns a long value. It is supported for `SELECT` statements, as well as for `DELETE` and `UPDATE`. The first row has the row number 1, and is calculated before ordering and grouping the result set, but after evaluating index conditions (even when the index conditions are specified in an outer query). Use the [ROW_NUMBER() OVER ()](../functions-window/row_number.md) function to get row numbers after grouping or in specified order.

## Example

```sql
SELECT ROWNUM(), * FROM TEST;
SELECT ROWNUM(), * FROM (SELECT * FROM TEST ORDER BY NAME);
SELECT ID FROM (SELECT T.*, ROWNUM AS R FROM TEST T) WHERE R BETWEEN 2 AND 3;
```
