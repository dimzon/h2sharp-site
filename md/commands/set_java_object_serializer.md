# SET JAVA_OBJECT_SERIALIZER

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_java_object_serializer) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET JAVA_OBJECT_SERIALIZER { [`null`](../grammar/null.md) | [`className`](../grammar/name.md) }
```

🟢 includes non-standard H2 syntax

Sets the object used to serialize and deserialize java objects being stored in column of type `OTHER`. The serializer class must be public and implement `org.h2.api.JavaObjectSerializer`. Inner classes are not supported. The class must be available in the classpath of the database engine (when using the server mode, it must be both in the classpath of the server and the client). This command can only be executed if there are no tables defined.

Admin rights are required to execute this command. This command commits an open transaction in this connection. This setting is persistent. This setting can be appended to the database URL: `jdbc:h2:./test;JAVA_OBJECT_SERIALIZER='com.acme.SerializerClassName'`

## Example

```sql
SET JAVA_OBJECT_SERIALIZER 'com.acme.SerializerClassName'
```
