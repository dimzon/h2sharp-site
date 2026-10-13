# CSVREAD

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#csvread) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CSVREAD([`fileNameString`](../grammar/string.md) [, [`columnsString`](../grammar/string.md) [, [`csvOptions`](../grammar/csv_options.md) ] ] )
```

🟢 includes non-standard H2 syntax

Returns the result set of reading the `CSV` (comma separated values) file. For each parameter, `NULL` means the default value should be used.

If the column names are specified (a list of column names separated with the fieldSeparator), those are used, otherwise (or if they are set to `NULL`) the first line of the file is interpreted as the column names. In that case, column names that contain no special characters (only letters, '_', and digits; similar to the rule for Java identifiers) are processed is the same way as unquoted identifiers and therefore case of characters may be changed. Other column names are processed as quoted identifiers and case of characters is preserved. To preserve the case of column names unconditionally use [caseSensitiveColumnNames](../grammar/csv_options.md) option.

The default charset is the default value for this system, and the default field separator is a comma. Missing unquoted values as well as data that matches nullString is parsed as `NULL`. All columns are of type `VARCHAR`.

The `BOM` (the byte-order-mark) character 0xfeff at the beginning of the file is ignored.

This function can be used like a table: `SELECT * FROM CSVREAD(...)`.

Instead of a file, a URL may be used, for example `jar:file:///c:/temp/example.zip!/org/example/nested.csv`. To read a stream from the classpath, use the prefix `classpath:`. To read from `HTTP`, use the prefix `http:` (as in a browser).

For performance reason, `CSVREAD` should not be used inside a join. Instead, import the data first (possibly into a temporary table) and then use the table.

Admin rights are required to execute this command.

## Example

```sql
SELECT * FROM CSVREAD('test.csv');
-- Read a file containing the columns ID, NAME with
SELECT * FROM CSVREAD('test2.csv', 'ID|NAME', 'charset=UTF-8 fieldSeparator=|');
SELECT * FROM CSVREAD('data/test.csv', null, 'rowSeparator=;');
-- Read a tab-separated file
SELECT * FROM CSVREAD('data/test.tsv', null, 'rowSeparator=' || CHAR(9));
SELECT "Last Name" FROM CSVREAD('address.csv');
SELECT "Last Name" FROM CSVREAD('classpath:/org/acme/data/address.csv');
```
