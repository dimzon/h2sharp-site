# String

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#string) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
[N]'anything' [...]
| U&{'anything' [...]} [ UESCAPE 'anything' ]
```

A character string literal starts and ends with a single quote. Two single quotes can be used to create a single quote inside a string. Prefix `N` means a national character string literal; H2 does not distinguish regular and national character string literals in any way, this prefix has no effect in H2.

String literals staring with `U&` are Unicode character string literals. All character string literals in H2 may have Unicode characters, but Unicode character string literals may contain Unicode escape sequences `\0000` or `\+000000`, where \ is an escape character, `0000` and `000000` are Unicode character codes in hexadecimal notation. Optional `UESCAPE` clause may be used to specify another escape character, with exception for single quote, double quote, plus sign, and hexadecimal digits (0-9, a-f, and A-F). By default the backslash is used. Two escape characters can be used to include a single character inside a string. Two single quotes can be used to create a single quote inside a string.

## Example

```sql
'John''s car'
'A' 'B' 'C'
U&'W\00f6rter ' '\\ \+01f600 /'
U&'|00a1' UESCAPE '|'
```
