# WITH

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#with) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
WITH [ RECURSIVE ] { [`name`](../grammar/name.md) [( [`columnName`](../grammar/name.md) [,...] )] AS ( [`query`](../grammar/query.md) ) [,...] }
[`query`](../grammar/query.md)
```

Can be used to create a recursive or non-recursive query (common table expression). For recursive queries the first select has to be a `UNION`. One or more common table entries can be referred to by name. Column name declarations are optional - the column names will be inferred from the named select queries.

## Example

```sql
WITH RECURSIVE cte(n) AS (
        SELECT 1
    UNION ALL
        SELECT n + 1
        FROM cte
        WHERE n < 100
)
SELECT sum(n) FROM cte;

Example 2:
WITH cte1 AS (
        SELECT 1 AS FIRST_COLUMN
), cte2 AS (
        SELECT FIRST_COLUMN+1 AS FIRST_COLUMN FROM cte1
)
SELECT sum(FIRST_COLUMN) FROM cte2;
```
