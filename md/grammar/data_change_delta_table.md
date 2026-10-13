# Data Change Delta Table

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/grammar.html#data_change_delta_table) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
{ OLD | NEW | FINAL } TABLE
( { [`insert`](../commands/insert.md) | [`update`](../commands/update.md) | [`delete`](../commands/delete.md) | { [`mergeInto`](../commands/merge_into.md) } | [`mergeUsing`](../commands/merge_using.md) } )
```

🟢 includes non-standard H2 syntax

Executes the inner data change command and returns old, new, or final rows.

`OLD` is not allowed for `INSERT` command. It returns old rows.

`NEW` and `FINAL` are not allowed for `DELETE` command.

`NEW` returns new rows after evaluation of default expressions, but before execution of triggers.

`FINAL` returns new rows after execution of triggers.

## Example

```sql
SELECT ID FROM FINAL TABLE (INSERT INTO TEST (A, B) VALUES (1, 2))
```
