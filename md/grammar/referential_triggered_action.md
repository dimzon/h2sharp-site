# Referential Triggered Action

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#referential_triggered_action) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
ON UPDATE [`referentialAction`](referential_action.md) [ ON DELETE [`referentialAction`](referential_action.md) ]
| ON DELETE [`referentialAction`](referential_action.md) [ ON UPDATE [`referentialAction`](referential_action.md) ]
```

Referential actions triggered during unique key updates and row deletions in the referenced table.

## Example

```sql
ON UPDATE CASCADE ON DELETE CASCADE
```
