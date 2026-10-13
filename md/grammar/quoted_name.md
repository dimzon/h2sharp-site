# Quoted Name

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#quoted_name) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
"anything"
| U&"anything" [ UESCAPE 'anything' ]
```

Case of characters in quoted names is preserved as is. Such names can contain spaces. The maximum name length is 256 characters. Two double quotes can be used to create a single double quote inside an identifier. With default settings identifiers in H2 are case sensitive.

Identifiers staring with `U&` are Unicode identifiers. All identifiers in H2 may have Unicode characters, but Unicode identifiers may contain Unicode escape sequences `\0000` or `\+000000`, where \ is an escape character, `0000` and `000000` are Unicode character codes in hexadecimal notation. Optional `UESCAPE` clause may be used to specify another escape character, with exception for single quote, double quote, plus sign, and hexadecimal digits (0-9, a-f, and A-F). By default the backslash is used. Two escape characters can be used to include a single character inside an Unicode identifier. Two double quotes can be used to create a single double quote inside an Unicode identifier.

## Example

```sql
"FirstName"
U&"\00d6ffnungszeit"
U&"/00d6ffnungszeit" UESCAPE '/'
```
