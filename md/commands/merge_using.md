# MERGE USING

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#merge_using) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
MERGE INTO [[`schemaName`](../grammar/name.md).][`targetTableName`](../grammar/name.md) [ [AS] [`targetAlias`](../grammar/alias.md)]
USING [`tableExpression`](../grammar/table_expression.md)
ON [`expression`](../grammar/expression.md)
[`mergeWhenClause`](../grammar/merge_when_clause.md) [,...]
```

Updates or deletes existing rows, and insert rows that don't exist.

The `ON` clause specifies the matching column expression.

Different rows from a source table may not match with the same target row (this is not ensured by H2 if target table is an updatable view). One source row may be matched with multiple target rows.

If statement doesn't need a source table a `DUAL` table can be substituted.

## Example

```sql
MERGE INTO TARGET_TABLE AS T USING SOURCE_TABLE AS S
    ON T.ID = S.ID
    WHEN MATCHED AND T.COL2 <> 'FINAL' THEN
        UPDATE SET T.COL1 = S.COL1
    WHEN MATCHED AND T.COL2 = 'FINAL' THEN
        DELETE
    WHEN NOT MATCHED THEN
        INSERT (ID, COL1, COL2) VALUES(S.ID, S.COL1, S.COL2);
MERGE INTO TARGET_TABLE AS T USING (SELECT * FROM SOURCE_TABLE) AS S
    ON T.ID = S.ID
    WHEN MATCHED AND T.COL2 <> 'FINAL' THEN
        UPDATE SET T.COL1 = S.COL1
    WHEN MATCHED AND T.COL2 = 'FINAL' THEN
        DELETE
    WHEN NOT MATCHED THEN
        INSERT VALUES (S.ID, S.COL1, S.COL2);
MERGE INTO TARGET T USING (VALUES (1, 4), (2, 15)) S(ID, V)
    ON T.ID = S.ID
    WHEN MATCHED THEN UPDATE SET V = S.V
    WHEN NOT MATCHED THEN INSERT VALUES (S.ID, S.V);
MERGE INTO TARGET_TABLE USING DUAL ON ID = 1
    WHEN NOT MATCHED THEN INSERT VALUES (1, 'Test')
    WHEN MATCHED THEN UPDATE SET NAME = 'Test';
```
