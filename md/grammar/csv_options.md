# Csv Options

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#csv_options) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[`charsetString`](string.md) [, [`fieldSepString`](string.md) [, [`fieldDelimString`](string.md) [, [`escString`](string.md) [, [`nullString`](string.md)]]]]
| [`optionString`](string.md)
```

🟢 includes non-standard H2 syntax

Optional parameters for `CSVREAD` and `CSVWRITE`. Instead of setting the options one by one, all options can be combined into a space separated key-value pairs, as follows: `STRINGDECODE('charset=UTF-8 escape=\" fieldDelimiter=\" fieldSeparator=, ' || 'lineComment=# lineSeparator=\n null= rowSeparator=')`. The following options are supported:

`caseSensitiveColumnNames` (true or false; disabled by default),

`charset` (for example '`UTF`-8'),

`escape` (the character that escapes the field delimiter),

`fieldDelimiter` (a double quote by default),

`fieldSeparator` (a comma by default),

`lineComment` (disabled by default),

`lineSeparator` (the line separator used for writing; ignored for reading),

`null` Support reading existing `CSV` files that contain explicit `null` delimiters. Note that an empty, unquoted values are also treated as null.

`quotedNulls` (quotes the nullString. true of false; disabled by default),

`preserveWhitespace` (true or false; disabled by default),

`writeColumnHeader` (true or false; enabled by default).

For a newline or other special character, use `STRINGDECODE` as in the example above. A space needs to be escaped with a backslash (`'\ '`), and a backslash needs to be escaped with another backslash (`'\\'`). All other characters are not to be escaped, that means newline and tab characters are written as such.

## Example

```sql
CALL CSVWRITE('test2.csv', 'SELECT * FROM TEST', 'charset=UTF-8 fieldSeparator=|');
```
