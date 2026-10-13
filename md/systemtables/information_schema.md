# Information Schema

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/systemtables.html#information_schema) · © H2 Group (MPL-2.0 / EPL-1.0)

The system tables and views in the schema `INFORMATION_SCHEMA` contain the meta data
of all tables, views, domains, and other objects in the database as well as the current settings.
This documentation describes the default new version of `INFORMATION_SCHEMA` for H2 2.0.
Old TCP clients (1.4.200 and below) see the legacy version of `INFORMATION_SCHEMA`,
because they can't work with the new one. The legacy version is not documented.
