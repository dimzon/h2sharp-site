# REGEXP_REPLACE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#regexp_replace) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REGEXP_REPLACE([`inputString`](../grammar/string.md), [`regexString`](../grammar/string.md), [`replacementString`](../grammar/string.md) [, [`flagsString`](../grammar/string.md)])
```

🟢 includes non-standard H2 syntax

Replaces each substring that matches a regular expression. For details, see the Java `String.replaceAll()` method. If any parameter is null (except optional flagsString parameter), the result is null.

Flags values are limited to 'i', 'c', 'n', 'm'. Other symbols cause exception. Multiple symbols could be used in one flagsString parameter (like 'im'). Later flags override first ones, for example 'ic' is equivalent to case sensitive matching 'c'.

'i' enables case insensitive matching (Pattern.`CASE_INSENSITIVE`)

'c' disables case insensitive matching (Pattern.`CASE_INSENSITIVE`)

'n' allows the period to match the newline character (Pattern.`DOTALL`)

'm' enables multiline mode (Pattern.`MULTILINE`)

## Example

```sql
REGEXP_REPLACE('Hello    World', ' +', ' ')
REGEXP_REPLACE('Hello WWWWorld', 'w+', 'W', 'i')
```
