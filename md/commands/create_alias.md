# CREATE ALIAS

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#create_alias) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
CREATE ALIAS [ IF NOT EXISTS ] [[`schemaName`](../grammar/name.md).][`functionAliasName`](../grammar/name.md)
[ DETERMINISTIC ]
{ FOR [`classAndMethodString`](../grammar/string.md) | AS [`sourceCodeString`](../grammar/string.md) }
```

🟢 includes non-standard H2 syntax

Creates a new function alias. If this is a ResultSet returning function, by default the return value is cached in a local temporary file.

`DETERMINISTIC` - Deterministic functions must always return the same value for the same parameters.

The method name must be the full qualified class and method name, and may optionally include the parameter classes as in `java.lang.Integer.parseInt(java.lang.String, int)`. The class and the method must both be public, and the method must be static. The class must be available in the classpath of the database engine (when using the server mode, it must be in the classpath of the server).

When defining a function alias with source code, the Sun `javac` is compiler is used if the file `tools.jar` is in the classpath. If not, `javac` is run as a separate process. Only the source code is stored in the database; the class is compiled each time the database is re-opened. Source code is usually passed as dollar quoted text to avoid escaping problems. If import statements are used, then the tag `@CODE` must be added before the method.

If the method throws an `SQLException`, it is directly re-thrown to the calling application; all other exceptions are first converted to a `SQLException`.

If the first parameter of the Java function is a `java.sql.Connection`, then a connection to the database is provided. This connection must not be closed. If the class contains multiple methods with the given name but different parameter count, all methods are mapped.

Admin rights are required to execute this command. This command commits an open transaction in this connection.

If you have the Groovy jar in your classpath, it is also possible to write methods using Groovy.

## Example

```sql
CREATE ALIAS MY_SQRT FOR 'java.lang.Math.sqrt';
CREATE ALIAS MY_ROUND FOR 'java.lang.Math.round(double)';
CREATE ALIAS GET_SYSTEM_PROPERTY FOR 'java.lang.System.getProperty';
CALL GET_SYSTEM_PROPERTY('java.class.path');
CALL GET_SYSTEM_PROPERTY('com.acme.test', 'true');
CREATE ALIAS REVERSE AS 'String reverse(String s) { return new StringBuilder(s).reverse().toString(); }';
CALL REVERSE('Test');
CREATE ALIAS tr AS '@groovy.transform.CompileStatic
    static String tr(String str, String sourceSet, String replacementSet){
        return str.tr(sourceSet, replacementSet);
    }
'
```
