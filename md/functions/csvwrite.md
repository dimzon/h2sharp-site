# CSVWRITE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#csvwrite) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CSVWRITE ( [`fileNameString`](../grammar/string.md), [`queryString`](../grammar/string.md) [, [`csvOptions`](../grammar/csv_options.md) [, [`lineSepString`](../grammar/string.md)] ] )
```

🟢 includes non-standard H2 syntax

Writes a `CSV` (comma separated values). The file is overwritten if it exists. If only a file name is specified, it will be written to the current working directory. For each parameter, `NULL` means the default value should be used. The default charset is the default value for this system, and the default field separator is a comma.

The values are converted to text using the default string representation; if another conversion is required you need to change the select statement accordingly. The parameter nullString is used when writing `NULL` (by default nothing is written when `NULL` appears). The default line separator is the default value for this system (system property `line.separator`).

The returned value is the number or rows written. Admin rights are required to execute this command.

## Example

```sql
CALL CSVWRITE('data/test.csv', 'SELECT * FROM TEST');
CALL CSVWRITE('data/test2.csv', 'SELECT * FROM TEST', 'charset=UTF-8 fieldSeparator=|');
-- Write a tab-separated file
CALL CSVWRITE('data/test.tsv', 'SELECT * FROM TEST', 'charset=UTF-8 fieldSeparator=' || CHAR(9));
```
