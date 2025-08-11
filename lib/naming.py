import re, unicodedata
def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode("ascii")
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+","-", s).strip("-")
    return re.sub(r"-{2,}","-", s)
