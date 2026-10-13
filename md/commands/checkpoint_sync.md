# CHECKPOINT SYNC

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#checkpoint_sync) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CHECKPOINT SYNC
```

🟢 includes non-standard H2 syntax

Flushes the data to disk and forces all system buffers be written to the underlying device.

Admin rights are required to execute this command.

## Example

```sql
CHECKPOINT SYNC
```
