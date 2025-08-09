from __future__ import annotations
import re, unicodedata, datetime as _dt

def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = s.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-_]+", "", s)
    s = re.sub(r"-{2,}", "-", s)
    return s or "unnamed"


def canonical_filename(dt: _dt.date, ftype: str, desc: str, ext: str) -> str:
    return f"{dt:%Y-%m-%d}_{slugify(ftype)}_{slugify(desc)}.{slugify(ext)}"
