# SET IGNORE_CATALOGS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_ignore_catalogs) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET IGNORE_CATALOGS { TRUE | FALSE }
```

🔴 compatibility-only syntax

If `IGNORE_CATALOGS` is enabled, catalog names in front of schema names will be ignored. This can be used if multiple catalogs used by the same connections must be simulated. Caveat: if both catalogs contain schemas of the same name and if those schemas contain objects of the same name, this will lead to errors, when trying to manage, access or change these objects. This setting can be appended to the database URL: `jdbc:h2:./test;IGNORE_CATALOGS=TRUE`

## Example

```sql
SET IGNORE_CATALOGS TRUE
```
