#!/usr/bin/env python3
"""Recolor H2 railroad track sprites for the dark H2Sharp theme.

Upstream tiles (h2database.com/html/images/div-*.png, white page theme) are
black line bands on opaque white. Mapping per pixel (all pixels are gray):
  line strength L = 255 - red   (white -> 0, black -> 255)
  out = TRACK_COLOR with alpha = round(alpha * L / 255)
White tile fill becomes transparent; AA grays become translucent track color.
Stdlib only (no PIL). Idempotent.
"""
import struct
import zlib
from pathlib import Path

TRACK = (124, 151, 198)  # #7c97c6 — visible but quiet on dark navy
IMG = Path(__file__).resolve().parent.parent / "assets" / "h2img"


def read_png(p: Path) -> tuple[int, int, bytearray]:
    """Read 8-bit RGBA non-interlaced PNG (stdlib only)."""
    d = p.read_bytes()
    assert d[:8] == b"\x89PNG\r\n\x1a\n"
    pos, w, h, idat = 8, 0, 0, b""
    while pos < len(d):
        (ln,) = struct.unpack(">I", d[pos:pos + 4])
        typ = d[pos + 4:pos + 8]
        data = d[pos + 8:pos + 8 + ln]
        if typ == b"IHDR":
            w, h, bd, ctype, _, _, _ = struct.unpack(">IIBBBBB", data)
            assert (bd, ctype) == (8, 6), (bd, ctype)
        elif typ == b"IDAT":
            idat += data
        pos += 12 + ln
    raw = zlib.decompress(idat)
    ch, stride = 4, w * 4
    out, prev, pos = bytearray(w * h * ch), bytearray(stride), 0
    for y in range(h):
        f = raw[pos]
        pos += 1
        line = bytearray(raw[pos:pos + stride])
        pos += stride
        if f == 1:
            for i in range(ch, len(line)):
                line[i] = (line[i] + line[i - ch]) & 255
        elif f == 2:
            for i in range(len(line)):
                line[i] = (line[i] + prev[i]) & 255
        elif f == 3:
            for i in range(len(line)):
                a = line[i - ch] if i >= ch else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif f == 4:
            for i in range(len(line)):
                a = line[i - ch] if i >= ch else 0
                b = prev[i]
                c = prev[i - ch] if i >= ch else 0
                pp = a + b - c
                pa, pb, pc = abs(pp - a), abs(pp - b), abs(pp - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 255
        out[y * stride:(y + 1) * stride] = line
        prev = line
    return w, h, out


def chunk(typ: bytes, data: bytes) -> bytes:
    import zlib as z

    return struct.pack(">I", len(data)) + typ + data + struct.pack(">I", z.crc32(typ + data) & 0xFFFFFFFF)


def write_png(path: Path, w: int, h: int, px: bytearray) -> None:
    stride = w * 4
    raw = bytearray()
    for y in range(h):
        raw.append(0)  # filter 0 (None)
        raw += px[y * stride:(y + 1) * stride]
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    png += chunk(b"IEND", b"")
    path.write_bytes(png)


for f in sorted(IMG.glob("div-*.png")):
    if (IMG / "orig" / f.name).exists():
        print(f.name, "already recolored (orig backup exists), skip")
        continue
    w, h, px = read_png(f)
    orig = IMG / "orig" / f.name
    orig.parent.mkdir(exist_ok=True)
    orig.write_bytes(f.read_bytes())
    out = bytearray(len(px))
    for i in range(0, len(px), 4):
        r, g, b, a = px[i], px[i + 1], px[i + 2], px[i + 3]
        assert r == g == b, (f.name, r, g, b)
        strength = 255 - r
        out[i] = TRACK[0]
        out[i + 1] = TRACK[1]
        out[i + 2] = TRACK[2]
        out[i + 3] = (a * strength + 127) // 255
    write_png(f, w, h, out)
    print(f.name, "recolored")
print("track color: #%02x%02x%02x" % TRACK)
