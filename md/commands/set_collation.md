# SET COLLATION

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_collation) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET [ DATABASE ] COLLATION
{ OFF | [`collationName`](../grammar/name.md)
[ STRENGTH { PRIMARY | SECONDARY | TERTIARY | IDENTICAL } ] }
```

🟢 includes non-standard H2 syntax

Sets the collation used for comparing strings. This command can only be executed if there are no tables defined. See `java.text.Collator` for details about the supported collations and the `STRENGTH` (`PRIMARY` is usually case- and umlaut-insensitive; `SECONDARY` is case-insensitive but umlaut-sensitive; `TERTIARY` is both case- and umlaut-sensitive; `IDENTICAL` is sensitive to all differences and only affects ordering).

The `ICU4J` collator is used if it is in the classpath. It is also used if the collation name starts with `ICU4J_` (in that case, the `ICU4J` must be in the classpath, otherwise an exception is thrown). The default collator is used if the collation name starts with `DEFAULT_` (even if `ICU4J` is in the classpath). The charset collator is used if the collation name starts with `CHARSET_` (e.g. `CHARSET_CP500`). This collator sorts strings according to the binary representation in the given charset.

Admin rights are required to execute this command. This command commits an open transaction in this connection. This setting is persistent. This setting can be appended to the database URL: `jdbc:h2:./test;COLLATION='ENGLISH'`

## Example

```sql
SET COLLATION ENGLISH
SET COLLATION CHARSET_CP500
```
