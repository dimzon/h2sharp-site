# SCRIPT

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#script) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SCRIPT { [ NODATA ] | [ SIMPLE ] [ COLUMNS ] }
[ NOPASSWORDS ] [ NOSETTINGS ]
[ DROP ] [ BLOCKSIZE [`blockSizeInt`](../grammar/int.md) ]
[ TO [`fileNameString`](../grammar/string.md) [`scriptCompressionEncryption`](../grammar/script_compression_encryption.md)
[ CHARSET [`charsetString`](../grammar/string.md) ] ]
[ TABLE [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) [, ...] ]
[ SCHEMA [`schemaName`](../grammar/name.md) [, ...] ]
```

🟢 includes non-standard H2 syntax

Creates a SQL script from the database.

`NODATA` will not emit `INSERT` statements. `SIMPLE` does not use multi-row insert statements. `COLUMNS` includes column name lists into insert statements. If the `DROP` option is specified, drop statements are created for tables, views, and sequences. If the block size is set, `CLOB` and `BLOB` values larger than this size are split into separate blocks. `BLOCKSIZE` is used when writing out `LOB` data, and specifies the point at the values transition from being inserted as inline values, to be inserted using out-of-line commands. `NOSETTINGS` turns off dumping the database settings (the `SET XXX` commands)

If no '`TO` fileName' clause is specified, the script is returned as a result set. This command can be used to create a backup of the database. For long term storage, it is more portable than copying the database files.

If a '`TO` fileName' clause is specified, then the whole script (including insert statements) is written to this file, and a result set without the insert statements is returned.

The password must be in single quotes; it is case sensitive and can contain spaces.

This command locks objects while it is running. Admin rights are required to execute this command.

When using the `TABLE` or `SCHEMA` option, only the selected table(s) / schema(s) are included.

## Example

```sql
SCRIPT NODATA
```
