# GEOMETRY

> H2 `2.5.252` + H2Sharp pin `27c5170` · [Original](https://www.h2database.com/html/datatypes.html#geometry_type) · © H2 Group (MPL-2.0 / EPL-1.0)

## Syntax

```bnf
GEOMETRY
[({ GEOMETRY |
{ POINT
| LINESTRING
| POLYGON
| MULTIPOINT
| MULTILINESTRING
| MULTIPOLYGON
| GEOMETRYCOLLECTION } [Z|M|ZM]}
[, [`sridInt`](../grammar/int.md)] )]
```

🟢 includes non-standard H2 syntax

A spatial geometry type. If additional constraints are not specified this type accepts all supported types of geometries. A constraint with required geometry type and dimension system can be set by specifying name of the type and dimension system. A whitespace between them is optional. 2D dimension system does not have a name and assumed if only a geometry type name is specified. `POINT` means 2D point, `POINT` Z or `POINTZ` means 3D point. `GEOMETRY` constraint means no restrictions on type or dimension system of geometry. A constraint with required spatial reference system identifier (`SRID`) can be set by specifying this identifier.

Mapped to `org.locationtech.jts.geom.Geometry` if `JTS` library is in classpath and to `java.lang.String` otherwise. May be represented in textual format using the `WKT` (well-known text) or `EWKT` (extended well-known text) format. Values are stored internally in `EWKB` (extended well-known binary) format, the maximum allowed length is 1,000,000,000 bytes. Only a subset of `EWKB` and `EWKT` features is supported. Supported objects are `POINT, LINESTRING, POLYGON, MULTIPOINT, MULTILINESTRING, MULTIPOLYGON`, and `GEOMETRYCOLLECTION`. Supported dimension systems are 2D (`XY`), Z (`XYZ`), M (`XYM`), and `ZM` (`XYZM`). `SRID` (spatial reference system identifier) is supported.

Use a quoted string containing a `WKT`/`EWKT` formatted string or `PreparedStatement.setObject()` to store values, and `ResultSet.getObject(..)` or `ResultSet.getString(..)` to retrieve the values.

## Example

```sql
GEOMETRY
GEOMETRY(POINT)
GEOMETRY(POINT Z)
GEOMETRY(POINT Z, 4326)
GEOMETRY(GEOMETRY, 4326)
```
