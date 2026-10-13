# REGEXP_SUBSTR

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#regexp_substr) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
REGEXP_SUBSTR([`inputString`](../grammar/string.md), [`regexString`](../grammar/string.md) [, [`positionInt`](../grammar/int.md), [`occurrenceInt`](../grammar/int.md), [`flagsString`](../grammar/string.md), [`groupInt`](../grammar/int.md)])
```

🟢 includes non-standard H2 syntax

Matches string to a regular expression and returns the matched substring. For details, see the java.util.regex.Pattern and related functionality.

The parameter position specifies where in inputString the match should start. Occurrence indicates which occurrence of pattern in inputString to search for.

Flags values are limited to 'i', 'c', 'n', 'm'. Other symbols cause exception. Multiple symbols could be used in one flagsString parameter (like 'im'). Later flags override first ones, for example 'ic' is equivalent to case sensitive matching 'c'.

'i' enables case insensitive matching (Pattern.`CASE_INSENSITIVE`)

'c' disables case insensitive matching (Pattern.`CASE_INSENSITIVE`)

'n' allows the period to match the newline character (Pattern.`DOTALL`)

'm' enables multiline mode (Pattern.`MULTILINE`)

If the pattern has groups, the group parameter can be used to specify which group to return.

## Example

```sql
REGEXP_SUBSTR('2020-10-01', '\d{4}')
REGEXP_SUBSTR('2020-10-01', '(\d{4})-(\d{2})-(\d{2})', 1, 1, NULL, 2)
```
