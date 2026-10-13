# SET MAX_LENGTH_INPLACE_LOB

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_max_length_inplace_lob) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET MAX_LENGTH_INPLACE_LOB [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the maximum size of an in-place `LOB` object.

This is the maximum length of an `LOB` that is stored with the record itself, and the default value is 256.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent.

## Example

```sql
SET MAX_LENGTH_INPLACE_LOB 128
```
