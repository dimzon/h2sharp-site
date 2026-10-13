# DIFFERENCE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#difference) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
DIFFERENCE([`string`](../grammar/string.md), [`string`](../grammar/string.md))
```

🟢 includes non-standard H2 syntax

Returns the difference between the sounds of two strings. The difference is calculated as a number of matched characters in the same positions in `SOUNDEX` representations of arguments. This method returns an int between 0 and 4 inclusive, or null if any of its parameters is null. Note that value of 0 means that strings are not similar to each other. Value of 4 means that strings are fully similar to each other (have the same `SOUNDEX` representation).

## Example

```sql
DIFFERENCE(T1.NAME, T2.NAME)
```
