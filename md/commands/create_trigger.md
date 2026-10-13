# CREATE TRIGGER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_trigger) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE TRIGGER [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`triggerName`](../grammar/name.md)
{ BEFORE | AFTER | INSTEAD OF }
{ INSERT | UPDATE | DELETE | { SELECT | ROLLBACK } }
[,...] ON [[`schemaName`](../grammar/name.md).][`tableName`](../grammar/name.md) [ FOR EACH { ROW | STATEMENT } ]
[ QUEUE [`int`](../grammar/int.md) ] [ NOWAIT ]
{ CALL [`triggeredClassNameString`](../grammar/string.md) | AS [`sourceCodeString`](../grammar/string.md) }
```

🟢 includes non-standard H2 syntax 🔴 compatibility-only syntax

Creates a new trigger. Admin rights are required to execute this command.

The trigger class must be public and implement `org.h2.api.Trigger`. Inner classes are not supported. The class must be available in the classpath of the database engine (when using the server mode, it must be in the classpath of the server).

The sourceCodeString must define a single method with no parameters that returns `org.h2.api.Trigger`. See `CREATE ALIAS` for requirements regarding the compilation. Alternatively, javax.script.ScriptEngineManager can be used to create an instance of `org.h2.api.Trigger`. Currently JavaScript (included in older `JREs` or provided by org.graalvm.js:js-scriptengine library in newer `JREs`) and ruby (with `JRuby`) are supported. In that case the source must begin respectively with `//javascript` or `#ruby`.

`BEFORE` triggers are called after data conversion is made, default values are set, null and length constraint checks have been made; but before other constraints have been checked. If there are multiple triggers, the order in which they are called is undefined.

`ROLLBACK` can be specified in combination with `INSERT, UPDATE`, and `DELETE`. Only row based `AFTER` trigger can be called on `ROLLBACK`. Exceptions that occur within such triggers are ignored. As the operations that occur within a trigger are part of the transaction, `ROLLBACK` triggers are only required if an operation communicates outside of the database.

`INSTEAD OF` triggers are implicitly row based and behave like `BEFORE` triggers. Only the first such trigger is called. Such triggers on views are supported. They can be used to make views updatable. These triggers on `INSERT` and `UPDATE` must update the passed new row to values that were actually inserted by the trigger; they are used for [FINAL TABLE](../grammar/data_change_delta_table.md) and for retrieval of generated keys.

A `BEFORE SELECT` trigger is fired just before the database engine tries to read from the table. The trigger can be used to update a table on demand. The trigger is called with both 'old' and 'new' set to null.

The `MERGE` statement will call both `INSERT` and `UPDATE` triggers. Not supported are `SELECT` triggers with the option `FOR EACH ROW`, and `AFTER SELECT` triggers.

Committing or rolling back a transaction within a trigger is not allowed, except for `SELECT` triggers.

By default a trigger is called once for each statement, without the old and new rows. `FOR EACH ROW` triggers are called once for each inserted, updated, or deleted row.

`QUEUE` is implemented for syntax compatibility with `HSQL` and has no effect.

The trigger need to be created in the same schema as the table. The schema name does not need to be specified when creating the trigger.

This command commits an open transaction in this connection.

## Example

```sql
CREATE TRIGGER TRIG_INS BEFORE INSERT ON TEST FOR EACH ROW CALL 'MyTrigger';
CREATE TRIGGER TRIG_SRC BEFORE INSERT ON TEST AS
    'org.h2.api.Trigger create() { return new MyTrigger("constructorParam"); }';
CREATE TRIGGER TRIG_JS BEFORE INSERT ON TEST AS '//javascript
return new (Java.type("org.example.MyTrigger"))("constructorParam");';
CREATE TRIGGER TRIG_RUBY BEFORE INSERT ON TEST AS '#ruby
Java::MyPackage::MyTrigger.new("constructorParam")';
```
