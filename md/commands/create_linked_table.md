# CREATE LINKED TABLE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_linked_table) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE [ FORCE ] [ [ GLOBAL | LOCAL ] TEMPORARY ]
LINKED TABLE [ IF NOT EXISTS ]
[[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) ( [`driverString`](../grammar/string.md), [`urlString`](../grammar/string.md), [`userString`](../grammar/string.md), [`passwordString`](../grammar/string.md),
[ [`originalSchemaString`](../grammar/string.md), ] [`originalTableString`](../grammar/string.md) )
[ EMIT UPDATES | READONLY ] [ FETCH_SIZE [`sizeInt`](../grammar/int.md)] [AUTOCOMMIT ON|OFF]
```

🟢 includes non-standard H2 syntax

Creates a table link to an external table. The driver name may be empty if the driver is already loaded. If the schema name is not set, only one table with that name may exist in the target database.

`FORCE` - Create the `LINKED TABLE` even if the remote database/table does not exist.

`EMIT UPDATES` - Usually, for update statements, the old rows are deleted first and then the new rows are inserted. It is possible to emit update statements (except on rollback), however in this case multi-row unique key updates may not always work. Linked tables to the same database share one connection.

`READONLY` - is set, the remote table may not be updated. This is enforced by H2.

`FETCH_SIZE` - the number of rows fetched, a hint with non-negative number of rows to fetch from the external table at once, may be ignored by the driver of external database. 0 is default and means no hint. The value is passed to `java.sql.Statement.setFetchSize()` method.

`AUTOCOMMIT` - is set to `ON`, the auto-commit mode is enable. `OFF` is disable. The value is passed to `java.sql.Connection.setAutoCommit()` method.

If the connection to the source database is lost, the connection is re-opened (this is a workaround for MySQL that disconnects after 8 hours of inactivity by default).

If a query is used instead of the original table name, the table is read only. Queries must be enclosed in parenthesis: `(SELECT * FROM ORDERS)`.

To use `JNDI` to get the connection, the driver class must be a javax.naming.Context (for example `javax.naming.InitialContext`), and the URL must be the resource name (for example `java:comp/env/jdbc/Test`).

Admin rights are required to execute this command. This command commits an open transaction in this connection.

## Example

```sql
CREATE LINKED TABLE LINK('org.h2.Driver', 'jdbc:h2:./test2',
    'sa', 'sa', 'TEST');
CREATE LINKED TABLE LINK('', 'jdbc:h2:./test2', 'sa', 'sa',
    '(SELECT * FROM TEST WHERE ID>0)');
CREATE LINKED TABLE LINK('javax.naming.InitialContext',
    'java:comp/env/jdbc/Test', NULL, NULL,
    '(SELECT * FROM TEST WHERE ID>0)');
```
