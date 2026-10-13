# RANDOM_UUID

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/functions.html#random_uuid) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
RANDOM_UUID([[`versionInt`](../grammar/int.md)]) | UUID()
```

🟢 includes non-standard H2 syntax

Returns a new `RFC` 9562-compliant `UUID` with the specified version. If version is not specified, a default version will be used. Current default is 4, but it may be changed in future versions of H2.

Version 4 is a `UUID` with 122 pseudo random bits. Please note that using an index on randomly generated data will result on poor performance once there are millions of rows in a table. The reason is that the cache behavior is very bad with randomly distributed data. This is a problem for any database system.

Version 7 is a time-ordered `UUID` value with layout optimized for database systems. It contains 48-bit number of milliseconds seconds since midnight 1 Jan 1970 `UTC` with leap seconds excluded, additional 12-bit sub-millisecond timestamp fraction if available, and 62 pseudo random bits.

## Example

```sql
RANDOM_UUID(7)
RANDOM_UUID()
```
