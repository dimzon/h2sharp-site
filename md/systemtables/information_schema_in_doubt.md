# IN_DOUBT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema_in_doubt) · © H2 Group (MPL-2.0 / EPL-1.0)

Contains information about prepared transactions.

| Column | Type | Description |
| --- | --- | --- |
| TRANSACTION_NAME | CHARACTER VARYING | The name of prepared transaction. |
| TRANSACTION_STATE | CHARACTER VARYING | The state of prepared transaction ('IN_DOUBT', 'COMMIT', or 'ROLLBACK'). |
