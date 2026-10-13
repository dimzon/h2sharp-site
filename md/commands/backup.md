# BACKUP

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#backup) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
BACKUP TO [`fileNameString`](../grammar/string.md)
```

🟢 includes non-standard H2 syntax

Backs up the database files to a .zip file. Objects are not locked, but the backup is transactionally consistent because the transaction log is also copied. Admin rights are required to execute this command.

## Example

```sql
BACKUP TO 'backup.zip'
```
