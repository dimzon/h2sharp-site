# SET CACHE_SIZE

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/commands.html#set_cache_size) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
SET CACHE_SIZE [`int`](../grammar/int.md)
```

🟢 includes non-standard H2 syntax

Sets the size of the cache in KB (each KB being 1024 bytes) for the current database. The default is 65536 per available GB of `RAM`, i.e. 64 MB per GB. The value is rounded to the next higher power of two. Depending on the virtual machine, the actual memory required may be higher.

This setting is persistent and affects all connections as there is only one cache per database. Using a very small value (specially 0) will reduce performance a lot. This setting only affects the database engine (the server in a client/server environment; in embedded mode, the database engine is in the same process as the application). It has no effect for in-memory databases.

Admin rights are required to execute this command, as it affects all connections. This command commits an open transaction in this connection. This setting is persistent. This setting can be appended to the database URL: `jdbc:h2:./test;CACHE_SIZE=8192`

## Example

```sql
SET CACHE_SIZE 8192
```
