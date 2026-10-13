# SELECT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#select) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SELECT [ DISTINCT [ ON ( [`expression`](../grammar/expression.md) [,...] ) ] | ALL ]
[`selectExpression`](../grammar/select_expression.md) [,...]
[ FROM [`tableExpression`](../grammar/table_expression.md) [,...] ]
[ WHERE [`expression`](../grammar/expression.md) ]
[ GROUP BY [`groupingElement`](../grammar/grouping_element.md) [,...] ] [ HAVING [`expression`](../grammar/expression.md) ]
[ WINDOW { { [`windowName`](../grammar/name.md) AS [`windowSpecification`](../grammar/window_specification.md) } [,...] } ]
[ QUALIFY [`expression`](../grammar/expression.md) ]
[ { UNION [ ALL ] | EXCEPT | INTERSECT } [`query`](../grammar/query.md) ]
[ ORDER BY [`selectOrder`](../grammar/select_order.md) [,...] ]
[ OFFSET [`expression`](../grammar/expression.md) { ROW | ROWS } ]
[ FETCH { FIRST | NEXT } [ [`expression`](../grammar/expression.md) [ PERCENT ] ] { ROW | ROWS }
{ ONLY | WITH TIES } ]
[ FOR UPDATE [ NOWAIT | WAIT [`secondsNumeric`](../grammar/numeric.md) | SKIP LOCKED ] ]
```

🟢 includes non-standard H2 syntax

Selects data from a table or multiple tables.

Command is executed in the following logical order:

1. Data is taken from table value expressions that are specified in the `FROM` clause, joins are executed. If `FROM` clause is not specified a single row is constructed.

2. `WHERE` filters rows. Aggregate or window functions are not allowed in this clause.

3. `GROUP BY` groups the result by the given expression(s). If `GROUP BY` clause is not specified, but non-window aggregate functions are used or `HAVING` is specified all rows are grouped together.

4. Aggregate functions are evaluated.

5. `HAVING` filters rows after grouping and evaluation of aggregate functions. Non-window aggregate functions are allowed in this clause.

6. Window functions are evaluated.

7. `QUALIFY` filters rows after evaluation of window functions. Aggregate and window functions are allowed in this clause.

8. `DISTINCT` removes duplicates. If `DISTINCT ON` is used only the specified expressions are checked for duplicates; `ORDER BY` clause, if any, is used to determine preserved rows. First row is each `DISTINCT ON` group is preserved. In absence of `ORDER BY` preserved rows are not determined, database may choose any row from each `DISTINCT ON` group.

9. `UNION, EXCEPT`, and `INTERSECT` combine the result of this query with the results of another query. `INTERSECT` has higher precedence than `UNION` and `EXCEPT`. Operators with equal precedence are evaluated from left to right.

10. `ORDER BY` sorts the result by the given column(s) or expression(s).

11. Number of rows in output can be limited with `OFFSET` and `FETCH` clauses. `OFFSET` specifies how many rows to skip. Please note that queries with high offset values can be slow. `FETCH FIRST`/`NEXT` limits the number of rows returned by the query. If `PERCENT` is specified number of rows is specified as a percent of the total number of rows and should be an integer value between 0 and 100 inclusive. `WITH TIES` can be used only together with `ORDER BY` and means that all additional rows that have the same sorting position as the last row will be also returned.

`WINDOW` clause specifies window definitions for window functions and window aggregate functions. This clause can be used to reuse the same definition in multiple functions.

If `FOR UPDATE` is specified, the tables or rows are locked for writing. If some rows are locked by another session, this query will wait some time for release of these locks, unless `NOWAIT` or `SKIP LOCKED` is specified. If `SKIP LOCKED` is specified, these locked rows will be excluded from result of this query. If `NOWAIT` is specified, presence of these rows will stop execution of this query immediately. If `WAIT` with timeout is specified and some rows are locked by another session, this timeout will be used instead of default timeout for this session. Please note that with current implementation the timeout doesn't limit execution time of the whole query, it only limits wait time for completion of particular transaction that holds a lock on a row selected by this query.

This clause is not allowed in `DISTINCT` queries and in queries with non-window aggregates, `GROUP BY`, or `HAVING` clauses. Only the selected rows are locked as in an `UPDATE` statement. Rows from the right side of a left join and from the left side of a right join, including nested joins, aren't locked. Locking behavior for rows that were excluded from result using `OFFSET` / `FETCH` / `LIMIT` / `TOP` or `QUALIFY` is undefined, to avoid possible locking of excessive rows try to filter out unneeded rows with the `WHERE` criteria when possible. Rows are processed one by one. Each row is read, tested with `WHERE` criteria, locked, read again and re-tested, because its value may be changed by concurrent transaction before lock acquisition. Note that new uncommitted rows from other transactions are not visible unless read uncommitted isolation level is used and therefore cannot be selected and locked. Modified uncommitted rows from other transactions that satisfy the `WHERE` criteria cause this `SELECT` to wait for commit or rollback of those transactions.

## Example

```sql
SELECT * FROM TEST;
SELECT * FROM TEST ORDER BY NAME;
SELECT ID, COUNT(*) FROM TEST GROUP BY ID;
SELECT NAME, COUNT(*) FROM TEST GROUP BY NAME HAVING COUNT(*) > 2;
SELECT 'ID' COL, MAX(ID) AS MAX FROM TEST UNION SELECT 'NAME', MAX(NAME) FROM TEST;
SELECT * FROM TEST OFFSET 1000 ROWS FETCH FIRST 1000 ROWS ONLY;
SELECT A, B FROM TEST ORDER BY A FETCH FIRST 10 ROWS WITH TIES;
SELECT * FROM (SELECT ID, COUNT(*) FROM TEST
    GROUP BY ID UNION SELECT NULL, COUNT(*) FROM TEST)
    ORDER BY 1 NULLS LAST;
SELECT DISTINCT C1, C2 FROM TEST;
SELECT DISTINCT ON(C1) C1, C2 FROM TEST ORDER BY C1;
SELECT ID, V FROM TEST WHERE ID IN (1, 2, 3) FOR UPDATE WAIT 0.5;
```
